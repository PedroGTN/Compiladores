# Generated from Jander.g4 by ANTLR 4.11.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,72,581,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,
        39,7,39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,
        45,2,46,7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,
        52,7,52,2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,
        58,2,59,7,59,2,60,7,60,2,61,7,61,2,62,7,62,2,63,7,63,2,64,7,64,2,
        65,7,65,2,66,7,66,2,67,7,67,2,68,7,68,2,69,7,69,2,70,7,70,2,71,7,
        71,2,72,7,72,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,1,4,1,5,1,5,
        1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,1,10,1,10,1,11,1,11,1,11,1,12,
        1,12,1,12,1,13,1,13,1,13,1,14,1,14,1,15,1,15,1,16,1,16,1,16,1,16,
        1,17,1,17,1,17,1,18,1,18,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,
        1,19,1,19,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,21,1,21,1,21,
        1,21,1,21,1,21,1,21,1,21,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,
        1,23,1,23,1,23,1,23,1,23,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,25,
        1,25,1,25,1,25,1,25,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,27,
        1,27,1,27,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,29,1,29,1,29,1,29,
        1,29,1,29,1,30,1,30,1,30,1,30,1,30,1,31,1,31,1,31,1,31,1,31,1,32,
        1,32,1,32,1,32,1,32,1,32,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,
        1,33,1,34,1,34,1,34,1,34,1,34,1,35,1,35,1,35,1,35,1,36,1,36,1,36,
        1,36,1,36,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,38,1,38,
        1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,39,1,39,1,39,1,39,1,39,1,39,
        1,39,1,39,1,39,1,39,1,39,1,39,1,39,1,40,1,40,1,40,1,40,1,40,1,40,
        1,40,1,40,1,40,1,41,1,41,1,41,1,41,1,41,1,41,1,41,1,41,1,41,1,41,
        1,41,1,41,1,41,1,42,1,42,1,42,1,42,1,42,1,43,1,43,1,43,1,43,1,43,
        1,43,1,43,1,43,1,43,1,43,1,43,1,43,1,43,1,44,1,44,1,44,1,44,1,44,
        1,44,1,44,1,44,1,44,1,44,1,44,1,44,1,44,1,44,1,44,1,44,1,44,1,45,
        1,45,1,45,1,45,1,46,1,46,1,46,1,46,1,46,1,46,1,46,1,47,1,47,1,47,
        1,47,1,47,1,47,1,47,1,47,1,48,1,48,1,48,1,48,1,48,1,48,1,48,1,48,
        1,48,1,48,1,48,1,49,1,49,1,49,1,49,1,49,1,49,1,49,1,49,1,49,1,49,
        1,50,1,50,1,50,1,50,1,50,1,50,1,50,1,50,1,50,1,50,1,50,1,51,1,51,
        1,51,1,51,1,51,1,51,1,52,1,52,1,52,1,52,1,52,1,52,1,52,1,52,1,52,
        1,52,1,52,1,52,1,52,1,52,1,53,1,53,1,54,4,54,470,8,54,11,54,12,54,
        471,1,55,4,55,475,8,55,11,55,12,55,476,1,55,1,55,4,55,481,8,55,11,
        55,12,55,482,3,55,485,8,55,1,56,1,56,1,56,1,56,1,56,1,56,3,56,493,
        8,56,1,57,1,57,5,57,497,8,57,10,57,12,57,500,9,57,1,58,1,58,1,58,
        1,58,1,58,1,58,3,58,508,8,58,1,59,1,59,1,59,5,59,513,8,59,10,59,
        12,59,516,9,59,1,59,1,59,1,60,1,60,1,60,1,61,1,61,5,61,525,8,61,
        10,61,12,61,528,9,61,1,61,1,61,1,61,1,61,1,62,1,62,1,62,1,62,1,63,
        1,63,1,63,1,63,1,63,1,63,1,63,1,63,1,63,3,63,547,8,63,1,64,1,64,
        1,65,1,65,1,66,1,66,1,67,1,67,1,68,1,68,1,69,1,69,1,70,1,70,5,70,
        563,8,70,10,70,12,70,566,9,70,1,70,1,70,1,71,1,71,1,71,5,71,573,
        8,71,10,71,12,71,576,9,71,1,71,1,71,1,72,1,72,0,0,73,1,1,3,2,5,3,
        7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,12,25,13,27,14,29,15,
        31,16,33,17,35,18,37,19,39,20,41,21,43,22,45,23,47,24,49,25,51,26,
        53,27,55,28,57,29,59,30,61,31,63,32,65,33,67,34,69,35,71,36,73,37,
        75,38,77,39,79,40,81,41,83,42,85,43,87,44,89,45,91,46,93,47,95,48,
        97,49,99,50,101,51,103,52,105,53,107,54,109,55,111,56,113,57,115,
        58,117,59,119,60,121,0,123,61,125,62,127,63,129,64,131,65,133,66,
        135,67,137,68,139,69,141,70,143,71,145,72,1,0,7,3,0,65,90,95,95,
        97,122,4,0,48,57,65,90,95,95,97,122,3,0,38,38,46,46,94,94,4,0,10,
        10,34,34,39,39,92,92,2,0,10,10,125,125,3,0,9,10,13,13,32,32,4,0,
        37,37,42,43,45,45,47,47,600,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,
        0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,
        17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,
        27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,0,0,0,35,1,0,0,0,0,
        37,1,0,0,0,0,39,1,0,0,0,0,41,1,0,0,0,0,43,1,0,0,0,0,45,1,0,0,0,0,
        47,1,0,0,0,0,49,1,0,0,0,0,51,1,0,0,0,0,53,1,0,0,0,0,55,1,0,0,0,0,
        57,1,0,0,0,0,59,1,0,0,0,0,61,1,0,0,0,0,63,1,0,0,0,0,65,1,0,0,0,0,
        67,1,0,0,0,0,69,1,0,0,0,0,71,1,0,0,0,0,73,1,0,0,0,0,75,1,0,0,0,0,
        77,1,0,0,0,0,79,1,0,0,0,0,81,1,0,0,0,0,83,1,0,0,0,0,85,1,0,0,0,0,
        87,1,0,0,0,0,89,1,0,0,0,0,91,1,0,0,0,0,93,1,0,0,0,0,95,1,0,0,0,0,
        97,1,0,0,0,0,99,1,0,0,0,0,101,1,0,0,0,0,103,1,0,0,0,0,105,1,0,0,
        0,0,107,1,0,0,0,0,109,1,0,0,0,0,111,1,0,0,0,0,113,1,0,0,0,0,115,
        1,0,0,0,0,117,1,0,0,0,0,119,1,0,0,0,0,123,1,0,0,0,0,125,1,0,0,0,
        0,127,1,0,0,0,0,129,1,0,0,0,0,131,1,0,0,0,0,133,1,0,0,0,0,135,1,
        0,0,0,0,137,1,0,0,0,0,139,1,0,0,0,0,141,1,0,0,0,0,143,1,0,0,0,0,
        145,1,0,0,0,1,147,1,0,0,0,3,149,1,0,0,0,5,151,1,0,0,0,7,153,1,0,
        0,0,9,155,1,0,0,0,11,158,1,0,0,0,13,161,1,0,0,0,15,163,1,0,0,0,17,
        165,1,0,0,0,19,167,1,0,0,0,21,169,1,0,0,0,23,171,1,0,0,0,25,174,
        1,0,0,0,27,177,1,0,0,0,29,180,1,0,0,0,31,182,1,0,0,0,33,184,1,0,
        0,0,35,188,1,0,0,0,37,191,1,0,0,0,39,193,1,0,0,0,41,203,1,0,0,0,
        43,211,1,0,0,0,45,219,1,0,0,0,47,227,1,0,0,0,49,232,1,0,0,0,51,239,
        1,0,0,0,53,244,1,0,0,0,55,252,1,0,0,0,57,255,1,0,0,0,59,262,1,0,
        0,0,61,268,1,0,0,0,63,273,1,0,0,0,65,278,1,0,0,0,67,284,1,0,0,0,
        69,293,1,0,0,0,71,298,1,0,0,0,73,302,1,0,0,0,75,307,1,0,0,0,77,316,
        1,0,0,0,79,325,1,0,0,0,81,338,1,0,0,0,83,347,1,0,0,0,85,360,1,0,
        0,0,87,365,1,0,0,0,89,378,1,0,0,0,91,395,1,0,0,0,93,399,1,0,0,0,
        95,406,1,0,0,0,97,414,1,0,0,0,99,425,1,0,0,0,101,435,1,0,0,0,103,
        446,1,0,0,0,105,452,1,0,0,0,107,466,1,0,0,0,109,469,1,0,0,0,111,
        474,1,0,0,0,113,492,1,0,0,0,115,494,1,0,0,0,117,507,1,0,0,0,119,
        509,1,0,0,0,121,519,1,0,0,0,123,522,1,0,0,0,125,533,1,0,0,0,127,
        546,1,0,0,0,129,548,1,0,0,0,131,550,1,0,0,0,133,552,1,0,0,0,135,
        554,1,0,0,0,137,556,1,0,0,0,139,558,1,0,0,0,141,560,1,0,0,0,143,
        569,1,0,0,0,145,579,1,0,0,0,147,148,5,61,0,0,148,2,1,0,0,0,149,150,
        5,44,0,0,150,4,1,0,0,0,151,152,5,46,0,0,152,6,1,0,0,0,153,154,5,
        94,0,0,154,8,1,0,0,0,155,156,5,60,0,0,156,157,5,45,0,0,157,10,1,
        0,0,0,158,159,5,46,0,0,159,160,5,46,0,0,160,12,1,0,0,0,161,162,5,
        43,0,0,162,14,1,0,0,0,163,164,5,42,0,0,164,16,1,0,0,0,165,166,5,
        47,0,0,166,18,1,0,0,0,167,168,5,37,0,0,168,20,1,0,0,0,169,170,5,
        38,0,0,170,22,1,0,0,0,171,172,5,60,0,0,172,173,5,62,0,0,173,24,1,
        0,0,0,174,175,5,62,0,0,175,176,5,61,0,0,176,26,1,0,0,0,177,178,5,
        60,0,0,178,179,5,61,0,0,179,28,1,0,0,0,180,181,5,62,0,0,181,30,1,
        0,0,0,182,183,5,60,0,0,183,32,1,0,0,0,184,185,5,110,0,0,185,186,
        5,97,0,0,186,187,5,111,0,0,187,34,1,0,0,0,188,189,5,111,0,0,189,
        190,5,117,0,0,190,36,1,0,0,0,191,192,5,101,0,0,192,38,1,0,0,0,193,
        194,5,97,0,0,194,195,5,108,0,0,195,196,5,103,0,0,196,197,5,111,0,
        0,197,198,5,114,0,0,198,199,5,105,0,0,199,200,5,116,0,0,200,201,
        5,109,0,0,201,202,5,111,0,0,202,40,1,0,0,0,203,204,5,100,0,0,204,
        205,5,101,0,0,205,206,5,99,0,0,206,207,5,108,0,0,207,208,5,97,0,
        0,208,209,5,114,0,0,209,210,5,101,0,0,210,42,1,0,0,0,211,212,5,108,
        0,0,212,213,5,105,0,0,213,214,5,116,0,0,214,215,5,101,0,0,215,216,
        5,114,0,0,216,217,5,97,0,0,217,218,5,108,0,0,218,44,1,0,0,0,219,
        220,5,105,0,0,220,221,5,110,0,0,221,222,5,116,0,0,222,223,5,101,
        0,0,223,224,5,105,0,0,224,225,5,114,0,0,225,226,5,111,0,0,226,46,
        1,0,0,0,227,228,5,114,0,0,228,229,5,101,0,0,229,230,5,97,0,0,230,
        231,5,108,0,0,231,48,1,0,0,0,232,233,5,108,0,0,233,234,5,111,0,0,
        234,235,5,103,0,0,235,236,5,105,0,0,236,237,5,99,0,0,237,238,5,111,
        0,0,238,50,1,0,0,0,239,240,5,108,0,0,240,241,5,101,0,0,241,242,5,
        105,0,0,242,243,5,97,0,0,243,52,1,0,0,0,244,245,5,101,0,0,245,246,
        5,115,0,0,246,247,5,99,0,0,247,248,5,114,0,0,248,249,5,101,0,0,249,
        250,5,118,0,0,250,251,5,97,0,0,251,54,1,0,0,0,252,253,5,115,0,0,
        253,254,5,101,0,0,254,56,1,0,0,0,255,256,5,102,0,0,256,257,5,105,
        0,0,257,258,5,109,0,0,258,259,5,95,0,0,259,260,5,115,0,0,260,261,
        5,101,0,0,261,58,1,0,0,0,262,263,5,101,0,0,263,264,5,110,0,0,264,
        265,5,116,0,0,265,266,5,97,0,0,266,267,5,111,0,0,267,60,1,0,0,0,
        268,269,5,99,0,0,269,270,5,97,0,0,270,271,5,115,0,0,271,272,5,111,
        0,0,272,62,1,0,0,0,273,274,5,115,0,0,274,275,5,101,0,0,275,276,5,
        106,0,0,276,277,5,97,0,0,277,64,1,0,0,0,278,279,5,115,0,0,279,280,
        5,101,0,0,280,281,5,110,0,0,281,282,5,97,0,0,282,283,5,111,0,0,283,
        66,1,0,0,0,284,285,5,102,0,0,285,286,5,105,0,0,286,287,5,109,0,0,
        287,288,5,95,0,0,288,289,5,99,0,0,289,290,5,97,0,0,290,291,5,115,
        0,0,291,292,5,111,0,0,292,68,1,0,0,0,293,294,5,112,0,0,294,295,5,
        97,0,0,295,296,5,114,0,0,296,297,5,97,0,0,297,70,1,0,0,0,298,299,
        5,97,0,0,299,300,5,116,0,0,300,301,5,101,0,0,301,72,1,0,0,0,302,
        303,5,102,0,0,303,304,5,97,0,0,304,305,5,99,0,0,305,306,5,97,0,0,
        306,74,1,0,0,0,307,308,5,102,0,0,308,309,5,105,0,0,309,310,5,109,
        0,0,310,311,5,95,0,0,311,312,5,112,0,0,312,313,5,97,0,0,313,314,
        5,114,0,0,314,315,5,97,0,0,315,76,1,0,0,0,316,317,5,101,0,0,317,
        318,5,110,0,0,318,319,5,113,0,0,319,320,5,117,0,0,320,321,5,97,0,
        0,321,322,5,110,0,0,322,323,5,116,0,0,323,324,5,111,0,0,324,78,1,
        0,0,0,325,326,5,102,0,0,326,327,5,105,0,0,327,328,5,109,0,0,328,
        329,5,95,0,0,329,330,5,101,0,0,330,331,5,110,0,0,331,332,5,113,0,
        0,332,333,5,117,0,0,333,334,5,97,0,0,334,335,5,110,0,0,335,336,5,
        116,0,0,336,337,5,111,0,0,337,80,1,0,0,0,338,339,5,114,0,0,339,340,
        5,101,0,0,340,341,5,103,0,0,341,342,5,105,0,0,342,343,5,115,0,0,
        343,344,5,116,0,0,344,345,5,114,0,0,345,346,5,111,0,0,346,82,1,0,
        0,0,347,348,5,102,0,0,348,349,5,105,0,0,349,350,5,109,0,0,350,351,
        5,95,0,0,351,352,5,114,0,0,352,353,5,101,0,0,353,354,5,103,0,0,354,
        355,5,105,0,0,355,356,5,115,0,0,356,357,5,116,0,0,357,358,5,114,
        0,0,358,359,5,111,0,0,359,84,1,0,0,0,360,361,5,116,0,0,361,362,5,
        105,0,0,362,363,5,112,0,0,363,364,5,111,0,0,364,86,1,0,0,0,365,366,
        5,112,0,0,366,367,5,114,0,0,367,368,5,111,0,0,368,369,5,99,0,0,369,
        370,5,101,0,0,370,371,5,100,0,0,371,372,5,105,0,0,372,373,5,109,
        0,0,373,374,5,101,0,0,374,375,5,110,0,0,375,376,5,116,0,0,376,377,
        5,111,0,0,377,88,1,0,0,0,378,379,5,102,0,0,379,380,5,105,0,0,380,
        381,5,109,0,0,381,382,5,95,0,0,382,383,5,112,0,0,383,384,5,114,0,
        0,384,385,5,111,0,0,385,386,5,99,0,0,386,387,5,101,0,0,387,388,5,
        100,0,0,388,389,5,105,0,0,389,390,5,109,0,0,390,391,5,101,0,0,391,
        392,5,110,0,0,392,393,5,116,0,0,393,394,5,111,0,0,394,90,1,0,0,0,
        395,396,5,118,0,0,396,397,5,97,0,0,397,398,5,114,0,0,398,92,1,0,
        0,0,399,400,5,102,0,0,400,401,5,117,0,0,401,402,5,110,0,0,402,403,
        5,99,0,0,403,404,5,97,0,0,404,405,5,111,0,0,405,94,1,0,0,0,406,407,
        5,114,0,0,407,408,5,101,0,0,408,409,5,116,0,0,409,410,5,111,0,0,
        410,411,5,114,0,0,411,412,5,110,0,0,412,413,5,101,0,0,413,96,1,0,
        0,0,414,415,5,102,0,0,415,416,5,105,0,0,416,417,5,109,0,0,417,418,
        5,95,0,0,418,419,5,102,0,0,419,420,5,117,0,0,420,421,5,110,0,0,421,
        422,5,99,0,0,422,423,5,97,0,0,423,424,5,111,0,0,424,98,1,0,0,0,425,
        426,5,99,0,0,426,427,5,111,0,0,427,428,5,110,0,0,428,429,5,115,0,
        0,429,430,5,116,0,0,430,431,5,97,0,0,431,432,5,110,0,0,432,433,5,
        116,0,0,433,434,5,101,0,0,434,100,1,0,0,0,435,436,5,118,0,0,436,
        437,5,101,0,0,437,438,5,114,0,0,438,439,5,100,0,0,439,440,5,97,0,
        0,440,441,5,100,0,0,441,442,5,101,0,0,442,443,5,105,0,0,443,444,
        5,114,0,0,444,445,5,111,0,0,445,102,1,0,0,0,446,447,5,102,0,0,447,
        448,5,97,0,0,448,449,5,108,0,0,449,450,5,115,0,0,450,451,5,111,0,
        0,451,104,1,0,0,0,452,453,5,102,0,0,453,454,5,105,0,0,454,455,5,
        109,0,0,455,456,5,95,0,0,456,457,5,97,0,0,457,458,5,108,0,0,458,
        459,5,103,0,0,459,460,5,111,0,0,460,461,5,114,0,0,461,462,5,105,
        0,0,462,463,5,116,0,0,463,464,5,109,0,0,464,465,5,111,0,0,465,106,
        1,0,0,0,466,467,5,45,0,0,467,108,1,0,0,0,468,470,2,48,57,0,469,468,
        1,0,0,0,470,471,1,0,0,0,471,469,1,0,0,0,471,472,1,0,0,0,472,110,
        1,0,0,0,473,475,2,48,57,0,474,473,1,0,0,0,475,476,1,0,0,0,476,474,
        1,0,0,0,476,477,1,0,0,0,477,484,1,0,0,0,478,480,5,46,0,0,479,481,
        2,48,57,0,480,479,1,0,0,0,481,482,1,0,0,0,482,480,1,0,0,0,482,483,
        1,0,0,0,483,485,1,0,0,0,484,478,1,0,0,0,484,485,1,0,0,0,485,112,
        1,0,0,0,486,493,5,101,0,0,487,488,5,111,0,0,488,493,5,117,0,0,489,
        490,5,110,0,0,490,491,5,97,0,0,491,493,5,111,0,0,492,486,1,0,0,0,
        492,487,1,0,0,0,492,489,1,0,0,0,493,114,1,0,0,0,494,498,7,0,0,0,
        495,497,7,1,0,0,496,495,1,0,0,0,497,500,1,0,0,0,498,496,1,0,0,0,
        498,499,1,0,0,0,499,116,1,0,0,0,500,498,1,0,0,0,501,508,5,44,0,0,
        502,503,5,46,0,0,503,508,5,46,0,0,504,505,5,60,0,0,505,508,5,45,
        0,0,506,508,7,2,0,0,507,501,1,0,0,0,507,502,1,0,0,0,507,504,1,0,
        0,0,507,506,1,0,0,0,508,118,1,0,0,0,509,514,5,34,0,0,510,513,3,121,
        60,0,511,513,8,3,0,0,512,510,1,0,0,0,512,511,1,0,0,0,513,516,1,0,
        0,0,514,512,1,0,0,0,514,515,1,0,0,0,515,517,1,0,0,0,516,514,1,0,
        0,0,517,518,5,34,0,0,518,120,1,0,0,0,519,520,5,92,0,0,520,521,5,
        39,0,0,521,122,1,0,0,0,522,526,5,123,0,0,523,525,8,4,0,0,524,523,
        1,0,0,0,525,528,1,0,0,0,526,524,1,0,0,0,526,527,1,0,0,0,527,529,
        1,0,0,0,528,526,1,0,0,0,529,530,5,125,0,0,530,531,1,0,0,0,531,532,
        6,61,0,0,532,124,1,0,0,0,533,534,7,5,0,0,534,535,1,0,0,0,535,536,
        6,62,0,0,536,126,1,0,0,0,537,547,5,62,0,0,538,539,5,62,0,0,539,547,
        5,61,0,0,540,547,5,60,0,0,541,542,5,60,0,0,542,547,5,61,0,0,543,
        544,5,60,0,0,544,547,5,62,0,0,545,547,5,61,0,0,546,537,1,0,0,0,546,
        538,1,0,0,0,546,540,1,0,0,0,546,541,1,0,0,0,546,543,1,0,0,0,546,
        545,1,0,0,0,547,128,1,0,0,0,548,549,7,6,0,0,549,130,1,0,0,0,550,
        551,5,58,0,0,551,132,1,0,0,0,552,553,5,40,0,0,553,134,1,0,0,0,554,
        555,5,41,0,0,555,136,1,0,0,0,556,557,5,91,0,0,557,138,1,0,0,0,558,
        559,5,93,0,0,559,140,1,0,0,0,560,564,5,123,0,0,561,563,8,4,0,0,562,
        561,1,0,0,0,563,566,1,0,0,0,564,562,1,0,0,0,564,565,1,0,0,0,565,
        567,1,0,0,0,566,564,1,0,0,0,567,568,5,10,0,0,568,142,1,0,0,0,569,
        574,5,34,0,0,570,573,3,121,60,0,571,573,8,3,0,0,572,570,1,0,0,0,
        572,571,1,0,0,0,573,576,1,0,0,0,574,572,1,0,0,0,574,575,1,0,0,0,
        575,577,1,0,0,0,576,574,1,0,0,0,577,578,5,10,0,0,578,144,1,0,0,0,
        579,580,9,0,0,0,580,146,1,0,0,0,15,0,471,476,482,484,492,498,507,
        512,514,526,546,564,572,574,1,6,0,0
    ]

class JanderLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    T__16 = 17
    T__17 = 18
    T__18 = 19
    ALGORITMO = 20
    DECLARE = 21
    LITERAL = 22
    INTEIRO = 23
    REAL = 24
    LOGICO = 25
    LEIA = 26
    ESCREVA = 27
    SE = 28
    FIM_SE = 29
    ENTAO = 30
    CASO = 31
    SEJA = 32
    SENAO = 33
    FIM_CASO = 34
    PARA = 35
    ATE = 36
    FACA = 37
    FIM_PARA = 38
    ENQUANTO = 39
    FIM_ENQUANTO = 40
    REGISTRO = 41
    FIM_REGISTRO = 42
    TIPO = 43
    PROCEDIMENTO = 44
    FIM_PROCEDIMENTO = 45
    VAR = 46
    FUNCAO = 47
    RETORNE = 48
    FIM_FUNCAO = 49
    CONSTANTE = 50
    VERDADEIRO = 51
    FALSO = 52
    FIM_ALGORITMO = 53
    SINAL = 54
    NUM_INT = 55
    NUM_REAL = 56
    OP_LOGICO = 57
    IDENT = 58
    PONTUACAO = 59
    CADEIA = 60
    COMENTARIO = 61
    WS = 62
    OP_REL = 63
    OP_ARIT = 64
    DELIM = 65
    ABREPAR = 66
    FECHAPAR = 67
    ABRECHAVE = 68
    FECHACHAVE = 69
    COMENTARIO_NAO_FECHADO = 70
    CADEIA_NAO_FECHADA = 71
    ERRO = 72

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "','", "'.'", "'^'", "'<-'", "'..'", "'+'", "'*'", "'/'", 
            "'%'", "'&'", "'<>'", "'>='", "'<='", "'>'", "'<'", "'nao'", 
            "'ou'", "'e'", "'algoritmo'", "'declare'", "'literal'", "'inteiro'", 
            "'real'", "'logico'", "'leia'", "'escreva'", "'se'", "'fim_se'", 
            "'entao'", "'caso'", "'seja'", "'senao'", "'fim_caso'", "'para'", 
            "'ate'", "'faca'", "'fim_para'", "'enquanto'", "'fim_enquanto'", 
            "'registro'", "'fim_registro'", "'tipo'", "'procedimento'", 
            "'fim_procedimento'", "'var'", "'funcao'", "'retorne'", "'fim_funcao'", 
            "'constante'", "'verdadeiro'", "'falso'", "'fim_algoritmo'", 
            "'-'", "':'", "'('", "')'", "'['", "']'" ]

    symbolicNames = [ "<INVALID>",
            "ALGORITMO", "DECLARE", "LITERAL", "INTEIRO", "REAL", "LOGICO", 
            "LEIA", "ESCREVA", "SE", "FIM_SE", "ENTAO", "CASO", "SEJA", 
            "SENAO", "FIM_CASO", "PARA", "ATE", "FACA", "FIM_PARA", "ENQUANTO", 
            "FIM_ENQUANTO", "REGISTRO", "FIM_REGISTRO", "TIPO", "PROCEDIMENTO", 
            "FIM_PROCEDIMENTO", "VAR", "FUNCAO", "RETORNE", "FIM_FUNCAO", 
            "CONSTANTE", "VERDADEIRO", "FALSO", "FIM_ALGORITMO", "SINAL", 
            "NUM_INT", "NUM_REAL", "OP_LOGICO", "IDENT", "PONTUACAO", "CADEIA", 
            "COMENTARIO", "WS", "OP_REL", "OP_ARIT", "DELIM", "ABREPAR", 
            "FECHAPAR", "ABRECHAVE", "FECHACHAVE", "COMENTARIO_NAO_FECHADO", 
            "CADEIA_NAO_FECHADA", "ERRO" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "ALGORITMO", 
                  "DECLARE", "LITERAL", "INTEIRO", "REAL", "LOGICO", "LEIA", 
                  "ESCREVA", "SE", "FIM_SE", "ENTAO", "CASO", "SEJA", "SENAO", 
                  "FIM_CASO", "PARA", "ATE", "FACA", "FIM_PARA", "ENQUANTO", 
                  "FIM_ENQUANTO", "REGISTRO", "FIM_REGISTRO", "TIPO", "PROCEDIMENTO", 
                  "FIM_PROCEDIMENTO", "VAR", "FUNCAO", "RETORNE", "FIM_FUNCAO", 
                  "CONSTANTE", "VERDADEIRO", "FALSO", "FIM_ALGORITMO", "SINAL", 
                  "NUM_INT", "NUM_REAL", "OP_LOGICO", "IDENT", "PONTUACAO", 
                  "CADEIA", "ESC_SEQ", "COMENTARIO", "WS", "OP_REL", "OP_ARIT", 
                  "DELIM", "ABREPAR", "FECHAPAR", "ABRECHAVE", "FECHACHAVE", 
                  "COMENTARIO_NAO_FECHADO", "CADEIA_NAO_FECHADA", "ERRO" ]

    grammarFileName = "Jander.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


