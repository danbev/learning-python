import sys

fin = open(sys.argv[1], "rt")
data = fin.read()
data = data.replace('#.include fipsmodule.cnf', '.include %s' % sys.argv[2])
data = data.replace('#fips = fips_sect', 'fips = fips_sect')
fin.close()
fin = open(sys.argv[1], "wt")
fin.write(data)
fin.close()
