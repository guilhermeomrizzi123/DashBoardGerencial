import pandas as pd

# - - - - - - - - SAP E1-170 - - - - - - - - -- - - - - - - - SAP E1-170 - - - - - - - - -- - - - - - - - SAP E1-170 -
# Função para organizar o cabeçalho e permitir a leitura do txt.
col_names = ['TIPO_DOC_GRD','NUM_DOC_GRD','MFRPN','DOKAR','DOKNR','DOKVR','MATNR','DSC_MODIF','IND_STAT_PN','EXP_DATE']

# Abrir a base de dados do SAP (ZTDP_PN_AFETADO.txt)
df_sap = pd.read_csv(r'C:\Users\grizzi\05-PycharmProjects\LiberacaoPNs\ZTDP_PN_AFETADO.txt', sep='|', encoding='utf-8', names = col_names, low_memory=False)

# Localizar e adicionar sinais nas letras de revisão.
df_sap['DOKVR'].replace(' /','--/',inplace=True)
df_sap['DOKVR'].replace(' A','--A',inplace=True)
df_sap['DOKVR'].replace(' B','--B',inplace=True)
df_sap['DOKVR'].replace(' C','--C',inplace=True)
df_sap['DOKVR'].replace(' D','--D',inplace=True)
df_sap['DOKVR'].replace(' E','--E',inplace=True)
df_sap['DOKVR'].replace(' F','--F',inplace=True)
df_sap['DOKVR'].replace(' G','--G',inplace=True)
df_sap['DOKVR'].replace(' H','--H',inplace=True)
df_sap['DOKVR'].replace(' I','--I',inplace=True)
df_sap['DOKVR'].replace(' J','--J',inplace=True)
df_sap['DOKVR'].replace(' K','--K',inplace=True)
df_sap['DOKVR'].replace(' L','--L',inplace=True)
df_sap['DOKVR'].replace(' M','--M',inplace=True)
df_sap['DOKVR'].replace(' N','--N',inplace=True)
df_sap['DOKVR'].replace(' O','--O',inplace=True)
df_sap['DOKVR'].replace(' P','--P',inplace=True)
df_sap['DOKVR'].replace(' Q','--Q',inplace=True)
df_sap['DOKVR'].replace(' R','--R',inplace=True)
df_sap['DOKVR'].replace(' S','--S',inplace=True)
df_sap['DOKVR'].replace(' T','--T',inplace=True)
df_sap['DOKVR'].replace(' U','--U',inplace=True)
df_sap['DOKVR'].replace(' V','--V',inplace=True)
df_sap['DOKVR'].replace(' W','--W',inplace=True)
df_sap['DOKVR'].replace(' X','--X',inplace=True)
df_sap['DOKVR'].replace(' Y','--Y',inplace=True)
df_sap['DOKVR'].replace(' Z','--Z',inplace=True)
df_sap['DOKVR'].replace(' /','--/',inplace=True)
df_sap['DOKVR'].replace('AA','-AA',inplace=True)
df_sap['DOKVR'].replace('AB','-AB',inplace=True)
df_sap['DOKVR'].replace('AC','-AC',inplace=True)
df_sap['DOKVR'].replace('AD','-AD',inplace=True)
df_sap['DOKVR'].replace('AE','-AE',inplace=True)
df_sap['DOKVR'].replace('AF','-AF',inplace=True)
df_sap['DOKVR'].replace('AG','-AG',inplace=True)
df_sap['DOKVR'].replace('AH','-AH',inplace=True)
df_sap['DOKVR'].replace('AI','-AI',inplace=True)
df_sap['DOKVR'].replace('AJ','-AJ',inplace=True)
df_sap['DOKVR'].replace('AK','-AK',inplace=True)
df_sap['DOKVR'].replace('AL','-AL',inplace=True)
df_sap['DOKVR'].replace('AM','-AM',inplace=True)
df_sap['DOKVR'].replace('AN','-AN',inplace=True)
df_sap['DOKVR'].replace('AO','-AO',inplace=True)
df_sap['DOKVR'].replace('AP','-AP',inplace=True)
df_sap['DOKVR'].replace('AQ','-AQ',inplace=True)
df_sap['DOKVR'].replace('AR','-AR',inplace=True)
df_sap['DOKVR'].replace('AS','-AS',inplace=True)
df_sap['DOKVR'].replace('AT','-AT',inplace=True)
df_sap['DOKVR'].replace('AU','-AU',inplace=True)
df_sap['DOKVR'].replace('AV','-AV',inplace=True)
df_sap['DOKVR'].replace('AW','-AW',inplace=True)
df_sap['DOKVR'].replace('AX','-AX',inplace=True)
df_sap['DOKVR'].replace('AY','-AY',inplace=True)
df_sap['DOKVR'].replace('AZ','-AZ',inplace=True)

# Concatenar PN com Letra de Revisão.
df_sap['FullPN_E1_170']=df_sap.MFRPN.str.cat(df_sap['DOKVR'],'')

# Remove colunas sem utilidade.
df_sap = df_sap[['TIPO_DOC_GRD', 'NUM_DOC_GRD', 'FullPN_E1_170']]




# - - - - - - - - 3DCOM E1-170 - - - - - - - -- - - - - - - - 3DCOM E1-170 - - - - - - - -- - - - - - 3DCOM E1-170 - -
# Abrir a base de dados do 3DCOM (VPM_VISIB_REL-PART-E170ENG.csv)
df_vpm_actionlist_e170 = pd.read_csv(r'C:\Users\grizzi\05-PycharmProjects\LiberacaoPNs\ActionList170.txt', sep=' ', encoding='utf-8', low_memory=False)

# Criar coluna para separar da string somente o valor que desejamos.
    # Para separar PN
df_vpm_actionlist_e170['N_Action_Id'] = df_vpm_actionlist_e170['Action'].str.extract('(...-.....-...)', expand = True)

    # Para separar letra de revisão.
df_vpm_actionlist_e170['N_Revision_Letter'] = df_vpm_actionlist_e170['Action'].str.extract('(_...)', expand = True)

    # Substituir sinais nas letras de revisão com o mesmo padrão adotado no df do SAP.
df_vpm_actionlist_e170['N_Revision_Letter'].replace('_--_','--/',inplace=True)
df_vpm_actionlist_e170['N_Revision_Letter'].replace('_--A','--A',inplace=True)
df_vpm_actionlist_e170['N_Revision_Letter'].replace('_--B','--B',inplace=True)
df_vpm_actionlist_e170['N_Revision_Letter'].replace('_--C','--C',inplace=True)
df_vpm_actionlist_e170['N_Revision_Letter'].replace('_--D','--D',inplace=True)
df_vpm_actionlist_e170['N_Revision_Letter'].replace('_--E','--E',inplace=True)
df_vpm_actionlist_e170['N_Revision_Letter'].replace('_--F','--F',inplace=True)
df_vpm_actionlist_e170['N_Revision_Letter'].replace('_--G','--G',inplace=True)
df_vpm_actionlist_e170['N_Revision_Letter'].replace('_--H','--H',inplace=True)
df_vpm_actionlist_e170['N_Revision_Letter'].replace('_--I','--I',inplace=True)
df_vpm_actionlist_e170['N_Revision_Letter'].replace('_--J','--J',inplace=True)
df_vpm_actionlist_e170['N_Revision_Letter'].replace('_--K','--K',inplace=True)
df_vpm_actionlist_e170['N_Revision_Letter'].replace('_--L','--L',inplace=True)
df_vpm_actionlist_e170['N_Revision_Letter'].replace('_--M','--M',inplace=True)
df_vpm_actionlist_e170['N_Revision_Letter'].replace('_--N','--N',inplace=True)
df_vpm_actionlist_e170['N_Revision_Letter'].replace('_--O','--O',inplace=True)
df_vpm_actionlist_e170['N_Revision_Letter'].replace('_--P','--P',inplace=True)
df_vpm_actionlist_e170['N_Revision_Letter'].replace('_--Q','--Q',inplace=True)
df_vpm_actionlist_e170['N_Revision_Letter'].replace('_--R','--R',inplace=True)
df_vpm_actionlist_e170['N_Revision_Letter'].replace('_--S','--S',inplace=True)
df_vpm_actionlist_e170['N_Revision_Letter'].replace('_--T','--T',inplace=True)
df_vpm_actionlist_e170['N_Revision_Letter'].replace('_--U','--U',inplace=True)
df_vpm_actionlist_e170['N_Revision_Letter'].replace('_--V','--V',inplace=True)
df_vpm_actionlist_e170['N_Revision_Letter'].replace('_--W','--W',inplace=True)
df_vpm_actionlist_e170['N_Revision_Letter'].replace('_--X','--X',inplace=True)
df_vpm_actionlist_e170['N_Revision_Letter'].replace('_--Y','--Y',inplace=True)
df_vpm_actionlist_e170['N_Revision_Letter'].replace('_--Z','--Z',inplace=True)
df_vpm_actionlist_e170['N_Revision_Letter'].replace('_-AA','-AA',inplace=True)
df_vpm_actionlist_e170['N_Revision_Letter'].replace('_-AB','-AB',inplace=True)
df_vpm_actionlist_e170['N_Revision_Letter'].replace('_-AC','-AC',inplace=True)
df_vpm_actionlist_e170['N_Revision_Letter'].replace('_-AD','-AD',inplace=True)
df_vpm_actionlist_e170['N_Revision_Letter'].replace('_-AE','-AE',inplace=True)
df_vpm_actionlist_e170['N_Revision_Letter'].replace('_-AF','-AF',inplace=True)
df_vpm_actionlist_e170['N_Revision_Letter'].replace('_-AG','-AG',inplace=True)
df_vpm_actionlist_e170['N_Revision_Letter'].replace('_-AH','-AH',inplace=True)
df_vpm_actionlist_e170['N_Revision_Letter'].replace('_-AI','-AI',inplace=True)

    # Concatenar PN com Letra de Revisão.
df_vpm_actionlist_e170['FullPN_E1_170']=df_vpm_actionlist_e170.N_Action_Id.str.cat(df_vpm_actionlist_e170['N_Revision_Letter'],'')

df_vpm_actionlist_e170 = df_vpm_actionlist_e170[['Action','FullPN_E1_170']]

# - -Junção 3DCOM E1-170 & SAP E1-170 - - - Junção 3DCOM E1-170 & SAP E1-170 - - - Junção 3DCOM E1-170 & SAP E1-170 - -
df_170e1 = df_vpm_actionlist_e170.merge(df_sap, on= 'FullPN_E1_170')

# Filtro Teste
df_170e1 = df_170e1 [df_170e1['FullPN_E1_170'] == '171-11116-401--/']


#etetetete
