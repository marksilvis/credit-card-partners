import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib_venn import venn2, venn3

st.title("US Credit Card Travel Partners")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

# Load CSV file
df = pd.read_csv('credit_card_data.csv')

# Extract credit card names
credit_card_names = df['Credit Card'].unique()

# Create sets of travel partners for each credit card
partner_sets = []
for card in credit_card_names:
    card_partners = set(df[df['Credit Card'] == card]['Travel Partner'])
    if len(card_partners) > 0:
        partner_sets.append(card_partners)

# Create Venn diagram
if len(partner_sets) == 3:
    # Assign unique colors to intersection areas
    c = ('red', 'green', 'blue', 'yellow', 'purple', 'cyan', 'gray')
    v = venn3(subsets=partner_sets, set_labels=credit_card_names, set_colors=c, normalize_to=100)

    # Add travel partner names to intersection areas
    v.get_label_by_id('100').set_text('\n'.join(partner_sets[0] - partner_sets[1] - partner_sets[2]))
    v.get_label_by_id('010').set_text('\n'.join(partner_sets[1] - partner_sets[0] - partner_sets[2]))
    v.get_label_by_id('001').set_text('\n'.join(partner_sets[2] - partner_sets[0] - partner_sets[1]))
    v.get_label_by_id('110').set_text('\n'.join(partner_sets[0] & partner_sets[1] - partner_sets[2]))
    v.get_label_by_id('101').set_text('\n'.join(partner_sets[0] & partner_sets[2] - partner_sets[1]))
    v.get_label_by_id('011').set_text('\n'.join(partner_sets[1] & partner_sets[2] - partner_sets[0]))
    v.get_label_by_id('111').set_text('\n'.join(partner_sets[0] & partner_sets[1] & partner_sets[2]))
    
    # Adjust text size
    for t in v.set_labels: t.set_fontsize(12)
    for t in v.subset_labels: t.set_fontsize(8)
elif len(partner_sets) == 2:
    v = venn2(subsets=partner_sets, set_labels=credit_card_names)
else:
    print("Error: Number of credit cards must be 2 or 3")

plt.title("Credit Card Partners 5/2024", fontsize = 14)
plt.savefig('test.png')
fig = plt.show
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot(plt.show())
