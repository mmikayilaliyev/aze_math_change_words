import sys
import math
"""
    Number word to word converter for the Azerbaijan language.
    Also converts currencies.
    Also do some math calculations
"""


def convert(input_str):
    """
        Returns a copy of the input string where the number words are converted to numbers.
    """

    return get_numbers(input_str)


# ********************************************************************************************
# ************************************* IMPLEMENTATION ***************************************
# ********************************************************************************************


special_cases_all_not2d_array = [
    [4, 1, 3, 4, 1, 3], [1, 4, 2, 1, 4, 2], [1, 4, 1, 1, 4, 1], [1, 4, 1, 4], [4, 1, 3, 2, 4,
                                                                               1, 3, 2], [1, 4, 2, 1, 1, 4, 2, 1], [4, 1, 3, 2, 1, 4, 1, 3, 2, 1], [1, 3, 2, 1, 3, 2],
    [1, 4, 2, 1, 1, 4, 2], [4, 1, 3, 2, 4, 1, 3], [4, 1, 3, 2, 1, 4, 1, 3, 2], [1, 4, 2, 1, 4, 2, 1], [4, 1, 3, 4, 1,
                                                                                                       3, 2], [1, 4, 1, 4, 2], [4, 4, 1], [4, 1, 3, 2, 4, 1, 3, 2, 1], [1, 3, 1, 3, 2], [4, 1, 3, 2, 2], [1, 3, 2, 2],
    [1, 1, 3], [1, 1, 4], [1, 1, 5], [1, 1, 7], [2, 2, 4], [2, 2, 5], [2, 2, 6], [2, 2, 7], [1, 2, 1, 4], [
        1, 2, 1, 5], [1, 2, 1, 6], [1, 2, 1, 7], [2, 1, 2, 4], [2, 1, 2, 5], [2, 1, 2, 6], [2, 1, 2, 7],
    [2, 1, 2, 1, 4], [2, 1, 2, 1, 5], [2, 1, 2, 1, 6], [2, 1, 2, 1, 7],
    [1, 3, 2, 1, 2, 1], [1, 3, 2, 1, 2], [1, 3, 2, 2, 1], [4, 1, 3, 1, 1], [
        4, 1, 3, 1, 2], [4, 1, 3, 2, 1, 2, 1],  [4, 1.3, 2, 1, 2],  [4, 1, 3, 2, 2, 1],
    [1, 4, 2, 2, 1], [1, 4, 1, 1], [1, 4, 1, 2], [1, 4, 2, 1, 2], [
        1, 4, 2, 1, 2, 1], [1, 4, 2, 2], [1, 4, 1, 4, 1]
]

special_cases_all = [
    [[4, 1, 3, 4, 1, 3], [1, 4, 2, 1, 4, 2], [1, 4, 1, 1, 4, 1], [1, 4, 1, 4], [4, 1, 3, 2, 4, 1, 3, 2], [
        1, 4, 2, 1, 1, 4, 2, 1], [4, 1, 3, 2, 1, 4, 1, 3, 2, 1], [1, 3, 2, 1, 3, 2]],    
   
    [[1, 4, 2, 1, 1, 4, 2], [4, 1, 3, 2, 4, 1, 3], [4, 1, 3, 2, 1, 4, 1, 3, 2]],
    [[1, 4, 2, 1, 4, 2, 1], [4, 1, 3, 4, 1, 3, 2], [1, 4, 1, 4, 2], [4, 4, 1], [4, 1, 3, 2, 4,
                                                                                1, 3, 2, 1], [1, 3, 1, 3, 2], [1, 4, 1, 4, 1]],                                # index 2
    [[1, 1, 3], [1, 1, 4], [1, 1, 5], [1, 1, 7], [2, 2, 4], [2, 2, 5], [2, 2, 6], [
        2, 2, 7]],                                                                
  
    [[1, 2, 1, 4], [1, 2, 1, 5], [1, 2, 1, 6], [1, 2, 1, 7]],
    [[2, 1, 2, 4], [2, 1, 2, 5], [2, 1, 2, 6], [2, 1, 2, 7], [2, 1, 2, 1, 4], [2, 1, 2, 1, 5], [
        2, 1, 2, 1, 6], [2, 1, 2, 1, 7]],                                  
    [[1, 3, 2, 2], [1, 3, 2, 1, 2], [4, 1, 3, 1, 1], [4, 1, 3, 1, 2], [4, 1, 3, 2, 2], [
        4, 1, 3, 2, 1, 2], [1, 4, 1, 1], [1, 4, 2, 1, 2], [1, 4, 2, 2]],                        
    [[1, 3, 2, 1, 2, 1], [1, 3, 2, 2, 1], [4, 1, 3, 2, 1, 2, 1], [4, 1, 3, 2, 2, 1], [
        1, 4, 2, 2, 1], [1, 4, 1, 2], [1, 4, 2, 1, 2, 1]]                                   
]


litnum = ['s??f??r   ', 'bir   ', 'iki    ', '????  ', 'd??rd   ',
          'be??   ', 'alt??   ', 'yeddi   ', 's??kkiz   ', 'doqquz   ']
litnum_word = ['s??f??r', 'bir', 'iki', '????', 'd??rd',
               'be??', 'alt??', 'yeddi', 's??kkiz', 'doqquz']
litnum_word_with_ten = litnum_word + ['on']


notlitnum = ['10   ', '20   ', '30   ', '40   ', '50   ', '60   ', '70   ', '80   ',
             '90   ', '100   ', '1000   ', '1000000   ', '1000000000   ', '1000000000000   ']
notlitnum_word = ['on', 'iyirmi', 'otuz', 'q??rx',
                  '??lli', 'altm????', 'yetmi??', 's??ks??n', 'doxsan', 'y??z', 'min', 'milyon', 'milyard', 'trilyon']

numsunderhundred = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                    10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 1000]
numsunderhun_tur = ['s??f??r', 'bir', 'iki', '????', 'd??rd', 'be??', 'alt??', 'yeddi', 's??kkiz', 'doqquz', 'on', 'iyirmi', 'otuz', 'q??rx',
                    '??lli', 'altm????', 'yetmi??', 's??ks??n', 'doxsan', 'y??z', 'min']

bignum = [100, 1000, 10 ** 6, 10 ** 9, 10 ** 12]
bignum_n = ['y??z', 'min', 'milyon', 'milyard', 'trilyon']

middle_forbucuk = [10, 20, 30, 40, 50, 60, 70, 80, 90]

smallnum_for_bucuk = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bignum_for_bucuk = [1000, 10**6, 10**9, 10**12]
smallnum_nfor_bucuk = ['bir', 'iki', '????', 'd??rd',
                       'be??', 'alt??', 'yeddi', 's??kkiz', 'doqquz', 'on']
bignum_nfor_bucuk = ['min', 'milyon', 'milyard', 'trilyon']

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50,
           60, 70, 80, 90, 100, 1000, 10 ** 6, 10 ** 9, 10 ** 12]
numbers_tur = ['s??f??r??nc??', 'birinci', 'ikinci', '??????nc??', 'd??rd??nc??', 'be??inci', 'alt??nc??', 'yeddinci', 's??kkizinci', 'doqquzuncu', 'onuncu', 'iyirminci',
               'otuzuncu', 'q??rx??nc??', '??llinci', 'altm??????nc??', 'yetmi??inci', 's??ks??ninci', 'doxsan??nc??', 'y??z??nc??', 'mininci', 'milyonuncu', 'milyard??nc??', 'trilyonuncu']
numbers1 = ['s??f??r', 'bir', 'iki', '????', 'd??rd', 'be??', 'alt??', 'yeddi', 's??kkiz', 'doqquz', 'on', 'iyirmi', 'otuz', 'q??rx',
            '??lli', 'altm????', 'yetmi??', 's??ks??n', 'doxsan', 'y??z', 'min', 'milyon', 'milyard', 'trilyon']
cu1 = ['birinci', 'ikinci', 'be??inci', 'yeddinci', 's??kkizinci',
       'iyirminci', '??llinci', 'yetmi??inci', 's??ks??ninci', 'mininci']
cu2 = ['alt??nc??', 'q??rx??nc??', 'altm??????nc??', 'doxsan??nc??', 'milyard??nc??']
cu3 = ['??????nc??', 'd??rd??nc??', 'y??z??nc??']
cu4 = ['doqquzuncu', 'onuncu', 'otuzuncu', 'milyonuncu', 'trilyonuncu']


numbers_row = ['bir', 'iki', '????', 'd??rd', 'be??', 'alt??', 'yeddi', 's??kkiz', 'doqquz', 'on', 'iyirmi', 'otuz', 'q??rx',
               '??lli', 'altm????', 'yetmi??', 's??ks??n', 'doxsan', 'y??z', 'min', 'milyon', 'milyard', 'trilyon']


bignum_n_reverse = bignum_n[::-1]
bignum_reverse = bignum[::-1]


symbols_in_word = [' dolar', ' euro', ' lira', ' manat', ' pound']
symbols_in_word2 = ['dolar', 'euro', 'lira', 'manat', 'pound']
symbols = ['$', '???', '???', '???', '??', '%', '.']


sing = ['s??f??r', 'bir', 'iki', '????', 'd??rd', 'be??',
        'alt??', 'yeddi', 's??kkiz', 'doqquz']  
tnth = ['on', 'iyirmi', 'otuz', 'q??rx', '??lli',
        'altm????', 'yetmi??', 's??ks??n', 'doxsan']  
yzlk = ['y??z'] 
hndr = ['min']  
mlyn = ['milyon']  
mlyrd = ['milyard']  
trlyn = ['trilyon']  

sp_case_numbers1 = ['s??f??r ', 'bir ', 'iki ', '???? ', 'd??rd ', 'be?? ', 'alt?? ', 'yeddi ', 's??kkiz ', 'doqquz ', 'on ', 'iyirmi ', 'otuz ', 'q??rx ',
                    '??lli ', 'altm???? ', 'yetmi?? ', 's??ks??n ', 'doxsan ', 'y??z ', 'min ', 'milyon ', 'milyard ', 'trilyon ']


goback = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


goback1 = [' s??f??r ', ' bir ', ' iki ', ' ???? ', ' d??rd ',
           ' be?? ', ' alt??', ' yeddi ', ' s??kkiz ', ' doqquz ']

sekilcisiz_word = litnum_word + notlitnum_word

sekilciliha_dade = [
    's??f??rda', 'bird??', 'ikid??', '????d??', 'd??rdd??', 'be??d??', 'alt??da', 'yeddid??', 's??kkizd??', 'doqquzda', 'onda',
    'iyirmid??', 'otuzda', 'q??rxda', '??llid??', 'altm????da', 'yetmi??d??', 's??ks??nd??', 'doxsanda',
    'y??zd??', 'mind??', 'milyonda', 'milyardda', 'trilyonda'
]
sekilciliha_da = [
    's??f??rda', 'alt??da', 'doqquzda', 'onda', 'otuzda', 'q??rxda',
    'altm????da', 'doxsanda', 'milyonda', 'milyardda', 'trilyonda'
]
sekilciliha_de = [
    'bird??', 'ikid??', '????d??', 'd??rdd??', 'be??d??', 'yeddid??', 's??kkizd??',
    'iyirmid??', '??llid??', 'yetmi??d??', 's??ks??nd??', 'y??zd??', 'mind??'
]
sekilciliha_i_full = [
    's??f??r??', 'biri', 'ikisi', '??????', 'd??rd??', 'be??i', 'alt??s??', 'yeddisi', 's??kkizi', 'doqquzu', 'onu',
    'iyirmisi', 'otuzu', 'q??rx??', '??llisi', 'altm??????', 'yetmi??i', 's??ks??ni', 'doxsan??', 'y??z??',
                'mini', 'milyonu', 'milyard??', 'trilyar??'
]
sekilciliha_i1 = [
    's??f??r??', 'alt??s??', 'q??rx??', 'altm??????', 'doxsan??', 'milyard??', 'trilyar??'
]

sekilciliha_i2 = [
    'biri', 'ikisi', 'be??i', 'yeddisi', 's??kkizi', 'iyirmisi', '??llisi', 'yetmi??i', 's??ks??ni', 'mini'
]
sekilciliha_i3 = [
    'doqquzu', 'onu', 'otuzu', 'milyonu'
]
sekilciliha_i4 = [
    '??????', 'd??rd??', 'y??z??'
]

sekilciliha_dan_full = ['s??f??rdan', 'bird??n', 'ikid??n', '????d??n', 'd??rdd??n', 'be??d??n', 'alt??dan', 'yeddid??n', 's??kkizd??n', 'doqquzdan', 'ondan',
                        'iyirmid??n', 'otuzdan', 'q??rxdan', '??llid??n', 'altm????dan', 'yetmi??d??n', 's??ks??nd??n', 'doxsandan', 'y??zd??n',
                        'mind??n', 'milyondan', 'milyarddan', 'trilyardan']

sekilciliha_dan = [
    's??f??rdan', 'alt??dan', 'doqquzdan', 'ondan', 'otuzdan', 'q??rxdan', 'altm????dan', 'doxsandan',
                'milyondan', 'milyarddan', 'trilyardan'
]
sekilciliha_den = [
    'bird??n', 'ikid??n', '????d??n', 'd??rdd??n', 'be??d??n', 'yeddid??n', 's??kkizd??n',
    'iyirmid??n', '??llid??n', 'yetmi??d??n', 's??ks??nd??n', 'y??zd??n',
    'mind??n'
]

sekilciliha_dir_full = ['s??f??rd??r', 'birdir', 'ikidir', '????d??r', 'd??rtd??r', 'be??dir', 'alt??d??r', 'yeddidir', 's??kkizdir', 'doqquzdur', 'ondur',
                        'iyirmidir', 'otuzdur', 'q??rxd??r', '??llidir', 'altm????d??r', 'yetmi??dir', 's??ks??ndir', 'doxsand??r', 'y??zd??r',
                        'mindir', 'milyondur', 'milyardd??r', 'trilyard??r']

sekilciliha_dir1 = [
    'birdir', 'ikidir', 'be??dir', 'yeddidir', 's??kkizdir', 'iyirmidir', '??llidir', 'yetmi??dir', 's??ks??ndir', 'mindir'
]

sekilciliha_dir2 = [
    's??f??rd??r', 'alt??d??r', 'q??rxd??r', 'altm????d??r', 'doxsand??r', 'milyardd??r', 'trilyard??r'
]

sekilciliha_dir3 = [
    'doqquzdur', 'ondur', 'otuzdur', 'milyondur'
]

sekilciliha_dir4 = [
    '????d??r', 'd??rtd??r', 'y??zd??r'
]

sekilciliha_inci_dir_full = ['s??f??r??nc??d??r', 'birincidir', 'ikincidir', '??????nc??d??r', 'd??rd??nc??d??r', 'be??incidir', 'alt??nc??d??r', 'yeddincidir', 's??kkizincidir', 'doqquzuncudur', 'onuncudur',
                             'iyirmincidir', 'otuzuncudur', 'q??rx??nc??d??r', '??llincidir', 'altm??????nc??d??r', 'yetmi??incidir', 's??ks??nincidir', 'doxsan??nc??d??r', 'y??z??nc??d??r',
                             'minincidir', 'milyonuncudur', 'milyard??nc??d??r', 'trilyar??nc??d??r']

sekilciliha_inci_dir1 = [
    'birincidir', 'ikincidir', 'be??incidir', 'yeddincidir', 's??kkizincidir', 'iyirmincidir', '??llincidir', 'yetmi??dir', 's??ks??ndir', 'mindir'
]

sekilciliha_inci_dir2 = [
    's??f??r??nc??d??r', 'alt??nc??d??r', 'q??rx??nc??d??r', 'altm??????nc??d??r', 'doxsan??nc??d??r', 'milyard??nc??d??r', 'trilyar??nc??d??r'
]

sekilciliha_inci_dir3 = [
    'doqquzuncudur', 'onuncudur', 'otuzuncudur', 'milyonuncudur'
]

sekilciliha_inci_dir4 = [
    '??????nc??d??r', 'd??rd??nc??d??r', 'y??z??nc??d??r'
]

sekilciliha_lardal??rd?? = [
    's??f??rlarda', 'ikil??rd??', '????l??rd??', 'd??rdl??rd??', 'be??l??rd??', 'alt??lar', 'yeddil??r', 's??kkizl??r', 'doqquzlar',
    'onlarda', 'iyirmil??rd??', 'otuzlarda', 'q??rxlarda', '??llil??rd??', 'altm????larda',
    'yetmi??l??rd??', 's??ks??nl??rd??', 'doxsanlarda', 'minl??rd??', 'y??zl??rd??', 'milyonlarda', 'milyardda', 'trilyarda'
]


sekilciliha_larda = [
    's??f??rlarda', 'alt??lar', 'doqquzlar', 'onlarda', 'otuzlarda', 'q??rxlarda', 'altm????larda',
    'doxsanlarda', 'milyonlarda', 'milyardda', 'trilyarda'
]

sekilciliha_l??rd?? = [
    'ikil??rd??', '????l??rd??', 'd??rdl??rd??', 'be??l??rd??', 'yeddil??r', 's??kkizl??r',
    'iyirmil??rd??', '??llil??rd??', 'yetmi??l??rd??', 's??ks??nl??rd??', 'minl??rd??', 'y??zl??rd??'
]

sekilciliha_ae_full = [
    's??f??ra', 'bir??', 'ikiye', '????e', 'd??rde', 'be??e', 'alt??ya', 'yeddiye', 's??kkize', 'doqquza', 'ona',
    'iyirmiye', 'otuza', 'q??rxa', '??lliye', 'altm????a', 'yetmi??e', 's??ks??ne', 'doxsana',
    'y??ze', 'mine', 'milyona', 'milyarda', 'trilyona'
]

sekiliciliha_a = [
    's??f??ra', 'alt??ya', 'doqquza', 'ona', 'otuza', 'q??rxa', 'altm????a', 'doxsana',
    'milyona', 'milyarda', 'trilyona'
]

sekilciliha_e = [
    'bir??', 'ikiye', '????e', 'd??rde', 'be??e', 'yeddiye', 's??kkize',
    'iyirmiye', '??lliye', 'yetmi??e', 's??ks??ne', 'y??ze', 'mine'
]

sekilciliha_li_full = [
    's??f??rl??', 'birli', 'ikili', '????l??', 'd??rtl??', 'be??li', 'alt??l??', 'yeddili', 's??kkizli', 'doqquzlu', 'onlu',
    'iyirmili', 'otuzlu', 'q??rxl??', '??llili', 'altm????l??', 'yetmi??li', 's??ks??nli', 'doxsanl??', 'y??zl??',
    'minli', 'milyonlu', 'milyardl??', 'trilyarl??'
]

sekilcili_li_1 = [
    's??f??rl??', 'alt??l??', 'q??rxl??', 'altm????l??', 'doxsanl??', 'milyardl??', 'trilyarl??'
]

sekilcili_li_2 = [
    'birli', 'ikili', 'be??li', 'yeddili', 's??kkizli', 'iyirmili', '??llili', 'yetmi??li', 's??ks??nli', 'minli'
]

sekilcili_li_3 = [
    '????l??', 'd??rtl??', 'y??zl??',
]

sekilcili_li_4 = [
    'doqquzlu', 'onlu', 'otuzlu', 'milyonlu'
]

sekilciliha_in_full = [
    's??f??r??n', 'birin', 'ikinin', '??????n', 'd??rd??n', 'be??in', 'alt??n??n', 'yeddinin', 's??kkizin', 'doqquzun', 'onun',
    'iyirminin', 'otuzun', 'q??rx??n', '??llinin', 'altm??????n', 'yetmi??in', 's??ks??nin', 'doxsan??n', 'y??z??n',
    'minin', 'milyonun', 'milyard??n', 'trilyar??n'
]

sekilciliha_in1 = [
    's??f??r??n', 'alt??n??n', 'q??rx??n', 'altm??????n', 'doxsan??n', 'milyard??n', 'trilyar??n'
]

sekilciliha_in2 = [
    'birin', 'ikinin', 'be??in', 'yeddinin', 's??kkizin', 'iyirminin', '??llinin', 'yetmi??in', 's??ks??nin', 'minin'
]

sekilciliha_in3 = [
    'doqquzun', 'onun', 'otuzun', 'milyonun'
]


sekilciliha_in4 = [
    '??????n', 'd??rd??n', 'y??z??n',
]

sekilciliha_larin_full = [
    's??f??rlar??n', 'birl??rin', 'ikil??rnin', '????l??rin', 'd??rtl??rin', 'be??l??rin', 'alt??lar??n', 'yeddil??rin', 's??kkizl??rin', 'doqquzlar??n', 'onlar??n',
    'iyirmil??rin', 'otuzlar??n', 'q??rxlar??n', '??llil??rin', 'altm????lar??n', 'yetmi??l??rin', 's??ks??nl??rin', 'doxsanlar??n', 'y??zl??rin',
    'minl??rin', 'milyonlar??n', 'milyardlar??n', 'trilyarlar??n'
]

sekilciliha_larin1 = [
    's??f??rlar??n', 'alt??lar??n', 'doqquzlar??n', 'onlar??n', 'otuzlar??n', 'q??rxlar??n', 'altm????lar??n', 'doxsanlar??n', 'milyonlar??n', 'milyardlar??n', 'trilyarlar??n'
]

sekilciliha_larin2 = [
    'birl??rin', 'ikil??rnin', '????l??rin', 'd??rtl??rin', 'be??l??rin', 'yeddil??rin', 's??kkizl??rin', 'iyirmil??rin', '??llil??rin', 'yetmi??l??rin', 's??ks??nl??rin', 'y??zl??rin',
    'minl??rin'
]

sekilciliha_larl??r_full = [
    's??f??rlar', 'birl??r', 'ikil??r', '????l??r', 'd??rtl??r', 'be??l??r', 'alt??lar', 'yeddil??r', 's??kkizl??r', 'doqquzlar', 'onlar',
    'iyirmil??r', 'otuzlar', 'q??rxlar', '??llil??r', 'altm????lar', 'yetmi??l??r', 's??ks??nl??r', 'doxsanlar', 'y??zl??r',
    'minl??r', 'milyonlar', 'milyardlar', 'trilyarlar'
]

sekilciliha_lar1 = [
    's??f??rlar', 'alt??lar', 'doqquzlar', 'onlar',
    'otuzlar', 'q??rxlar', 'altm????lar', 'doxsanlar',
    'milyonlar', 'milyardlar', 'trilyarlar'
]

sekilciliha_lar2 = [
    'birl??r', 'ikil??r', '????l??r', 'd??rtl??r', 'be??l??r', 'yeddil??r', 's??kkizl??r', 'iyirmil??r', '??llil??r', 'yetmi??l??r', 's??ks??nl??r', 'y??zl??r', 'minl??r'
]

sekilcili_hal = sekilciliha_dade + sekilciliha_i_full + sekilciliha_dan_full + \
    sekilciliha_dir_full + sekilciliha_inci_dir_full + sekilciliha_lardal??rd?? + \
    sekilciliha_ae_full + sekilciliha_li_full + sekilciliha_in_full + sekilciliha_larin_full + \
    sekilciliha_larl??r_full

tamliq = ['onda', 'y??zd??', 'mind??', 'milyonda', 'trilyonda']
tamliq_numbers = [10, 100, 1000, 10**6, 10**9]

math_commands = [
    '??st??g??l', 'vur', 'topla', '????x', 'b??l', 'b??l??ns??n', '??st??', 't??r??m??si', 'inteqral', 'faizi', 'sinius', 'kosnus', 'tanqes', 'kotanqes', 'faktorial',
    'arksinius', 'arkkotanqes', 'arktanqes', 'arkkotanqes', 'kambinzon', 'kvadrat??', 'kubu', 'k??kalt??', 'loqarifma', 'permutasiya', 'aranjiman',
    'pi', 'radian', 'd??r??c??' 
]

loq_h = ['e' , '??sasdan']

all_turrk = numsunderhun_tur + ['milyon', 'milyard', 'trilyon'] + numbers_tur + symbols_in_word2 + ['faiz'] + [
    'tam', 'n??qt??'] + tamliq + sekilcili_hal + ['kuru??', 'cent', 'penny'] + math_commands + loq_h

all_num_natural = numsunderhun_tur + bignum_n




testdic = {'??st??g??l': '+' ,'topla':'+','c??ml??':'+','????x':'-','vur':'*','b??l':'/','??st??':'**'}

def calculate(str1):
    """
        doing calc from words to number by its floor place

        fun(main_calc):
        actually main_calc do calculation and get answer for the fun(calculation)

        variables:
        sum- its sum of calculation
        str1 - the sring which will be given for calculation
    """

    def main_calc(n=str1):
        """
            TODO
        """

        if n == 'y??z':
            pass
        elif len(n) == 1:
            return (numsunderhundred[numsunderhun_tur.index(n[0])])
        elif (n in numsunderhun_tur) or (n in bignum_n):
            for i in numsunderhun_tur:
                if n == i:
                    return numsunderhundred[numsunderhun_tur.index(i)]
            for i in bignum_n:
                if n == i:
                    return bignum[bignum_n.index(i)]
        else:
            if (bignum_n[0] == n[1]) and len(n) == 4:
                return (100 * (numsunderhundred[numsunderhun_tur.index(n[0])]) + (numsunderhundred[numsunderhun_tur.index(n[2])]) + numsunderhundred[numsunderhun_tur.index(n[3])])
            elif (bignum_n[0] == n[1]) and len(n) == 3:
                return (100 * (numsunderhundred[numsunderhun_tur.index(n[0])]) + (numsunderhundred[numsunderhun_tur.index(n[2])]))
            elif (bignum_n[0] == n[1]) and len(n) == 2:
                return (100 * (numsunderhundred[numsunderhun_tur.index(n[0])]))
            elif (bignum_n[0] == n[0]) and len(n) == 3:
                return (100 + (numsunderhundred[numsunderhun_tur.index(n[1])]) + (numsunderhundred[numsunderhun_tur.index(n[2])]))
            elif (bignum_n[0] == n[0]) and len(n) == 2:
                return (100 + (numsunderhundred[numsunderhun_tur.index(n[1])]))
            elif (bignum_n[0] not in n) and len(n) == 2:
                return ((numsunderhundred[numsunderhun_tur.index(n[1])]) + (numsunderhundred[numsunderhun_tur.index(n[0])]))

    if str1 != []:
        return main_calc(n=str1)
    else:
        return 1


def check(k):
    """
        checks if the number belongs to which classification
        makes string a list
        checking number and do calculation
    """

    k1 = k.split(' ')
    for i in numbers_tur:
        if k1[-1] == i:
            k1[-1] = numbers_row[numbers_tur.index(i)]
            return str(my_sum(k1))+'-{}'.format(k[-2:])
    return my_sum(k1)


def my_sum(k1):
    """
        summing result from fun(calculate) and get a string
        num - the result of calculation 
    """

    num = 0
    for i in bignum_n_reverse:
        if i in k1:
            word = k1[:k1.index(i)]
            num = num + calculate(word) * \
                bignum_reverse[bignum_n_reverse.index(i)]
            k1 = k1[k1.index(i)+1:]
            if k1 == [] and word == []:
                return num
    if k1 == []:
        return num
    num = num + calculate(k1)
    return num


def symbolic(i, k):
    """
        this function seperates symbols from words then brings them together
        k1 - not symbolic side
    """

    k1 = k.split(i)[0]
    res = check(k1)
    return str(res) + symbols[symbols_in_word.index(i)]


def result(k):
    """
        Checks if the number is directly equal to one of the floor numbers or not,
        then takes number from calculation and gives an answer.
    """

    for i in numsunderhun_tur:
        if i == k:
            return numsunderhundred[numsunderhun_tur.index(i)]
    for i in bignum_n:
        if i == k:
            return bignum[bignum_n.index(i)]
    for i in numbers_tur:
        if i == k:
            return Decider(k[0])
    for i in symbols_in_word:
        if i in k:
            return symbolic(i, k)
    return check(k)


def function1(newlist_classifier, num_list):
    """
         This function searchs the correct way of calculation depending on situation
    """
    if (len(newlist_classifier) == 3) and ((newlist_classifier[0] == newlist_classifier[2]) and (newlist_classifier[1] < newlist_classifier[0]) or (newlist_classifier == [1, 2, 1])):
        return str(result(num_list[0])) + ' ' + str(result(' '.join(num_list[1:])))
    elif (len(newlist_classifier) == 4) and ((newlist_classifier[1] == newlist_classifier[-1]) and ((newlist_classifier[0] == newlist_classifier[2]) or (newlist_classifier[0] + 1 == newlist_classifier[2]))):
        return str(result(' '.join(num_list[:2]))) + ' ' + str(result(' '.join(num_list[2:])))
    elif (len(newlist_classifier) == 5) and (newlist_classifier[0] == 3 and newlist_classifier[3] == 3 and newlist_classifier[2] == 1) and (newlist_classifier[0] == newlist_classifier[-1]):
        return str(result(' '.join(num_list[:2]))) + ' ' + str(result(' '.join(num_list[2:])))
    elif (len(newlist_classifier) == 6) and ((newlist_classifier[2] == newlist_classifier[5]) and (newlist_classifier[1] == newlist_classifier[4]) and (newlist_classifier[0] == newlist_classifier[3])):
        return str(result(' '.join(num_list[:3]))) + ' ' + str(result(' '.join(num_list[3:])))

    frst_el = newlist_classifier[0]
    maks_el = max(newlist_classifier)
    if ((maks_el > 3) and newlist_classifier.count(maks_el) == 1):
        maks_el_index = newlist_classifier.index(maks_el)
        if (0 < len(newlist_classifier[:maks_el_index]) < 5 and max(newlist_classifier[:maks_el_index]) < 4) or newlist_classifier[-1] == maks_el:
            return str(result(' '.join(num_list)))
    if (newlist_classifier.count(maks_el) > 1 and maks_el > 3):
        mid_section = newlist_classifier[newlist_classifier.index(
            maks_el)+1:newlist_classifier.index(maks_el, 2)]
        max_mid_section = max(mid_section)
        if max_mid_section < 3 and (1 < len(mid_section) < 5):
            reverse = mid_section.index(1, 1)
            l1 = len(mid_section)-reverse
            return str(result(' '.join(num_list[:newlist_classifier.index(maks_el)+1+l1]))) + ' ' + str(result(' '.join(num_list[newlist_classifier.index(maks_el)+1+l1:])))
        return str(result(' '.join(num_list[:newlist_classifier.index(maks_el)+1]))) + str(result(' '.join(num_list[newlist_classifier.index(maks_el)+1:])))

    if maks_el >= 3:
        if (frst_el == 1 and (newlist_classifier[1] == 1)) or (frst_el == 1 and (newlist_classifier[1] == 2)):
            pass
        else:
            for i in newlist_classifier:
                if i > frst_el:
                    frst_el = i
                    break
                else:
                    continue

        curr = newlist_classifier[0]
        temp = []
        res = []

        for ele in newlist_classifier:
            if ele >= curr or ele == temp[-1]:
                res.append(temp)
                curr = ele
                temp = []
            temp.append(ele)
        res.append(temp)

        res = res[1:]
        len1 = []
        res_0 = res[0]
        res_00 = res[0][0]

        if len(res) > 1:
            if len(res[0]) == 1:
                if (res[0][0] == 1 or res[0][0] == 2) and res[1][0] > res[0][0]:
                    res = res[1:]
                    res[0].insert(0, res_00)
            elif len(res[0]) != 1:
                pass

        if len(res) == 1:
            answer = str(result(' '.join(num_list)))
            return answer

        if max(res[1]) <= 5 and (max(res[0]) < max(res[1])):
            res = res[0] + res[1]

        if len(res) == len(num_list):
            answer = str(result(' '.join(num_list)))
            return answer
        else:
            pass

        for i in res:
            len1.append(len(i))

        if len(len1) == 1:
            answer = str(result(' '.join(num_list)))
            return answer

        sen = []
        leni = len1
        x = 0
        y = leni[0]
        for i in range(0, len(leni), 1):
            if i == (len(leni) - 1):
                sen.append(result(' '.join(num_list[x:])))
                break
            sen.append(result(' '.join(num_list[x: y])))
            x = x + leni[i]
            y = y + leni[i]
        sentence = ' '.join(([str(i) for i in sen]))
        return sentence
    elif maks_el < 3:

        for i in newlist_classifier:
            if i > frst_el:
                frst_el = i
                break
            else:
                continue

        curr = newlist_classifier[0]
        temp = []
        res = []

        for ele in newlist_classifier:
            if ele >= curr or ele == temp[-1]:
                res.append(temp)
                curr = ele
                temp = []
            temp.append(ele)

        res.append(temp)

        res = res[1:]
        len1 = []
        res_0 = res[0]
        res_00 = res[0][0]

        if len(res) > 2:
            if res[0] == [1] and (res[1] == [2, 1] or res[1] == [2]):
                pass
            elif len(res[0]) == 1:
                if (res[0][0] == 1 or res[0][0] == 2) and res[1][0] > res[0][0]:
                    res = res[1:]
                    res[0].insert(0, res_00)
            elif len(res[0]) != 1:
                res = res[1:]
                res[0] = res_0 + res[0]
        elif len(res) == 1:
            pass

        for i in res:
            len1.append(len(i))

        if len(len1) == 1:
            answer = str(result(' '.join(num_list)))
            return answer

        sen = []
        leni = len1
        x = 0
        y = leni[0]
        for i in range(0, len(leni), 1):
            if i == (len(leni)-1):
                sen.append(result(' '.join(num_list[x:])))
                break
            sen.append(result(' '.join(num_list[x:y])))
            x = x + leni[i]
            y = y + leni[i]
        sentence = ' '.join(([str(i) for i in sen]))
        return sentence


def function2(newlist_classifier, num_list):
    """
        This function is helping seperate word 'y??zd??' from list then calculate list using function1 and 
        at the end adding % sign
    """
    if (-1) == newlist_classifier[0]:
        ans = function1(newlist_classifier[1:], num_list[1:])
        if len(ans.split(' ')) == 1:
            return ans + '%'
        else:
            ans = ans.split(' ')
            ans.insert(1, '%')
            ans = ' '.join(ans)
            return ans
    else:
        minus_ind = newlist_classifier.index(-1)
        frstprt = num_list[:minus_ind]
        scndprt = num_list[minus_ind+1:]
        return function1(newlist_classifier=newlist_classifier[:minus_ind], num_list=frstprt) + ' ' + function1(newlist_classifier=newlist_classifier[minus_ind+1:], num_list=scndprt) + "%"


def FunctionNormal(num_list):
    """
        If there is no 'y??zd??' , 'n??qt??' , 'bu??uk'  words in the list this function works
        First it checks is this same words for ex " ???? ???? " , "min dokkuz y??z min doqquz y??z" or "on iki on iki on iki"
        Then creating newlist chechks is there currencies 
        and calls function1 for calculation if cant find the possibile variants
    """
    if (len(num_list) % 2 == 0) and (num_list[:(len(num_list)//2)] == num_list[(len(num_list)//2):]):
        ans = str(result(' '.join(num_list[:len(num_list)//2])))
        return ans + '-' + ans
    if (len(num_list) % 3 == 0) and (num_list[:len(num_list)//3] == (num_list[len(num_list)//3:2*len(num_list)//3])) and (num_list[len(num_list)//3:2*len(num_list)//3]) == (num_list[2*len(num_list)//3:3*len(num_list)//3]):
        ans = str(result(' '.join(num_list[:len(num_list)//3])))
        return ans + ' ' + ans + ' ' + ans
    if len(set(num_list)) == 1:
        return (num_list[0]+' ')*len(num_list)
    newlist_classifier = []
    for i in range(0, len(num_list), 1):
        if num_list[i] in sing:
            newlist_classifier.append(1)
        elif num_list[i] in tnth:
            newlist_classifier.append(2)
        elif num_list[i] in yzlk:
            newlist_classifier.append(3)
        elif num_list[i] in hndr:
            newlist_classifier.append(4)
        elif num_list[i] in mlyn:
            newlist_classifier.append(5)
        elif num_list[i] in mlyrd:
            newlist_classifier.append(6)
        elif num_list[i] in trlyn:
            newlist_classifier.append(7)
        elif num_list[i] in symbols_in_word2:
            newlist_classifier.append(0)
        elif num_list[i] == 'kuru??' or num_list[i] == 'cent' or num_list[i] == 'penny' or num_list[i] == 'kepik':
            newlist_classifier.append('w')

    if (newlist_classifier[-1] == 0 and len(num_list) == 1) or (newlist_classifier[-1] == 'w' and len(num_list) == 1):
        return num_list[0]

    if ('w' in newlist_classifier and 0 in newlist_classifier) or ('w' in newlist_classifier) or (0 in newlist_classifier):
        return FunctionForMoney(num_list, newlist_classifier)

    if (0 not in newlist_classifier) and ('w' not in newlist_classifier):
        if newlist_classifier in special_cases_all_not2d_array:
            for i in special_cases_all:
                if newlist_classifier in i:
                    way = special_cases_all.index(i)
                    break
            if way == 0:
                return FunctionNormal(num_list[:(len(newlist_classifier)//2)]) + '-' + FunctionNormal(num_list[(len(newlist_classifier)//2):])
            if way == 1:
                return FunctionNormal(num_list[:(len(newlist_classifier)//2)+1]) + '-' + FunctionNormal(num_list[(len(newlist_classifier)//2)+1:])
            if way == 2:
                return FunctionNormal(num_list[:(len(newlist_classifier)//2)]) + '-' + FunctionNormal(num_list[(len(newlist_classifier)//2):])
            if way == 3:
                if num_list[0] in all_num_natural:
                    return str(numbers[all_num_natural.index(num_list[0])]) + '-' + FunctionNormal(num_list[1:])
            if way == 4:
                return str(numbers[all_num_natural.index(num_list[0])]) + '-' + FunctionNormal(num_list[1:])
            if way == 5:
                return FunctionNormal((num_list[:2]+num_list[-1:])) + '-' + FunctionNormal(num_list[2:])
            if way == 6:
                return FunctionNormal(num_list[:len(newlist_classifier)-1]) + '-0' + str(numbers[all_num_natural.index(num_list[-1])])
            if way == 7:
                return FunctionNormal(num_list[:len(newlist_classifier)-2]) + '-' + FunctionNormal(num_list[len(newlist_classifier)-2:])

    if len(set(newlist_classifier)) == 1:
        if newlist_classifier[0] == 2:
            newlist2 = []
            for i in num_list:
                newlist2.append(str(result(i)))
            sent = ' '.join(newlist2)
            return sent
        elif newlist_classifier[0] == 1:
            newlist2 = []
            for i in num_list:
                newlist2.append(str(i))
            sent = ' '.join(newlist2)
            return sent
    else:
        text = ' '.join(num_list)
        answer = str(function1(newlist_classifier, text.split(' ')))
        return answer


def FunctionForMoney(num_list, newlist_classifier):
    def WhichCoin(k):
        if k == 'cent':
            return '$'
        if k == 'kuru??':
            return '???'
        if k == 'kepik':
            return '???'
        if k == "penny":
            return '??'
    # on iki lira on bes kurus
    if newlist_classifier.count('w') == 1 and newlist_classifier.count(0) == 1:
        if ('w' in newlist_classifier) and (0 in newlist_classifier):
            if newlist_classifier.index('w') > newlist_classifier.index(0):
                bigmoney = (FunctionNormal(
                    num_list[:newlist_classifier.index(0)]))
                if bigmoney in sp_case_numbers1:
                    bigmoney = (FunctionNormal(
                        num_list[:newlist_classifier.index(0)]))[:-1]
                if (bigmoney in all_num_natural):
                    bigmoney = str(numbers[all_num_natural.index(bigmoney)])
                litmoney = FunctionNormal(
                    num_list[newlist_classifier.index(0) + 1:newlist_classifier.index('w')])
                if litmoney in sp_case_numbers1:
                    litmoney = FunctionNormal(num_list[newlist_classifier.index(
                        0) + 1:newlist_classifier.index('w')])[:-1]
                if (litmoney in all_num_natural):
                    litmoney = str(numbers[all_num_natural.index(litmoney)])
                symbol = (symbols[symbols_in_word2.index(
                    num_list[newlist_classifier.index(0)])])
                return bigmoney + '.' + litmoney + symbol

    # on iki lira
    if newlist_classifier.count(0) == 1 and newlist_classifier.count('w') == 0 and len(newlist_classifier) > 1:
        if num_list[-1] in symbols_in_word2:
            ans1 = FunctionNormal(num_list[:-1])
            if ans1 in sp_case_numbers1:
                ans1 = str(numbers[all_num_natural.index(num_list[0])])
                return ans1 + (symbols[symbols_in_word2.index(num_list[newlist_classifier.index(0)])])
            return ans1 + (symbols[symbols_in_word2.index(num_list[newlist_classifier.index(0)])])
        elif num_list[0] in symbols_in_word2:
            return str(symbols[symbols_in_word2.index(num_list[newlist_classifier.index(0)])]) + ' ' + FunctionNormal(num_list[1:])
        else:
            money_index = newlist_classifier[0]
            return FunctionNormal(num_list[:money_index]) + str(symbols[symbols_in_word2.index(num_list[newlist_classifier.index(0)])]) + ' ' + FunctionNormal(num_list[money_index+1:])

    # on iki kurus
    if newlist_classifier.count('w') == 1 and newlist_classifier.count(0) == 0 and len(newlist_classifier) > 1:

        if num_list[-1] in ['kuru??', 'cent']:
            ans1 = FunctionNormal(num_list[:-1])
            if ans1 in sp_case_numbers1:
                ans1 = str(numbers[all_num_natural.index(num_list[0])])
                return '0.' + ans1 + WhichCoin(num_list[-1])
            return '0.' + ans1 + WhichCoin(num_list[-1])

        elif num_list[0] in ['kuru??', 'cent']:
            return num_list[0] + ' ' + FunctionNormal(num_list[1:])
        else:
            coin_index = newlist_classifier.index('w')
            ans1 = FunctionNormal(num_list[:coin_index])
            if ans1 in sp_case_numbers1:
                ans1 = str(numbers[all_num_natural.index(num_list[0])])
                if int(ans1) < 10:
                    return '0.0' + ans1 + WhichCoin(num_list[coin_index]) + ' ' + FunctionNormal(num_list[coin_index+1:])
            return '0.' + ans1 + WhichCoin(num_list[coin_index]) + ' ' + FunctionNormal(num_list[coin_index+1:])
    # on uc lira on iki lira
    if newlist_classifier.count(0) >= 2 and newlist_classifier.count('w') == 0:
        frstmoney_index = newlist_classifier.index(0)
        frst_part = FunctionForMoney(
            num_list[:frstmoney_index+1], newlist_classifier[:frstmoney_index+1])
        scnd_part = FunctionForMoney(
            num_list[frstmoney_index+1:], newlist_classifier[frstmoney_index+1:])
        return frst_part + ' ' + scnd_part
    # on iki lira ??lli kurus on uc lira
    if newlist_classifier.count(0) == 2 and newlist_classifier.count('w') == 1:
        if newlist_classifier.index(0) < newlist_classifier.index('w') and newlist_classifier[-1] == 0:
            return FunctionForMoney(num_list[: newlist_classifier.index('w') + 1], newlist_classifier[:newlist_classifier.index('w')+1]) + ' ' + FunctionForMoney(num_list[newlist_classifier.index('w') + 1:], newlist_classifier[newlist_classifier.index('w')+1:])
    # ??lli kurus altmis kurus
    if newlist_classifier.count('w') >= 2 and newlist_classifier.count(0) == 0:
        frstcoin_index = newlist_classifier.index('w')
        frst_part = FunctionForMoney(
            num_list[:frstcoin_index+1], newlist_classifier[:frstcoin_index+1])
        scnd_part = FunctionForMoney(
            num_list[frstcoin_index+1:], newlist_classifier[frstcoin_index+1:])
        return frst_part + ' ' + scnd_part


def Numberization(lizt):
    if len(lizt) == 1:
        if lizt[0] in litnum_word_with_ten:
            return litnum_word_with_ten.index(lizt[0])
        elif lizt[0] in bignum_n:
            return bignum[bignum_n.index(lizt[0])]
        elif lizt[0] in numsunderhun_tur:
            return numsunderhundred[numsunderhun_tur.index(lizt[0])]
    else:
        return float(Decider(lizt))


def FunctionForDrops(num_list):
    """
        after creating newlist_classifier we seperate list where is n??qt?? word
        and calculate them then bring them together
        for example
        "on iki n??qt?? on be??"
        first it calculates "on iki" then "on be??"  and later we connect them with "." sign
    """
    newlist_classifier = []
    for i in range(len(num_list)):
        if num_list[i] in sing:
            newlist_classifier.append(1)
        elif num_list[i] in tnth:
            newlist_classifier.append(2)
        elif num_list[i] in yzlk:
            newlist_classifier.append(3)
        elif num_list[i] in hndr:
            newlist_classifier.append(4)
        elif num_list[i] in mlyn:
            newlist_classifier.append(5)
        elif num_list[i] in mlyrd:
            newlist_classifier.append(6)
        elif num_list[i] in trlyn:
            newlist_classifier.append(7)
        elif num_list[i] in symbols_in_word:
            newlist_classifier.append(0)
        elif num_list[i] == 'n??qt??':
            newlist_classifier.append('w')

    first_words_main = newlist_classifier[:newlist_classifier.index('w')]
    firs_words_numlist = num_list[:newlist_classifier.index('w')]
    second_words_main = newlist_classifier[newlist_classifier.index('w') + 1:]
    second_words_numlist = num_list[newlist_classifier.index('w') + 1:]
    first_place = function1(first_words_main, firs_words_numlist)
    second_place = function1(second_words_main, second_words_numlist)
    connected = first_place + '.' + second_place
    return connected


def FunctionForTamliq(num_list):

    index_tam = num_list.index('tam')
    for i in tamliq:
        if i in num_list:
            in_which_tam = num_list.index(i)
            tam_num = i
            break
    if in_which_tam-index_tam == 1:
        """ be?? tam onda s??kkiz"""
        frst_part = num_list[:index_tam]
        scnd_part = num_list[index_tam+2:]
        number_t = tamliq_numbers[tamliq.index(tam_num)]
        ans1 = Numberization(frst_part)
        ans2 = Numberization(scnd_part)
        return str(ans1 + ans2/number_t)

    elif in_which_tam - index_tam == 2:
        frst_part = num_list[:index_tam]
        scnd_part = num_list[in_which_tam+1:]
        number_tams_e = num_list[index_tam+1]
        if number_tams_e == 'on':
            number_t = (tamliq_numbers[tamliq.index(tam_num)])*10
        elif number_tams_e == 'y??z':
            number_t = (tamliq_numbers[tamliq.index(tam_num)])*100
        ans1 = Numberization(frst_part)
        ans2 = Numberization(scnd_part)
        return str(ans1 + ans2/number_t)


def FunctionForFaizAndTamliq(num_list):
    if num_list.count('faiz') == 1 and num_list.count('tam') == 1:
        if 'faiz' == num_list[-1]:
            return FunctionForTamliq(num_list[:num_list.index('faiz')]) + '%'
        else:
            frst_part = num_list[:num_list.index('faiz')+1]
            scnd_part = num_list[num_list.index('faiz')+1:]
            return FunctionForFaiz(frst_part) + FunctionForTamliq(scnd_part)


def FunctionForFaiz(num_list):
    if num_list.count('faiz') == 1:
        if 'faiz' == num_list[-1]:
            if len(num_list) == 2:
                fff = litnum_word_with_ten.index(num_list[0])
                return str(fff) + '% '
            return Decider(num_list[:-1]) + '% '
        else:
            faiz_index = num_list.index('faiz')
            frst_part = num_list[:faiz_index]
            scnd_part = num_list[faiz_index+1:]
            if len(frst_part) == 1 and len(scnd_part) == 1:
                return str(litnum_word.index(frst_part[0])) + '% ' + str(litnum_word.index(scnd_part[0]))
            if len(frst_part) == 1:
                fff = litnum_word.index(frst_part[0])
                return str(fff)+'% ' + Decider(scnd_part)
            if len(scnd_part) == 1:
                sss = litnum_word.index(scnd_part[0])
                return Decider(frst_part)+'% ' + str(sss)

        return Decider(frst_part) + '%' + Decider(scnd_part)


def DoMathOperations(num_list):
    operations = ['+','-','*','/','**']
    k = 0
    for i in num_list:
        if i in math_commands:
            k = k + 1

    res = [testdic.get(e, e) for e in num_list]

    kop = []
    big_kop = []

    for i in res:
        if i not in operations:
            kop.append(i)
        else:
            big_kop.append(kop)
            kop = []
            big_kop.append(i)
    big_kop.append(kop)

    res = [] 
    for i in big_kop:
        if type(i) == list:
            if 'sinius' in i:
                res.append(str(math.sin(Numberization(i[1:]))))
            elif  'kosinus' in i:
                res.append(str(math.cos(Numberization(i[1:]))))
            elif 'faktorial' in i:
                res.append(str(math.factorial(int(Numberization(i[:-1])))))
            else:
                res.append(str(Numberization(i)))
        else:
            res.append(str(i))

    rrr = ' '.join(res)

    return str(eval(rrr))



def FunctionExtra(num_list):
    def fctionExtra(num_list):
        main_num = num_list[-1]
        if main_num in cu1:
            return '-ci'
        elif main_num in cu2:
            return '-c??'
        elif main_num in cu3:
            return '-c??'
        elif main_num in cu4:
            return '-cu'

    if len(num_list) == 1:
        one = str(numbers[numbers_tur.index(num_list[-1])])
        return one+str(fctionExtra(num_list))
    else:
        kop = ' '.join(num_list)
        kop = kop.replace(
            num_list[-1], numbers1[numbers_tur.index(num_list[-1])])
        ans = FunctionNormal(kop.split(' '))
        return str(ans) + (fctionExtra(num_list))


def FunctionForI(num_list):
    def fctionChecksi4(num_list):
        if num_list[-1] in sekilciliha_i1:
            return '-??'
        elif num_list[-1] in sekilciliha_i2:
            return '-i'
        elif num_list[-1] in sekilciliha_i3:
            return '-u'
        elif num_list[-1] in sekilciliha_i4:
            return '-??'
    ans1 = str(fctionChecksi4(num_list))
    if len(num_list) == 1:
        return str(numbers[sekilciliha_i_full.index(num_list[0])]) + fctionChecksi4(num_list)
    if num_list[-1] in sekilciliha_i_full:
        num_list[-1] = (sekilcisiz_word[sekilciliha_i_full.index(num_list[-1])])
        return Decider(num_list) + ans1


def FunctionForDir(num_list):
    def fctionChecksDir(num_list):
        if num_list[-1] in sekilciliha_dir1:
            return '-dir'
        elif num_list[-1] in sekilciliha_dir2:
            return '-d??r'
        elif num_list[-1] in sekilciliha_dir3:
            return '-dur'
        elif num_list[-1] in sekilciliha_dir4:
            return '-d??r'
    ans1 = str(fctionChecksDir(num_list))
    if len(num_list) == 1:
        return str(numbers[sekilciliha_dir_full.index(num_list[0])]) + fctionChecksDir(num_list)
    if num_list[-1] in sekilciliha_dir_full:
        num_list[-1] = (sekilcisiz_word[sekilciliha_dir_full.index(num_list[-1])])
        return Decider(num_list) + ans1


def FunctionForCidir(num_list):
    def fctionChecksi4(num_list):
        if num_list[-1] in sekilciliha_inci_dir1:
            return '-cidir'
        elif num_list[-1] in sekilciliha_inci_dir2:
            return '-c??d??r'
        elif num_list[-1] in sekilciliha_inci_dir3:
            return '-cudur'
        elif num_list[-1] in sekilciliha_inci_dir4:
            return '-c??d??r'
    ans1 = str(fctionChecksi4(num_list))
    if len(num_list) == 1:
        return str(numbers[sekilciliha_inci_dir_full.index(num_list[0])]) + fctionChecksi4(num_list)
    if num_list[-1] in sekilciliha_inci_dir_full:
        num_list[-1] = (sekilcisiz_word[sekilciliha_inci_dir_full.index(num_list[-1])])
        return Decider(num_list) + ans1


def FunctionForDa(num_list):
    def fctionChecksDaOrDe(num_list):
        if num_list[-1] in sekilciliha_da:
            return '-da'
        else:
            return '-de'
    ans1 = str(fctionChecksDaOrDe(num_list))
    if len(num_list) == 1:
        return str(numbers[sekilciliha_dade.index(num_list[0])]) + fctionChecksDaOrDe(num_list)
    if num_list[-1] in sekilciliha_dade:
        num_list[-1] = (sekilcisiz_word[sekilciliha_dade.index(num_list[-1])])
        return Decider(num_list) + ans1


def FunctionForDan(num_list):
    def fctionChecksDanOrDen(num_list):
        if num_list[-1] in sekilciliha_dan:
            return '-dan'
        else:
            return '-den'
    ans1 = str(fctionChecksDanOrDen(num_list))
    if len(num_list) == 1:
        return str(numbers[sekilciliha_dan_full.index(num_list[0])]) + fctionChecksDanOrDen(num_list)
    if num_list[-1] in sekilciliha_dan_full:
        num_list[-1] = (sekilcisiz_word[sekilciliha_dan_full.index(num_list[-1])])
        return Decider(num_list) + ans1


def FunctionForLarDa(num_list):
    def fctionChecksLarda(num_list):
        if num_list[-1] in sekilciliha_larda:
            return '-larda'
        else:
            return '-l??rd??'
    ans1 = str(fctionChecksLarda(num_list))
    if len(num_list) == 1:
        return str(numbers[sekilciliha_lardal??rd??.index(num_list[0])]) + fctionChecksLarda(num_list)
    if num_list[-1] in sekilciliha_lardal??rd??:
        num_list[-1] = (sekilcisiz_word[sekilciliha_lardal??rd??.index(num_list[-1])])
        return Decider(num_list) + ans1


def FunctionForAe(num_list):
    def fctionChecksAE(num_list):
        if num_list[-1] in sekiliciliha_a:
            return '-a'
        else:
            return '-e'
    ans1 = str(fctionChecksAE(num_list))
    if len(num_list) == 1:
        return str(numbers[sekilciliha_ae_full.index(num_list[0])]) + fctionChecksAE(num_list)
    if num_list[-1] in sekilciliha_ae_full:
        num_list[-1] = (sekilcisiz_word[sekilciliha_ae_full.index(num_list[-1])])
        return Decider(num_list) + ans1


def FunctionForLi(num_list):
    def fctionChecksli(num_list):
        if num_list[-1] in sekilcili_li_1:
            return '-l??'
        elif num_list[-1] in sekilcili_li_2:
            return '-li'
        elif num_list[-1] in sekilcili_li_1:
            return '-l??'
        elif num_list[-1] in sekilcili_li_1:
            return '-lu'
    ans1 = str(fctionChecksli(num_list))
    if len(num_list) == 1:
        return str(numbers[sekilciliha_li_full.index(num_list[0])]) + fctionChecksli(num_list)
    if num_list[-1] in sekilciliha_li_full:
        num_list[-1] = (sekilcisiz_word[sekilciliha_li_full.index(num_list[-1])])
        return Decider(num_list) + ans1


def FunctionForIn(num_list):
    def fctionChecksIn(num_list):
        if num_list[-1] in sekilciliha_in1:
            return '-??n'
        elif num_list[-1] in sekilciliha_in2:
            return '-in'
        elif num_list[-1] in sekilciliha_in3:
            return '-un'
        elif num_list[-1] in sekilciliha_in4:
            return '-??n'
    ans1 = str(fctionChecksIn(num_list))
    if len(num_list) == 1:
        return str(numbers[sekilciliha_in_full.index(num_list[0])]) + fctionChecksIn(num_list)
    if num_list[-1] in sekilciliha_in_full:
        num_list[-1] = (sekilcisiz_word[sekilciliha_in_full.index(num_list[-1])])
        return Decider(num_list) + ans1


def FunctionForLarin(num_list):
    def fctionChecksLarIn(num_list):
        if num_list[-1] in sekilciliha_larin1:
            return '-lar??n'
        elif num_list[-1] in sekilciliha_larin2:
            return '-l??rin'
    ans1 = str(fctionChecksLarIn(num_list))
    if len(num_list) == 1:
        return str(numbers[sekilciliha_larin_full.index(num_list[0])]) + fctionChecksLarIn(num_list)
    if num_list[-1] in sekilciliha_larin_full:
        num_list[-1] = (sekilcisiz_word[sekilciliha_larin_full.index(num_list[-1])])
        return Decider(num_list) + ans1


def FunctionForLarl??r(num_list):
    def fctionChecksLar(num_list):
        if num_list[-1] in sekilciliha_lar1:
            return '-lar'
        elif num_list[-1] in sekilciliha_lar2:
            return '-l??r'
    ans1 = str(fctionChecksLar(num_list))
    if len(num_list) == 1:
        return str(numbers[sekilciliha_larl??r_full.index(num_list[0])]) + fctionChecksLar(num_list)
    if num_list[-1] in sekilciliha_larl??r_full:
        num_list[-1] = (sekilcisiz_word[sekilciliha_larl??r_full.index(num_list[-1])])
        return Decider(num_list) + ans1



def Decider(num_list):
    for i in num_list:
        if i in math_commands:
            return DoMathOperations(num_list)
    if num_list[-1] in sekilciliha_larin_full:
        return FunctionForLarin(num_list)
    if num_list[-1] in sekilciliha_larl??r_full:
        return FunctionForLarl??r(num_list)
    if num_list[-1] in sekilciliha_in_full:
        return FunctionForIn(num_list)
    if num_list[-1] in sekilciliha_li_full:
        return FunctionForLi(num_list)
    if num_list[-1] in sekilciliha_dade:
        return FunctionForDa(num_list)
    if num_list[-1] in sekilciliha_i_full:
        return FunctionForI(num_list)
    if num_list[-1] in sekilciliha_dan_full:
        return FunctionForDan(num_list)
    if num_list[-1] in sekilciliha_dir_full:
        return FunctionForDir(num_list)
    if num_list[-1] in sekilciliha_inci_dir_full:
        return FunctionForCidir(num_list)
    if num_list[-1] in sekilciliha_lardal??rd??:
        return FunctionForLarDa(num_list)
    if num_list[-1] in sekilciliha_ae_full:
        return FunctionForAe(num_list)
    for i in tamliq:
        if i in num_list and ('faiz' in num_list):
            return FunctionForFaizAndTamliq(num_list)
        if i in num_list and ('faiz' not in num_list):
            return FunctionForTamliq(num_list)
    if 'faiz' in num_list:
        return FunctionForFaiz(num_list)
    if 'n??qt??' in num_list:
        if num_list == ['n??qt??']:
            return 'n??qt??'
        elif len(num_list) > 1 and num_list[-1] == 'n??qt??':
            return FunctionNormal(num_list[:-1]) + " n??qt??"
        return FunctionForDrops(num_list)
    elif num_list[-1] in numbers_tur:
        return FunctionExtra(num_list)

    return FunctionNormal(num_list)


def symbol_seperate(text):
    """
        if there is a symbol in the text it seperates symbol from words
    """
    symbols = {
        '-': ' - ', '+': ' + ', '!': ' ! ', '@': ' @ ', '#': ' # ', '^': ' ^ ', '&': ' & ',
        '*': ' * ', '(': ' ( ', ')': ' ) ', '`': ' ` ', ';': ' ; ', ':': ' : ',
        "'": " ' ", '"': ' " ', '[': ' [ ', ']': ' ] ', '{': ' { ', '}': ' } ', '/': ' / ',
        ',': ' , ', '<': ' < ', '>': ' > ', '_': ' _ ', '=': ' = ', '?': ' ? ',
        '~': ' ~ ', '|': ' | ', '???': ' ??? ', '??': ' ?? ', '??': ' ?? ', '??': ' ?? ',
        '??': ' ?? ', '??': ' ?? ', '??': " ?? ", '???': ' ??? ', '???': ' ??? '
    }

    for w_i, i in symbols.items():
        text = text.replace(w_i, i)
    return text


def symbol_commine(text):
    """
        TODO
    """

    symbols = {
        ' - ': '-', ' + ': '+', ' ! ': '!', ' @ ': '@', ' # ': '#', ' ^ ': '^', ' & ': '&',
        ' * ': '*', ' ( ': '(', ' ) ': ')', ' ` ': '`', ' ; ': ';', ' : ': ':', " ' ": "'",
        ' " ': '"', ' [ ': '[', ' ] ': ']', ' { ': '{', ' } ': '}', ' / ': '/', ' , ': ',',
        ' < ': '<', ' > ': '>', ' _ ': '_', ' = ': '=', ' ? ': '?', ' ~ ': '~', ' | ': '|',
        ' ??? ': '???', ' ?? ': '??', ' ?? ': '??', ' ?? ': '??', ' ?? ': '??', ' ?? ': '??', ' ?? ': "??",
        ' ??? ': '???', ' ??? ': '???'
    }

    for w_i, i in symbols.items():
        text = text.replace(w_i, i)
    return text


def get_numbers(sentence):
    """
        Words in the sentence are added step by step.
        If the word is number, it adds it to numlist and calculating.
    """
    if sentence == '':
        return sentence
    sentence = sentence.replace('  ', ' ')
    sentence = '. ' + sentence + ' .'
    text = []
    numlist = []
    sent_splitted = sentence.split(' ')
    for i in sent_splitted:
        if i in all_turrk:
            numlist.append(i)
        elif i not in all_turrk:
            if len(numlist) != 0 and len(numlist) != 1:
                answer = Decider(numlist)
                numlist.clear()
                text.append(answer)
                text.append(i)
            else:
                if len(numlist) == 0:
                    text.append(i)
                    numlist.clear()
                elif len(numlist) == 1 and (numlist[0] in litnum_word):
                    text.append(str(litnum_word.index(numlist[0])))
                    numlist.clear()
                    text.append(i)
                elif len(numlist) == 1 and (numlist[0] in notlitnum_word):
                    text.append(
                        str(notlitnum[notlitnum_word.index(numlist[0])]))
                    numlist.clear()
                    text.append(i)
                else:
                    answer = Decider(numlist)
                    numlist.clear()
                    text.append(answer)
                    text.append(i)
    
    end = " ".join(text)
    end = symbol_commine(end)
    for i in range(2):
        end = end.replace('  ', ' ')

    return end[2:-2]


while True:
    k = str(input())
    try:
        print(get_numbers(k))
    except EOFError:
        print('Try again', file=sys.stderr)

