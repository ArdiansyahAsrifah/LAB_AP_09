golongan = input("golongan= ").upper()
daya = float(input("daya= "))
pemakaian = float(input("pemakaian= "))
tagihan = 0

match (golongan, daya):
    case ("R1", 900):
        tagihan = 1.352 * pemakaian
    case ("R1", 1.300):
        tagihan = 1444.70 * pemakaian
    case ("R1", 2.200):
        tagihan = 1444.70 * pemakaian
    case ("R2",_) if 3.500 <= daya <= 5.500:
        tagihan = 1699.53 * pemakaian
    case ("R3",_) if daya >= 6.600:
        tagihan = 1699.53 * pemakaian
    case ("B2",_) if 6.600 <= daya <= 200000:
        tagihan = 1444.70 * pemakaian
    case ("B3",_) if daya > 200000:
        tagihan = 1114.74 * pemakaian
    case ("I3",_) if daya>= 200000:
        tagihan = 1314.12 * pemakaian
    case ("P1",_) if 6.600 <= daya <= 200000:
        tagihan = 1523.28 * pemakaian
    case (_):
        print('data tidak valid') 

print(f"Jumlah tagihan anda sebesar:Rp {tagihan:,.2f}".replace('.','+').replace(',','.').replace('+',','))

