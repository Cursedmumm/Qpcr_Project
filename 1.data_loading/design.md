Janus robot generates an XML file that tracks the increasing luminescence after each cycle (45 in this case)

user can go back to the machine and perform a ct calculation that results in a .ct file containing ct values which are formatted as a 2^ number.

The text file contains information on the melting temperatures tm1 and sometimes tm2, check the relevance for this info

using the information on the well positioning a table could be generated that contains all the gene data, one issue is that all wells are included in the rapport, even empty ones.

if user does not name his samples they would share a name with the empty wells but if gene amplification did not occur then the ct values would be similar to the empty ones = dilemma.

perhaps a check could be done to see if their are gene names present in the document and if not too ask the user to relabel the well positions used in the experiment.

just need to make sure python can easily read this .ct file and merge it with the .txt

