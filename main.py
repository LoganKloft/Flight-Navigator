import load
import time

start_time = time.time()
loader = load.Load()
loader.clean_data()
loader.create_airports()
loader.create_airlines()
loader.create_routes()
loader.create_relations()
end_time = time.time()
print("Total time:", end_time - start_time, "seconds")