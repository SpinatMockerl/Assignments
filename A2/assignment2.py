#! /usr/bin/env python3

#import vcf

__author__ = 'Mock Michael'


class Assignment2:
    
    def __init__(self, main_file_name):
        ## Check if pyvcf is installed
        #print("PyVCF version: %s" % vcf.VERSION)
        self.main_file_name = main_file_name
        

    def get_average_quality_of_file(self):
        n = 0
        score = 0

        with open(main_file_name, "r") as vcf_file:
            for line in vcf_file:
                if line[0] != "#":
                    n += 1
                    attr = line.split("\t")
                    score += int(attr[5])

        return(score / n)
        

    def get_total_number_of_variants_of_file(self):
        n = 0

        with open(main_file_name, "r") as vcf_file:
            for line in vcf_file:
                if line[0] != "#":
                    n += 1
        
        return(n)
    
    def get_variant_caller_of_vcf(self):
        '''
        Return the variant caller name
        :return: 
        '''
        print("TODO")
        
        
    def get_human_reference_version(self):
        '''
        Return the genome reference version
        :return: 
        '''
        print("TODO")
        
        
    def get_number_of_indels(self):
        '''
        Return the number of identified INDELs
        :return:
        '''
        print("TODO")
        

    def get_number_of_snvs(self):
        '''
        Return the number of SNVs
        :return: 
        '''
        print("TODO")
        
    def get_number_of_heterozygous_variants(self):
        '''
        Return the number of heterozygous variants
        :return: 
        '''
        print("TODO")
        
    
    def merge_chrs_into_one_vcf(self):
        '''
        Creates one VCF containing all variants of chr21 and chr22
        :return:
        '''
        print("TODO")
        
        print("Number of total variants")
        
    
    def print_summary(self):
        print("Print all results here")
    
    

if __name__ == '__main__':
    print("Assignment 2")
    assignment2 = Assignment2()
    assignment2.print_summary()
    print("Done with assignment 2")
   
    



