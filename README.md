# FilterFasta

Filter FASTA file based on list of sequence identifiers and extract subsequences from start to end position
and saves subsequences in the FASTA file.

# Usage

The input file for the script is FASTA file and file with seq ids and start, end positions to extract:
```bash
./filter_fasta_subseq.py -f input.fasta -s seq_id_start_end.dat -o output.fasta
```

The `seq\_id\_start\_end.dat` has at least 3 columns:
* sequence id
* start position
* end position

That extract sequence from start to end position(inclusive) and save it to the 
output FASTA with the same sequence id and description.
Format of the `seq\_id\_start\_end.dat` and `filter\_fasta\_subseq.py` is consistent with QIIME
`filter\_fasta.py` that can be used to extract sequences based on seq id.

At present sequence id should be only seen once in `seq\_id\_start\_end.dat`.

## End position before Start position

In this case we extract sequence from End to Start.

# Testing

To run unit tests use:
```
nosetests
```

