import requests
#from concurrent.futures import ThreadPoolExecutor
import concurrent.futures

NODES = 4 #will accept as input
#create a list of 4 URLs running Flask, which will then accept the job
#we have to make it like hadoop
#urls = ["http://127.0.0.1:6000", "http://127.0.0.1:6001", "http://127.0.0.1:6002", "http://127.0.0.1:6003"]
urls = ["http://127.0.0.1:5000", "http://127.0.0.1:5001", "http://127.0.0.1:5002", "http://127.0.0.1:5003"]
num_computations = int(input("Enter the number of computations:\n")) #user will enter a number. We divide it by 4 and send the job to each node

#we have to send the job to each node at the same time
#creating a list of jobs
jobs = []
result = []
for i in range(NODES):
    jobs.append(num_computations//NODES)
#print(jobs)
#sending the jobs to each node asynchronously
def send_job(url, job_num):
    return requests.get(url + "?data=" + str(job_num)).json()

#use threadpoolexecutor to send the jobs to each node

with concurrent.futures.ThreadPoolExecutor(max_workers = 4) as executor:
    for d in range(len(urls)):
        result.append(executor.submit(send_job, url=urls[d], job_num=jobs[d]))

    for future in concurrent.futures.as_completed(result):
        print(future.result())

#print(result)