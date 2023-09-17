import asyncio
import time
import os

# async function to wait for a text file to exist
async def CheckFileExists(filename=None, waittime=1, attempts=5, extensions=None):
	for attempt in range(attempts):
		if os.path.exists(filename) and any(filename.endswith(extension) for extension in extensions):
			print(f"File {filename} exists")
			return
		else:
			await asyncio.sleep(waittime)
	print(f"File {filename} does not exist after {attempts} attempts")

async def main(filelist, waittime, attempts, extensions):
	for file in filelist:
		await CheckFileExists(file, waittime, attempts, extensions)

if __name__ == "__main__":
	# Declare variables
	waittime = 1
	attempts = 5
	extensions = [".txt",".csv",".tsv"]
	filelist = ["data/test.tsv","data/test.csv","data/test.txt"]

	start = time.perf_counter()
	asyncio.run(main(filelist, waittime, attempts, extensions))
	end = time.perf_counter() - start
	print(f"{__file__} executed in {end:0.2f} seconds.")