import papermill as pm
import json

def run_notebook(text):
    input_path = 'bpmn_generator/model/NLP_Model.ipynb'
    output_path = 'bpmn_generator/model/output_notebook.ipynb'
    
    pm.execute_notebook(
        input_path,
        output_path,
        parameters=dict(text=text)
    )
    
    with open(output_path, 'r') as f:
        notebook_content = json.load(f)
    
    results = []
    for cell in notebook_content['cells']:
        if cell['cell_type'] == 'code':
            for output in cell.get('outputs', []):
                if output['output_type'] == 'stream':
                    output_data = output['text']
                    if isinstance(output_data, list):
                        for item in output_data:
                            results.append(item.strip())
                    else:
                        results.append(output_data.strip())
 
    del results[-1]
    
    return results