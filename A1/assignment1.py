#!/usr/bin/python3

import mysql.connector
import os

import pysam

import numpy as np

__author__ = 'Mock Michael'


class Assignment1:
    
    def __init__(self, gene, bamFileName, genome_reference, file_name):
        self.gene = gene
        self.bam_file_name = bamFileName
    
    #def download_gene_coordinates(self, genome_reference, file_name):

        file_exists = False
        user_action = ""
        
        if os.path.isfile(file_name):
            file_exists = True
            print("ERROR: File already exists")
            user_action = input("Would You like to read [DEFAULT = r] or overwrite [o] the existing file %s, or abort [q]? "
                % file_name)

        if user_action.lower() == "q":
            print("ABORTING")
            sys.exit(0)

        if file_exists == False or user_action.lower() == "o":

            print("Connecting to UCSC to fetch data")
        
            ## Open connection
            cnx = mysql.connector.connect(host='genome-mysql.cse.ucsc.edu',
                user='genomep', passwd='password', db=genome_reference)
        
            ## Get cursor
            cursor = cnx.cursor(buffered = True)
        
            ## Build query fields
            query_fields = ["refGene.name2",
                            "refGene.name",
                            "refGene.chrom",
                            "refGene.txStart",
                            "refGene.txEnd",
                            "refGene.strand",
                            "refGene.exonCount",
                            "refGene.exonStarts",
                            "refGene.exonEnds"]
            ## No. of fields of type string
            nStringFields = 4

            ## Build query
            query = "SELECT DISTINCT {0} FROM refGene WHERE refGene.name2 = {1}".format(",".join(query_fields), "".join(["'", self.gene, "'"]))
        
            ## Execute query
            cursor.execute(query)

            ## Write to file
            rowStr = str(next(cursor)).strip("('").strip(")").replace(" '", " ", nStringFields -1).replace("', ", ", ", nStringFields)

            cursor.execute("SELECT chromInfo.size FROM chromInfo WHERE chrom = 'chr21'")

            rowStr += ", "
            rowStr += str(next(cursor)).strip("(").strip(",)")

            with open(file_name, "w") as fh:
                fh.write(rowStr)
                
            ## Close cursor & connection
            cursor.close()
            cnx.close()
        
            print("Done fetching data")
        
        with open(file_name, "r") as fh:
            self.gene_coordinates = fh.readline().strip("\n").split(", ")

            exon_starts = self.gene_coordinates[7].strip("b'").strip(",'").split(",")
            exon_stops = self.gene_coordinates[8].strip("b'").strip(",'").split(",")

            self.gene_coordinates[7] = []
            self.gene_coordinates[8] = []

            for i in range(0, len(exon_starts)):
                self.gene_coordinates[7].append(int(exon_starts[i]))
                self.gene_coordinates[8].append(int(exon_stops[i]))
        
        self.chromosome = self.gene_coordinates[2]
        self.chr_len = int(self.gene_coordinates[9])
        
    def get_coordinates_of_gene(self, file_name):
        return(self.gene_coordinates)
        
    def get_gene_symbol(self):
        return(self.gene)
                        
    def get_sam_header(self):
        bamfile = pysam.AlignmentFile(self.bam_file_name, "rb")
        header = bamfile.header
        bamfile.close()
        return(header)
        
    def get_properly_paired_reads_of_gene(self):
        bamfile = pysam.AlignmentFile(self.bam_file_name, "rb")
        nPaired = 0
        for read in bamfile.fetch():
            if read.is_paired:
                nPaired += 1
        bamfile.close()
        return(nPaired)
        
    def get_gene_reads_with_indels(self):
        n_indel_reads = 0
        bamfile = pysam.AlignmentFile(self.bam_file_name, "rb")
        for read in bamfile.fetch():
            if ('I' or 'D') in read:
                n_indel_reads += 1
        return(n_indel_reads)
        
    def calculate_total_average_coverage(self):
        bamfile = pysam.AlignmentFile(self.bam_file_name, "rb")

        aln_len = 0

        for seq in bamfile.header["SQ"]:
            aln_len += int(seq["LN"])

        return(aln_len / self.chr_len)
        
    def calculate_gene_average_coverage(self):
        gene_start = int(self.gene_coordinates[3])
        gene_stop = int(self.gene_coordinates[4])

        gene_len = gene_stop - gene_start
        aln_len = 0

        bamfile = pysam.AlignmentFile(self.bam_file_name, "rb")

        coverages = bamfile.count_coverage("chr21", gene_start, gene_stop +1)
        return(np.mean(coverages))

    def get_number_mapped_reads(self):
        bamfile = pysam.AlignmentFile(self.bam_file_name, "rb")

        return(bamfile.mapped) #indexfasta&sort&index before

    def get_region_of_gene(self):
        region = [self.gene_coordinates[2]]

        for i in range(0, len(self.gene_coordinates[7])):
            region.append([self.gene_coordinates[7][i], self.gene_coordinates[8][i]])

        return(region)

    def get_number_of_exons(self):
        return(len(self.gene_coordinates[7]))
    
    def print_summary(self):
        print("Name, ID, Chromosome, Start, Stop, Strand, Exon Count, Exon Starts, Exon Ends")
        print(assignment1.get_coordinates_of_gene(ucsc_file_name))

        print("Number of Properly Paired Reads:")
        print(assignment1.get_properly_paired_reads_of_gene())

        print("Total Average Coverage:")
        print(assignment1.calculate_total_average_coverage())

        print("Gene Average Coverage:")
        print(assignment1.calculate_gene_average_coverage())

        print("Number of Mapped Reads:")
        print(assignment1.get_number_mapped_reads())

        print("Exons (Gene Region):")
        print(assignment1.get_region_of_gene())

        print("Number of Exons:")
        print(assignment1.get_number_of_exons())

    
if __name__ == '__main__':
    gene = "OLIG2"
    ucsc_file_name = "test.ucsc"
    bam_file_name = "chr21.bam"
    genome_reference = "hg38"

    print("Assignment 1")
    assignment1 = Assignment1(gene, bam_file_name, genome_reference, ucsc_file_name)

    assignment1.print_summary()
    
    print("Done with assignment 1")