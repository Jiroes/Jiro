m_dict = {
        'CRINGE': "sesuatu yang sangat aneh atau memalukan "
        'LOL':"tanggapan sesuatu yang lucu"
        'GG':"permainan bagus"
        'NT':"kerja bagus"
        }
word = input("ketik kata yang tidak kau ketahui")        
        
if word in m_dict.keys():
    print(m_dict[word])
    
else:
    print('tak valid')
