import os
import time

# get the number of files in input folder
input_folder = 'partitioned-mini-selected'
output_folder = 'partitioned-results-mini'
file_names = sorted(os.listdir(input_folder))

print(file_names)

for n in file_names:
    #restart script
    os.system('python restart.py')

    #move file to process
    os.system("cp {}/{} output/data/OIE_2016/P0.jsonl".format(input_folder, n))
    """ 
    try: """
    os.system("""
                python scripts/manager.py --task=OIE_2016 --model="bert-large-cased" --beam-size=6 --max-distance=2048 --batch-size-per-device=4 --stage=0 --cuda=0
            """)
    """     except:
        pass """
    
    os.system("mv result/OIE_2016.bert-large-cased.np.d2048.b6.sorted/P0_result.json {}/{}.json".format(output_folder, n))
