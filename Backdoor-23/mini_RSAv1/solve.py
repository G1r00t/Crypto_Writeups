from Crypto.Util.number import long_to_bytes
import gmpy2
c = 5926440800047066468184992240057621921188346083131741617482777221394411358243130401052973132050605103035491365016082149869814064434831123043357292949645845605278066636109516907741970960547141266810284132826982396956610111589
m = int(gmpy2.iroot(c, 3)[0])
print(long_to_bytes(m))