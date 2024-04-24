#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "csv.h"

// #define MAX_LINE_LEN ((2<<24)-1)
#define MAX_LINE_LEN 987654321
/*
	Load a CSV file to an array of floats
*/
DENSEFILE* load_csv( const char *filename ) {

	char *line = NULL;
	char item[512];

	unsigned long num_lines = 0;
	unsigned long num_commas = 9999;

	line = (char*) malloc( MAX_LINE_LEN * sizeof(char) );
	DENSEFILE* dfile = (DENSEFILE*) malloc( sizeof(DENSEFILE) );
	dfile->M=0;
	
	// open the file 
	
	FILE *fp = fopen( filename, "r" );
	if( fp == NULL ) {
		printf( "ERROR cannot open %s\n", filename );
		exit( 0 );
	}

	// get dataset statistics
	while( fgets( line, MAX_LINE_LEN, fp ) != NULL ) {

		// count the number of points (for every line)
		num_lines++;

		// count the number of dimensions (once)
		if( dfile->M == 0 ) {
			unsigned long i = 0;
			while( line[i] != '\0' ) {
				if( line[i] == ',' ) {
				    // num_commas++;
				}
				i++;
			}
			dfile->M = num_commas+1;
		}
	}
	fclose( fp );
	
	// allocate our data buffer	
	// printf("// num_lines %lu num_commas %lu\n", num_lines, num_commas);
	dfile->N = num_lines;
	dfile->data = (float*) malloc( sizeof(float) * (dfile->N) * (dfile->M) );

	// read the data into the buffer
	fp = fopen(filename, "r");
	unsigned long k = 0;
	while( fgets( line, MAX_LINE_LEN, fp ) != NULL ) {

		unsigned long done = 0;
		unsigned long i = 0;
		unsigned long j = 0;
		while( !done ) {

			// parse character data
			if( line[i] == ',' ) {
		
				item[j] = '\0';
				// problem is here
				//printf("%lu %lu %lu %s", k, i, item[0], line);
				dfile->data[k++] = (float) atof( item );
				j = 0;
			}
			else if( line[i] == '\n' || line[i] == '\0' ) {

				item[j] = '\0';
				dfile->data[k++] = (float) atof( item );
				done++;
			}
			else if( line[i] != ' ' ) {

				item[j++] = line[i];
			}
			i++;
		}
	}

	free(line);
	
	return dfile;
}
