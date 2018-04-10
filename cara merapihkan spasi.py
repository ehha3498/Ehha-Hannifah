nama = ["Ari","Bambang"]
nilai = [80,70]

print("==========================")
print("| No |    Nama   | Nilai |")
print("==========================")

for i in range(len(nama)):
    #print("| %2d | %-11s| %5d |" %(i+1,nama(i),nilai[i]))
    print("| {no:2d} | {nama:11s} | {nilai:5.2f} |". format(nama=nama[i],nilai=nilai[i],no=i+1))

print("==========================")

