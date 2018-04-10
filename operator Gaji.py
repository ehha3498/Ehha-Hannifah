gaji=input("masukkan gaji:")
berkeluarga=(False,True)[raw_input("sudah berkeluarga? (Y/T)")=="T"] 
punya_rumah=(False,True)[raw_input("punya rumah? (Y/T)")=="Y"]

if gaji > 3000000:
   print("gaji sudah diatas UMR")
   if berkeluarga:
       print ("wajib ikutan asuransi dan menabung untuk pensiun")
   else:
       print("Tidak perlu ikutan asuransi")

   if Punya_rumah:
       print("Wajib bayar pajak rumah")
   else:
       print("Tidak wajib bayar pajak rumah")
else:
    print("gaji belum UMR")
        
       
      
