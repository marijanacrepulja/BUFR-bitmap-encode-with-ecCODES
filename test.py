#  Using ecCodes version: 2.43.0

import sys
import traceback

from eccodes import *


def bufr_encode():
    ibufr = codes_bufr_new_from_samples('BUFR4')
     # Define bitmap, 
     # firstOrderStatistic will be assing to the descriptor where the 0 present in the ivalues array
     # If you count backwards from 2-24-000,it come to the amplitudeOfEcho 
    ivalues = (
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 0, 1, 1, 1, 1, 1,
        ) # 30 values meaning 30 relpication as defined in the BUFR template
    codes_set_array(ibufr, 'inputDataPresentIndicator', ivalues)

    codes_set(ibufr, 'edition', 4)
    codes_set(ibufr, 'masterTableNumber', 0)
    codes_set(ibufr, 'bufrHeaderCentre', 34)
    codes_set(ibufr, 'bufrHeaderSubCentre', 0)
    codes_set(ibufr, 'updateSequenceNumber', 0)
    codes_set(ibufr, 'dataCategory', 5)
    codes_set(ibufr, 'internationalDataSubCategory', 255)
    codes_set(ibufr, 'dataSubCategory', 0)
    codes_set(ibufr, 'masterTablesVersionNumber', 45)
    codes_set(ibufr, 'localTablesVersionNumber', 0)
    codes_set(ibufr, 'typicalYear', 2025)
    codes_set(ibufr, 'typicalMonth', 9)
    codes_set(ibufr, 'typicalDay', 29)
    codes_set(ibufr, 'typicalHour', 0)
    codes_set(ibufr, 'typicalMinute', 55)
    codes_set(ibufr, 'typicalSecond', 5)
    codes_set(ibufr, 'numberOfSubsets', 8000)
    codes_set(ibufr, 'observedData', 1)
    codes_set(ibufr, 'compressedData', 1)
    ivalues = 321040
        
    # Create the structure of the data section
    codes_set(ibufr, 'unexpandedDescriptors', ivalues)
    codes_set(ibufr, '#1#firstOrderStatistics', 10)
    codes_set(ibufr, '#1#amplitudeOfEcho', 30)
    # assign firstOrderStatisticalValue to amplitudeOfEcho within bitmap
    codes_set(ibufr, '#1#amplitudeOfEcho->firstOrderStatisticalValue',3)

# Encode the keys back in the data section
    codes_set(ibufr, 'pack', 1)

    outfile = open('outfile.bufr', 'wb')
    codes_write(ibufr, outfile)
    print ("Created output BUFR file 'outfile.bufr'")
    codes_release(ibufr)
    outfile.close()

def main():
    try:
        bufr_encode()
    except CodesInternalError as err:
        traceback.print_exc(file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())

