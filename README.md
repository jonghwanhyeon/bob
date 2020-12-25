# bob
Hello. This is Bob Ross.

## Usage
```bash
$ wget \
    --output-document=output.png \
    --header="Content-Type: application/json" \
    --post-data '{"url":  "https://source.unsplash.com/random/1024x1024",
                    "transforms": [
                        {"blur": 13},
                        {"select": [{">": [{"getitem": [{"to_hsl": {"representative": []}}, 2]}, 80]},
                            {"tint": [0, 0, 0, 0.20]}
                        ]}
                    ]}' \
    http://localhost:5000
```