import os
import pandas as pd

audio_directory = 'audio'

data = {
    'audio_file_path': [],
    'label': []
}


for root, dirs, files in os.walk(audio_directory):
    for file in files:
        if file.endswith('.wav'):
            file_path = os.path.join(root, file)
            label = 0
            if file.startswith('song'):
                label = 1
            data['audio_file_path'].append(file_path)
            data['label'].append(label)

df = pd.DataFrame(data)

csv_file_path = 'audio_data_labels.csv'
df.to_csv(csv_file_path, index=False)

print(f'CSV file created at {csv_file_path}')