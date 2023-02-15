#!/usr/bin/env python
# coding: utf-8

# In[1]:


from mewpy.simulation import solvers
from mewpy.simulation import set_default_solver
set_default_solver('glpk')


# In[2]:


from cobra.io.sbml import read_sbml_model
model = read_sbml_model('Human-GEM-annotated.xml')
model


# In[3]:


reaction_id = 'HMR_4396' #change this manually, cannot make into function as variable won't save...
print('target reaction',':',model.reactions.get_by_id(reaction_id).id,':',model.reactions.get_by_id(reaction_id).name)
print('\n')
metabolites_list = []
immediately_connected = {}
connected_by_one_reaction = {}
do_not_scan = ['H2O','Pi','H+','PPi','NADPH','NADP+'] #append this with whatever you aren't interested in
for m in (model.reactions.get_by_id(reaction_id).metabolites):
    print('metabolite:',m.name)
    rxns = []
    for rxn in m.reactions:
        print(m.name,'->',rxn.id,':',rxn.name)
        rxns.append(rxn.id)
        metabolites_list.append(m.name)
    immediately_connected[m.name] = rxns
    print('\n')
print('reactions immediately connected to the target reaction:')
print(rxns)
print('\n')
print('reactions connected to immediately connected reactions:')
for r in rxns:
    for mb in (model.reactions.get_by_id(r).metabolites):
        rxns_2 = []
        if mb.name not in metabolites_list:
            if mb.name not in do_not_scan:
                print('metabolite:',mb.name)
                metabolites_list.append(mb.name)
                for reaction in mb.reactions:
                    print(mb.name,'->',reaction.id,':',reaction.name)
                    rxns_2.append(reaction.id)
                connected_by_one_reaction[mb.name] = rxns_2
                print('\n')


# In[4]:


#example of printing the dictionaries
for k,v in immediately_connected.items():
    print(k,v)
    print('\n')
for key, value in connected_by_one_reaction.items():
    print(key, value)
    print('\n')


# In[5]:


#what does the result look like?
print('number of reactions immediately connected to target reaction:', len(immediately_connected))
print('number of reactions feeding into immediately connected reactions:', len(connected_by_one_reaction))


# In[ ]:




