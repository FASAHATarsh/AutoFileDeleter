import os
import shutil
import time


def main():
	folder_count = 0
	file_count = 0
#	path =input("Enter path(basepath) : ") 
	path = 'D:\Iron Arsh\Coding\Python\demoFolder\demo1'
#	seconds = time.time() - (30 * 24 * 60 * 60)
	seconds = time.time() - (5* 60)

	if os.path.exists(path):
		for root_folder, folders, files in os.walk(path):
			if seconds >= get_age(root_folder):
				remove_folder(root_folder)
				folder_count += 1
				break
			else:
				for folder in folders:
					folder_path = os.path.join(root_folder,folder)
					if seconds >= get_age(folder_path):
						remove_folder(folder_path)
						folder_count += 1
				for file in files:
					file_path = os.path.join(root_folder, file)
					if seconds >= get_age(file_path):
						remove_file(file_path)
						file_count += 1
		else:
			if seconds >= get_age(path):
				remove_file(path)
				file_count += 1

	else:
		print(f"{path}"+" is not found")
		file_count += 1 

	print("Total folders deleted: " + f"{folder_count}")
	print("Total files deleted:" + f"{file_count}")


def remove_folder(path):
	if not shutil.rmtree(path):
		print(f"{path}" + " is removed successfully!")

	else:
		print("Unable to delete the " + f"{path}")



def remove_file(path):
	if not os.remove(path):
		print(f"{path}" + " is removed successfully!")

	else:
		print("Unable to delete the " + f"{path}")


def get_age(path):
	ctime = os.stat(path).st_ctime
	return ctime


if __name__ == '__main__':
	main()
