import random 

def nilairandom(): 
 return random.uniform (-10,10) 

def nilaiminimum(x1,x2): 
 f = (4-2.1*x1**2 + (x1**4/3))*x1**2+x1**2+(-4+4*x2**2)*x2**2 
 return f 

def probabilitas(tampung,nilaiminawal,suhusaatitu): 
 P = (2.7182)**(nilaiminawal-tampung)/suhusaatitu 
 return P 

suhuawal = 500
suhuakhir = 0.01 
alpha = 0.8 # nilai untuk mengurangi suhu awal atau yang jalan-jalan  
x1= nilairandom() 
x2= nilairandom()  
nilaiminawal= nilaiminimum(x1,x2)

while (suhuawal > suhuakhir) : 
	 for i in range (10000) : 
		  x1= nilairandom() 
		  x2= nilairandom()  
		  tampung = nilaiminimum(x1,x2) 
		  if (nilaiminawal>tampung) : 
		   nilaiminawal = tampung # best so far mengganti nilai terkecil yang telah didapat 
		  else : 
		   if probabilitas(tampung,nilaiminawal,suhuawal)>random.random(): 
		    nilaiminawal = tampung # memilih nilai probabilitasnya jika lebih besar 
		    suhuawal = suhuawal * alpha 
print(nilaiminawal)