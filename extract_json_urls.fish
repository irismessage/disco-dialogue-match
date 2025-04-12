#!/usr/bin/env fish
trash urls.txt
for f in songs*.json;
    jq --raw-output '.response.songs[] | .url' $f >> urls.txt; 
end
