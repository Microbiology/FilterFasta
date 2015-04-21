# FilterFasta

Filter FASTA file based on list of sequence identifiers and extract subsequences from start to end position
and saves subsequences in the FASTA file.

# Usage

The input file for the script is FASTA file and file with seq ids and start, end position to extract:
```bash
./filter_fasta_subseq.py -f input.fasta -s seq_id_start_end.dat -o output.fasta
```

The `seq\_id\_start\_end` has at least 3 columns:
* sequence id
* start position
* end position

That extract sequence from start to end position(inclusive) and save it to output FASTA with the same sequence id.

## End position before Start position

???

# Testing
```
nosetests
```


