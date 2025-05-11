#!/bin/bash

# Path to YAML and template
QUOTE_YAML="batches/quote_001.yaml"
TEMPLATE="templates/quote_template.md"
OUTPUT="output/quote_001_response.md"

# Extract fields using grep and cut
ORIGIN=$(grep "origin:" $QUOTE_YAML | cut -d ":" -f2- | xargs)
DESTINATION=$(grep "destination:" $QUOTE_YAML | cut -d ":" -f2- | xargs)
COMMODITY=$(grep "commodity:" $QUOTE_YAML | cut -d ":" -f2- | xargs)
WEIGHT=$(grep "weight:" $QUOTE_YAML | cut -d ":" -f2- | xargs)
DIMENSIONS=$(grep "dimensions:" $QUOTE_YAML | cut -d ":" -f2- | xargs)
RATE="\$4,250"  # Hardcoded for now

# Use the template and replace placeholders
cat $TEMPLATE \
  | sed "s/\[Origin City, State\]/$ORIGIN/" \
  | sed "s/\[Destination City, State\]/$DESTINATION/" \
  | sed "s/\[Commodity Name\]/$COMMODITY/" \
  | sed "s/\[Weight\]/$WEIGHT/" \
  | sed "s/\[LxWxH\]/$DIMENSIONS/" \
  | sed "s/\[Rate\]/$RATE/" > $OUTPUT

echo "Quote generated at $OUTPUT"
