import argparse
import numpy
import matplotlib.pyplot as plt
import pickle
import os
import math

def split_orbits(orbits):
	print("split branch")
	def generator_split(gen):
		cores = int(os.environ.get("OMP_NUM_THREADS"))
		if cores == 1:
			 yield gen
		else:
			num = math.ceil(gen.size / (cores))
			print(num)
			for i in range(cores):
				end = num*(i+1)
				if i == cores - 1:
					end = gen.size
				yield gen[num*i:end]
	for i, x in enumerate(generator_split(orbits)):
		with open(f"orbit{i:03d}.pickle","wb") as file:
			pickle.dump(x,file)

def fetch_orbit_data(input,filename):
    i = numpy.arange(0,len(input.t),40)
    ts = input.t[i]
    print("fetch branch")
    energy = input.E(ts)
    momentum = input.Lz(ts)
    res = numpy.array([energy,momentum])
    print(res)
    with open(f"wipmom_{os.path.basename(filename)}","wb") as file:
        pickle.dump(res,file)
    return 0

def compile():
	res = numpy.array([])
	for filename in os.listdir():
		if "wipmom" in filename:
			with open(filename, "rb") as file:
				if res.size == 0:
					res = pickle.load(file)
				else:
					res = numpy.concatenate((res, pickle.load(file)),1)
	with open("momentum.pickle","wb") as file:
		pickle.dump(res,file)
		

def main():
	parser = argparse.ArgumentParser("momentum")

	parser.add_argument("-s","--split",default=False)
	parser.add_argument("-c","--compile",default=False)
	parser.add_argument("filename")
	args =parser.parse_args()
	if os.path.exists(args.filename):
		with open(args.filename, "rb") as file:
			data = pickle.load(file)
	else:
		print("file provided does not exist")
		return 0
	if bool(args.split) == True:
		print("split")
		split_orbits(data)
	elif bool(args.compile) == True:
		print("compile")
		compile()
	else:
		fetch_orbit_data(data,args.filename)
	return 0

if __name__ == '__main__':
    main()
