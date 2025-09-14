import gradio as gr
from rdkit import Chem
from rdkit.Chem import Draw
import random
import pandas as pd

# Simple generative chemist agent to generate molecule fragments
# We're simulating the generation process for this MVP
# A more advanced version would use a true generative model like a fine-tuned ChemBERTa
def generate_molecule_smiles():
    """Generates a random, but valid, SMILES string for demonstration."""
    # A simple list of starting SMILES fragments to "generate"
    fragments = [
        "C1CC1", "C1=CC=C(C=C1)O", "CNC(=O)c1cn(C)c2ccccc12",
        "CC(C)CC(C)N", "c1ccccc1-c1ccccc1"
    ]
    
    # In a real app, this would be a call to a generative model
    # For now, we'll pick one and "mutate" it
    base_smiles = random.choice(fragments)
    
    # Add a simple, random "modification" to simulate generative process
    modifiers = ["-C(=O)O", "-N(=O)O", "-F", "-Cl"]
    if random.random() > 0.5:
        return base_smiles + random.choice(modifiers)
    else:
        return base_smiles

# Predictor Agent (Mock)
# For the MVP, we will use a simple, deterministic function to "predict" properties
# A real-world app would use a pre-trained QSAR/QSPR model
def predict_properties(smiles):
    """Mocks the prediction of key drug properties."""
    try:
        mol = Chem.MolFromSmiles(smiles)
        if mol is None:
            return None, None, None, "Invalid SMILES string."

        # Mock predictions based on molecule length or a simple rule
        length_factor = len(smiles) / 50.0
        
        binding_affinity = 0.85 - random.random() * 0.2
        toxicity_score = 0.1 + random.random() * 0.3
        
        # A simple check to simulate a bad candidate
        if "C(=O)O" in smiles: # Example:
            toxicity_score += 0.5 # a known bad fragment
            
        toxicity_score = round(min(1.0, toxicity_score), 2)
        binding_affinity = round(max(0, binding_affinity), 2)

        return binding_affinity, toxicity_score, "Oral", "Success"

    except Exception as e:
        return None, None, None, f"Error: {str(e)}"

# Gradio UI
def run_compass(viral_target):
    """Main function for the Gradio interface."""
    
    status = "Generating and evaluating new molecular candidates..."
    
    smiles_string = generate_molecule_smiles()
    
    # Run the "Predictor" agent
    binding, toxicity, availability, result_status = predict_properties(smiles_string)
    
    # Generate the 2D molecular image
    mol = Chem.MolFromSmiles(smiles_string)
    if mol is None:
        return None, "Error: Could not visualize molecule.", None

    # **CORRECTED LINE:** Use MolToImage to get a Pillow image object directly
    mol_image = Draw.MolToImage(mol, size=(400, 400))
    
    # Prepare the output as a table for Gradio
    properties = pd.DataFrame({
        "Property": ["Binding Affinity", "Toxicity Score", "Bioavailability"],
        "Value": [
            f"{binding:.2f} (High is better)",
            f"{toxicity:.2f} (Low is better)",
            availability
        ]
    })
    
    return mol_image, smiles_string, gr.Dataframe(properties)

# Gradio Interface setup
with gr.Blocks() as demo:
    gr.Markdown("# Molecular Compass: The AI-Native Drug Discovery Engine")
    gr.Markdown("Reimagining Pardes Biosciences for 2025.")
    
    with gr.Row():
        with gr.Column(scale=2):
            target_input = gr.Textbox(
                label="Target Protein",
                placeholder="e.g., SARS-CoV-2 Main Protease (M-pro)",
                value="SARS-CoV-2 Main Protease (M-pro)"
            )
            generate_button = gr.Button("Generate & Evaluate Candidate")
            
        with gr.Column(scale=1):
            with gr.Accordion("How It Works", open=False):
                gr.Markdown(
                    "1. **Generative Chemist:** Creates a novel molecular structure.\n"
                    "2. **Predictor Agent:** Simulates properties like toxicity and binding.\n"
                    "3. **Optimizer:** Refines the design based on the results."
                )

    with gr.Row():
        with gr.Column(scale=1):
            smiles_output = gr.Textbox(label="Generated Molecule (SMILES)")
            molecule_image = gr.Image(label="2D Visualization")
        
        with gr.Column(scale=1):
            properties_output = gr.Dataframe(label="Predicted Properties")

    generate_button.click(
        fn=run_compass,
        inputs=target_input,
        outputs=[molecule_image, smiles_output, properties_output]
    )

demo.launch()