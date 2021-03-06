import pandas as pd
from datetime import date
from datetime import timedelta

# - - - - - - - - SAP E1-170 - - - - - - - - -- - - - - - - - SAP E1-170 - - - - - - - - -- - - - - - - - SAP E1-170 -
    # Função para organizar o cabeçalho e permitir a leitura do txt.
col_names = ['TIPO_DOC_GRD','NUM_DOC_GRD','MFRPN','DOKAR','DOKNR','DOKVR','MATNR','DSC_MODIF','IND_STAT_PN','EXP_DATE']

    # Abrir a base de dados do SAP (ZTDP_PN_AFETADO.txt)
df_sap = pd.read_csv(r'C:\Users\grizzi\05-PycharmProjects\LiberacaoPNs\ZTDP_PN_AFETADO.txt', sep='|', encoding='utf-8', names = col_names, low_memory=False)

    # Localizar e adicionar sinais nas letras de revisão.
df_sap["DOKVR"].replace("","--/",inplace=True)
df_sap["DOKVR"].replace(" /","--/",inplace=True)
df_sap["DOKVR"].replace(" A","--A",inplace=True)
df_sap["DOKVR"].replace(" B","--B",inplace=True)
df_sap["DOKVR"].replace(" C","--C",inplace=True)
df_sap["DOKVR"].replace(" D","--D",inplace=True)
df_sap["DOKVR"].replace(" E","--E",inplace=True)
df_sap["DOKVR"].replace(" F","--F",inplace=True)
df_sap["DOKVR"].replace(" G","--G",inplace=True)
df_sap["DOKVR"].replace(" H","--H",inplace=True)
df_sap["DOKVR"].replace(" I","--I",inplace=True)
df_sap["DOKVR"].replace(" J","--J",inplace=True)
df_sap["DOKVR"].replace(" K","--K",inplace=True)
df_sap["DOKVR"].replace(" L","--L",inplace=True)
df_sap["DOKVR"].replace(" M","--M",inplace=True)
df_sap["DOKVR"].replace(" N","--N",inplace=True)
df_sap["DOKVR"].replace(" O","--O",inplace=True)
df_sap["DOKVR"].replace(" P","--P",inplace=True)
df_sap["DOKVR"].replace(" Q","--Q",inplace=True)
df_sap["DOKVR"].replace(" R","--R",inplace=True)
df_sap["DOKVR"].replace(" S","--S",inplace=True)
df_sap["DOKVR"].replace(" T","--T",inplace=True)
df_sap["DOKVR"].replace(" U","--U",inplace=True)
df_sap["DOKVR"].replace(" V","--V",inplace=True)
df_sap["DOKVR"].replace(" W","--W",inplace=True)
df_sap["DOKVR"].replace(" X","--X",inplace=True)
df_sap["DOKVR"].replace(" Y","--Y",inplace=True)
df_sap["DOKVR"].replace(" Z","--Z",inplace=True)
df_sap["DOKVR"].replace("AA","-AA",inplace=True)
df_sap["DOKVR"].replace("AB","-AB",inplace=True)
df_sap["DOKVR"].replace("AC","-AC",inplace=True)
df_sap["DOKVR"].replace("AD","-AD",inplace=True)
df_sap["DOKVR"].replace("AE","-AE",inplace=True)
df_sap["DOKVR"].replace("AF","-AF",inplace=True)
df_sap["DOKVR"].replace("AG","-AG",inplace=True)
df_sap["DOKVR"].replace("AH","-AH",inplace=True)
df_sap["DOKVR"].replace("AI","-AI",inplace=True)
df_sap["DOKVR"].replace("AJ","-AJ",inplace=True)
df_sap["DOKVR"].replace("AK","-AK",inplace=True)
df_sap["DOKVR"].replace("AL","-AL",inplace=True)
df_sap["DOKVR"].replace("AM","-AM",inplace=True)
df_sap["DOKVR"].replace("AN","-AN",inplace=True)
df_sap["DOKVR"].replace("AO","-AO",inplace=True)
df_sap["DOKVR"].replace("AP","-AP",inplace=True)
df_sap["DOKVR"].replace("AQ","-AQ",inplace=True)
df_sap["DOKVR"].replace("AR","-AR",inplace=True)
df_sap["DOKVR"].replace("AS","-AS",inplace=True)
df_sap["DOKVR"].replace("AT","-AT",inplace=True)
df_sap["DOKVR"].replace("AU","-AU",inplace=True)
df_sap["DOKVR"].replace("AV","-AV",inplace=True)
df_sap["DOKVR"].replace("AW","-AW",inplace=True)
df_sap["DOKVR"].replace("AX","-AX",inplace=True)
df_sap["DOKVR"].replace("AY","-AY",inplace=True)
df_sap["DOKVR"].replace("AZ","-AZ",inplace=True)
df_sap["DOKVR"].replace("BA","-BA",inplace=True)
df_sap["DOKVR"].replace("BB","-BB",inplace=True)
df_sap["DOKVR"].replace("BC","-BC",inplace=True)
df_sap["DOKVR"].replace("BD","-BD",inplace=True)
df_sap["DOKVR"].replace("BE","-BE",inplace=True)
df_sap["DOKVR"].replace("BF","-BF",inplace=True)
df_sap["DOKVR"].replace("BG","-BG",inplace=True)
df_sap["DOKVR"].replace("BH","-BH",inplace=True)
df_sap["DOKVR"].replace("BI","-BI",inplace=True)
df_sap["DOKVR"].replace("BJ","-BJ",inplace=True)
df_sap["DOKVR"].replace("BK","-BK",inplace=True)
df_sap["DOKVR"].replace("BL","-BL",inplace=True)
df_sap["DOKVR"].replace("BM","-BM",inplace=True)
df_sap["DOKVR"].replace("BN","-BN",inplace=True)
df_sap["DOKVR"].replace("BO","-BO",inplace=True)
df_sap["DOKVR"].replace("BP","-BP",inplace=True)
df_sap["DOKVR"].replace("BQ","-BQ",inplace=True)
df_sap["DOKVR"].replace("BR","-BR",inplace=True)
df_sap["DOKVR"].replace("BS","-BS",inplace=True)
df_sap["DOKVR"].replace("BT","-BT",inplace=True)
df_sap["DOKVR"].replace("BU","-BU",inplace=True)
df_sap["DOKVR"].replace("BV","-BV",inplace=True)
df_sap["DOKVR"].replace("BW","-BW",inplace=True)
df_sap["DOKVR"].replace("BX","-BX",inplace=True)
df_sap["DOKVR"].replace("BY","-BY",inplace=True)
df_sap["DOKVR"].replace("BZ","-BZ",inplace=True)
df_sap["DOKVR"].replace("CA","-CA",inplace=True)
df_sap["DOKVR"].replace("CB","-CB",inplace=True)
df_sap["DOKVR"].replace("CC","-CC",inplace=True)
df_sap["DOKVR"].replace("CD","-CD",inplace=True)
df_sap["DOKVR"].replace("CE","-CE",inplace=True)
df_sap["DOKVR"].replace("CF","-CF",inplace=True)
df_sap["DOKVR"].replace("CG","-CG",inplace=True)
df_sap["DOKVR"].replace("CH","-CH",inplace=True)
df_sap["DOKVR"].replace("CI","-CI",inplace=True)
df_sap["DOKVR"].replace("CJ","-CJ",inplace=True)
df_sap["DOKVR"].replace("CK","-CK",inplace=True)
df_sap["DOKVR"].replace("CL","-CL",inplace=True)
df_sap["DOKVR"].replace("CM","-CM",inplace=True)
df_sap["DOKVR"].replace("CN","-CN",inplace=True)
df_sap["DOKVR"].replace("CO","-CO",inplace=True)
df_sap["DOKVR"].replace("CP","-CP",inplace=True)
df_sap["DOKVR"].replace("CQ","-CQ",inplace=True)
df_sap["DOKVR"].replace("CR","-CR",inplace=True)
df_sap["DOKVR"].replace("CS","-CS",inplace=True)
df_sap["DOKVR"].replace("CT","-CT",inplace=True)
df_sap["DOKVR"].replace("CU","-CU",inplace=True)
df_sap["DOKVR"].replace("CV","-CV",inplace=True)
df_sap["DOKVR"].replace("CW","-CW",inplace=True)
df_sap["DOKVR"].replace("CX","-CX",inplace=True)
df_sap["DOKVR"].replace("CY","-CY",inplace=True)
df_sap["DOKVR"].replace("CZ","-CZ",inplace=True)
df_sap["DOKVR"].replace("DA","-DA",inplace=True)
df_sap["DOKVR"].replace("DB","-DB",inplace=True)
df_sap["DOKVR"].replace("DC","-DC",inplace=True)
df_sap["DOKVR"].replace("DD","-DD",inplace=True)
df_sap["DOKVR"].replace("DE","-DE",inplace=True)
df_sap["DOKVR"].replace("DF","-DF",inplace=True)
df_sap["DOKVR"].replace("DG","-DG",inplace=True)
df_sap["DOKVR"].replace("DH","-DH",inplace=True)
df_sap["DOKVR"].replace("DI","-DI",inplace=True)
df_sap["DOKVR"].replace("DJ","-DJ",inplace=True)
df_sap["DOKVR"].replace("DK","-DK",inplace=True)
df_sap["DOKVR"].replace("DL","-DL",inplace=True)
df_sap["DOKVR"].replace("DM","-DM",inplace=True)
df_sap["DOKVR"].replace("DN","-DN",inplace=True)
df_sap["DOKVR"].replace("DO","-DO",inplace=True)
df_sap["DOKVR"].replace("DP","-DP",inplace=True)
df_sap["DOKVR"].replace("DQ","-DQ",inplace=True)
df_sap["DOKVR"].replace("DR","-DR",inplace=True)
df_sap["DOKVR"].replace("DS","-DS",inplace=True)
df_sap["DOKVR"].replace("DT","-DT",inplace=True)
df_sap["DOKVR"].replace("DU","-DU",inplace=True)
df_sap["DOKVR"].replace("DV","-DV",inplace=True)
df_sap["DOKVR"].replace("DW","-DW",inplace=True)
df_sap["DOKVR"].replace("DX","-DX",inplace=True)
df_sap["DOKVR"].replace("DY","-DY",inplace=True)
df_sap["DOKVR"].replace("DZ","-DZ",inplace=True)
df_sap["DOKVR"].replace("EA","-EA",inplace=True)
df_sap["DOKVR"].replace("EB","-EB",inplace=True)
df_sap["DOKVR"].replace("EC","-EC",inplace=True)
df_sap["DOKVR"].replace("ED","-ED",inplace=True)
df_sap["DOKVR"].replace("EE","-EE",inplace=True)
df_sap["DOKVR"].replace("EF","-EF",inplace=True)
df_sap["DOKVR"].replace("EG","-EG",inplace=True)
df_sap["DOKVR"].replace("EH","-EH",inplace=True)
df_sap["DOKVR"].replace("EI","-EI",inplace=True)
df_sap["DOKVR"].replace("EJ","-EJ",inplace=True)
df_sap["DOKVR"].replace("EK","-EK",inplace=True)
df_sap["DOKVR"].replace("EL","-EL",inplace=True)
df_sap["DOKVR"].replace("EM","-EM",inplace=True)
df_sap["DOKVR"].replace("EN","-EN",inplace=True)
df_sap["DOKVR"].replace("EO","-EO",inplace=True)
df_sap["DOKVR"].replace("EP","-EP",inplace=True)
df_sap["DOKVR"].replace("EQ","-EQ",inplace=True)
df_sap["DOKVR"].replace("ER","-ER",inplace=True)
df_sap["DOKVR"].replace("ES","-ES",inplace=True)
df_sap["DOKVR"].replace("ET","-ET",inplace=True)
df_sap["DOKVR"].replace("EU","-EU",inplace=True)
df_sap["DOKVR"].replace("EV","-EV",inplace=True)
df_sap["DOKVR"].replace("EW","-EW",inplace=True)
df_sap["DOKVR"].replace("EX","-EX",inplace=True)
df_sap["DOKVR"].replace("EY","-EY",inplace=True)
df_sap["DOKVR"].replace("EZ","-EZ",inplace=True)
df_sap["DOKVR"].replace("FA","-FA",inplace=True)
df_sap["DOKVR"].replace("FB","-FB",inplace=True)
df_sap["DOKVR"].replace("FC","-FC",inplace=True)
df_sap["DOKVR"].replace("FD","-FD",inplace=True)
df_sap["DOKVR"].replace("FE","-FE",inplace=True)
df_sap["DOKVR"].replace("FF","-FF",inplace=True)
df_sap["DOKVR"].replace("FG","-FG",inplace=True)
df_sap["DOKVR"].replace("FH","-FH",inplace=True)
df_sap["DOKVR"].replace("FI","-FI",inplace=True)
df_sap["DOKVR"].replace("FJ","-FJ",inplace=True)
df_sap["DOKVR"].replace("FK","-FK",inplace=True)
df_sap["DOKVR"].replace("FL","-FL",inplace=True)
df_sap["DOKVR"].replace("FM","-FM",inplace=True)
df_sap["DOKVR"].replace("FN","-FN",inplace=True)
df_sap["DOKVR"].replace("FO","-FO",inplace=True)
df_sap["DOKVR"].replace("FP","-FP",inplace=True)
df_sap["DOKVR"].replace("FQ","-FQ",inplace=True)
df_sap["DOKVR"].replace("FR","-FR",inplace=True)
df_sap["DOKVR"].replace("FS","-FS",inplace=True)
df_sap["DOKVR"].replace("FT","-FT",inplace=True)
df_sap["DOKVR"].replace("FU","-FU",inplace=True)
df_sap["DOKVR"].replace("FV","-FV",inplace=True)
df_sap["DOKVR"].replace("FW","-FW",inplace=True)
df_sap["DOKVR"].replace("FX","-FX",inplace=True)
df_sap["DOKVR"].replace("FY","-FY",inplace=True)
df_sap["DOKVR"].replace("FZ","-FZ",inplace=True)
df_sap["DOKVR"].replace("GA","-GA",inplace=True)
df_sap["DOKVR"].replace("GB","-GB",inplace=True)
df_sap["DOKVR"].replace("GC","-GC",inplace=True)
df_sap["DOKVR"].replace("GD","-GD",inplace=True)
df_sap["DOKVR"].replace("GE","-GE",inplace=True)
df_sap["DOKVR"].replace("GF","-GF",inplace=True)
df_sap["DOKVR"].replace("GG","-GG",inplace=True)
df_sap["DOKVR"].replace("GH","-GH",inplace=True)
df_sap["DOKVR"].replace("GI","-GI",inplace=True)
df_sap["DOKVR"].replace("GJ","-GJ",inplace=True)
df_sap["DOKVR"].replace("GK","-GK",inplace=True)
df_sap["DOKVR"].replace("GL","-GL",inplace=True)
df_sap["DOKVR"].replace("GM","-GM",inplace=True)
df_sap["DOKVR"].replace("GN","-GN",inplace=True)
df_sap["DOKVR"].replace("GO","-GO",inplace=True)
df_sap["DOKVR"].replace("GP","-GP",inplace=True)
df_sap["DOKVR"].replace("GQ","-GQ",inplace=True)
df_sap["DOKVR"].replace("GR","-GR",inplace=True)
df_sap["DOKVR"].replace("GS","-GS",inplace=True)
df_sap["DOKVR"].replace("GT","-GT",inplace=True)
df_sap["DOKVR"].replace("GU","-GU",inplace=True)
df_sap["DOKVR"].replace("GV","-GV",inplace=True)
df_sap["DOKVR"].replace("GW","-GW",inplace=True)
df_sap["DOKVR"].replace("GX","-GX",inplace=True)
df_sap["DOKVR"].replace("GY","-GY",inplace=True)
df_sap["DOKVR"].replace("GZ","-GZ",inplace=True)
df_sap["DOKVR"].replace("HA","-HA",inplace=True)
df_sap["DOKVR"].replace("HB","-HB",inplace=True)
df_sap["DOKVR"].replace("HC","-HC",inplace=True)
df_sap["DOKVR"].replace("HD","-HD",inplace=True)
df_sap["DOKVR"].replace("HE","-HE",inplace=True)
df_sap["DOKVR"].replace("HF","-HF",inplace=True)
df_sap["DOKVR"].replace("HG","-HG",inplace=True)
df_sap["DOKVR"].replace("HH","-HH",inplace=True)
df_sap["DOKVR"].replace("HI","-HI",inplace=True)
df_sap["DOKVR"].replace("HJ","-HJ",inplace=True)
df_sap["DOKVR"].replace("HK","-HK",inplace=True)
df_sap["DOKVR"].replace("HL","-HL",inplace=True)
df_sap["DOKVR"].replace("HM","-HM",inplace=True)
df_sap["DOKVR"].replace("HN","-HN",inplace=True)
df_sap["DOKVR"].replace("HO","-HO",inplace=True)
df_sap["DOKVR"].replace("HP","-HP",inplace=True)
df_sap["DOKVR"].replace("HQ","-HQ",inplace=True)
df_sap["DOKVR"].replace("HR","-HR",inplace=True)
df_sap["DOKVR"].replace("HS","-HS",inplace=True)
df_sap["DOKVR"].replace("HT","-HT",inplace=True)
df_sap["DOKVR"].replace("HU","-HU",inplace=True)
df_sap["DOKVR"].replace("HV","-HV",inplace=True)
df_sap["DOKVR"].replace("HW","-HW",inplace=True)
df_sap["DOKVR"].replace("HX","-HX",inplace=True)
df_sap["DOKVR"].replace("HY","-HY",inplace=True)
df_sap["DOKVR"].replace("HZ","-HZ",inplace=True)
df_sap["DOKVR"].replace("IA","-IA",inplace=True)
df_sap["DOKVR"].replace("IB","-IB",inplace=True)
df_sap["DOKVR"].replace("IC","-IC",inplace=True)
df_sap["DOKVR"].replace("ID","-ID",inplace=True)
df_sap["DOKVR"].replace("IE","-IE",inplace=True)
df_sap["DOKVR"].replace("IF","-IF",inplace=True)
df_sap["DOKVR"].replace("IG","-IG",inplace=True)
df_sap["DOKVR"].replace("IH","-IH",inplace=True)
df_sap["DOKVR"].replace("II","-II",inplace=True)
df_sap["DOKVR"].replace("IJ","-IJ",inplace=True)
df_sap["DOKVR"].replace("IK","-IK",inplace=True)
df_sap["DOKVR"].replace("IL","-IL",inplace=True)
df_sap["DOKVR"].replace("IM","-IM",inplace=True)
df_sap["DOKVR"].replace("IN","-IN",inplace=True)
df_sap["DOKVR"].replace("IO","-IO",inplace=True)
df_sap["DOKVR"].replace("IP","-IP",inplace=True)
df_sap["DOKVR"].replace("IQ","-IQ",inplace=True)
df_sap["DOKVR"].replace("IR","-IR",inplace=True)
df_sap["DOKVR"].replace("IS","-IS",inplace=True)
df_sap["DOKVR"].replace("IT","-IT",inplace=True)
df_sap["DOKVR"].replace("IU","-IU",inplace=True)
df_sap["DOKVR"].replace("IV","-IV",inplace=True)
df_sap["DOKVR"].replace("IW","-IW",inplace=True)
df_sap["DOKVR"].replace("IX","-IX",inplace=True)
df_sap["DOKVR"].replace("IY","-IY",inplace=True)
df_sap["DOKVR"].replace("IZ","-IZ",inplace=True)
df_sap["DOKVR"].replace("JA","-JA",inplace=True)
df_sap["DOKVR"].replace("JB","-JB",inplace=True)
df_sap["DOKVR"].replace("JC","-JC",inplace=True)
df_sap["DOKVR"].replace("JD","-JD",inplace=True)
df_sap["DOKVR"].replace("JE","-JE",inplace=True)
df_sap["DOKVR"].replace("JF","-JF",inplace=True)
df_sap["DOKVR"].replace("JG","-JG",inplace=True)
df_sap["DOKVR"].replace("JH","-JH",inplace=True)
df_sap["DOKVR"].replace("JI","-JI",inplace=True)
df_sap["DOKVR"].replace("JJ","-JJ",inplace=True)
df_sap["DOKVR"].replace("JK","-JK",inplace=True)
df_sap["DOKVR"].replace("JL","-JL",inplace=True)
df_sap["DOKVR"].replace("JM","-JM",inplace=True)
df_sap["DOKVR"].replace("JN","-JN",inplace=True)
df_sap["DOKVR"].replace("JO","-JO",inplace=True)
df_sap["DOKVR"].replace("JP","-JP",inplace=True)
df_sap["DOKVR"].replace("JQ","-JQ",inplace=True)
df_sap["DOKVR"].replace("JR","-JR",inplace=True)
df_sap["DOKVR"].replace("JS","-JS",inplace=True)
df_sap["DOKVR"].replace("JT","-JT",inplace=True)
df_sap["DOKVR"].replace("JU","-JU",inplace=True)
df_sap["DOKVR"].replace("JV","-JV",inplace=True)
df_sap["DOKVR"].replace("JW","-JW",inplace=True)
df_sap["DOKVR"].replace("JX","-JX",inplace=True)
df_sap["DOKVR"].replace("JY","-JY",inplace=True)
df_sap["DOKVR"].replace("JZ","-JZ",inplace=True)
df_sap["DOKVR"].replace("KA","-KA",inplace=True)
df_sap["DOKVR"].replace("KB","-KB",inplace=True)
df_sap["DOKVR"].replace("KC","-KC",inplace=True)
df_sap["DOKVR"].replace("KD","-KD",inplace=True)
df_sap["DOKVR"].replace("KE","-KE",inplace=True)
df_sap["DOKVR"].replace("KF","-KF",inplace=True)
df_sap["DOKVR"].replace("KG","-KG",inplace=True)
df_sap["DOKVR"].replace("KH","-KH",inplace=True)
df_sap["DOKVR"].replace("KI","-KI",inplace=True)
df_sap["DOKVR"].replace("KJ","-KJ",inplace=True)
df_sap["DOKVR"].replace("KK","-KK",inplace=True)
df_sap["DOKVR"].replace("KL","-KL",inplace=True)
df_sap["DOKVR"].replace("KM","-KM",inplace=True)
df_sap["DOKVR"].replace("KN","-KN",inplace=True)
df_sap["DOKVR"].replace("KO","-KO",inplace=True)
df_sap["DOKVR"].replace("KP","-KP",inplace=True)
df_sap["DOKVR"].replace("KQ","-KQ",inplace=True)
df_sap["DOKVR"].replace("KR","-KR",inplace=True)
df_sap["DOKVR"].replace("KS","-KS",inplace=True)
df_sap["DOKVR"].replace("KT","-KT",inplace=True)
df_sap["DOKVR"].replace("KU","-KU",inplace=True)
df_sap["DOKVR"].replace("KV","-KV",inplace=True)
df_sap["DOKVR"].replace("KW","-KW",inplace=True)
df_sap["DOKVR"].replace("KX","-KX",inplace=True)
df_sap["DOKVR"].replace("KY","-KY",inplace=True)
df_sap["DOKVR"].replace("KZ","-KZ",inplace=True)
df_sap["DOKVR"].replace("LA","-LA",inplace=True)
df_sap["DOKVR"].replace("LB","-LB",inplace=True)
df_sap["DOKVR"].replace("LC","-LC",inplace=True)
df_sap["DOKVR"].replace("LD","-LD",inplace=True)
df_sap["DOKVR"].replace("LE","-LE",inplace=True)
df_sap["DOKVR"].replace("LF","-LF",inplace=True)
df_sap["DOKVR"].replace("LG","-LG",inplace=True)
df_sap["DOKVR"].replace("LH","-LH",inplace=True)
df_sap["DOKVR"].replace("LI","-LI",inplace=True)
df_sap["DOKVR"].replace("LJ","-LJ",inplace=True)
df_sap["DOKVR"].replace("LK","-LK",inplace=True)
df_sap["DOKVR"].replace("LL","-LL",inplace=True)
df_sap["DOKVR"].replace("LM","-LM",inplace=True)
df_sap["DOKVR"].replace("LN","-LN",inplace=True)
df_sap["DOKVR"].replace("LO","-LO",inplace=True)
df_sap["DOKVR"].replace("LP","-LP",inplace=True)
df_sap["DOKVR"].replace("LQ","-LQ",inplace=True)
df_sap["DOKVR"].replace("LR","-LR",inplace=True)
df_sap["DOKVR"].replace("LS","-LS",inplace=True)
df_sap["DOKVR"].replace("LT","-LT",inplace=True)
df_sap["DOKVR"].replace("LU","-LU",inplace=True)
df_sap["DOKVR"].replace("LV","-LV",inplace=True)
df_sap["DOKVR"].replace("LW","-LW",inplace=True)
df_sap["DOKVR"].replace("LX","-LX",inplace=True)
df_sap["DOKVR"].replace("LY","-LY",inplace=True)
df_sap["DOKVR"].replace("LZ","-LZ",inplace=True)
df_sap["DOKVR"].replace("MA","-MA",inplace=True)
df_sap["DOKVR"].replace("MB","-MB",inplace=True)
df_sap["DOKVR"].replace("MC","-MC",inplace=True)
df_sap["DOKVR"].replace("MD","-MD",inplace=True)
df_sap["DOKVR"].replace("ME","-ME",inplace=True)
df_sap["DOKVR"].replace("MF","-MF",inplace=True)
df_sap["DOKVR"].replace("MG","-MG",inplace=True)
df_sap["DOKVR"].replace("MH","-MH",inplace=True)
df_sap["DOKVR"].replace("MI","-MI",inplace=True)
df_sap["DOKVR"].replace("MJ","-MJ",inplace=True)
df_sap["DOKVR"].replace("MK","-MK",inplace=True)
df_sap["DOKVR"].replace("ML","-ML",inplace=True)
df_sap["DOKVR"].replace("MM","-MM",inplace=True)
df_sap["DOKVR"].replace("MN","-MN",inplace=True)
df_sap["DOKVR"].replace("MO","-MO",inplace=True)
df_sap["DOKVR"].replace("MP","-MP",inplace=True)
df_sap["DOKVR"].replace("MQ","-MQ",inplace=True)
df_sap["DOKVR"].replace("MR","-MR",inplace=True)
df_sap["DOKVR"].replace("MS","-MS",inplace=True)
df_sap["DOKVR"].replace("MT","-MT",inplace=True)
df_sap["DOKVR"].replace("MU","-MU",inplace=True)
df_sap["DOKVR"].replace("MV","-MV",inplace=True)
df_sap["DOKVR"].replace("MW","-MW",inplace=True)
df_sap["DOKVR"].replace("MX","-MX",inplace=True)
df_sap["DOKVR"].replace("MY","-MY",inplace=True)
df_sap["DOKVR"].replace("MZ","-MZ",inplace=True)
df_sap["DOKVR"].replace("NA","-NA",inplace=True)
df_sap["DOKVR"].replace("NB","-NB",inplace=True)
df_sap["DOKVR"].replace("NC","-NC",inplace=True)
df_sap["DOKVR"].replace("ND","-ND",inplace=True)
df_sap["DOKVR"].replace("NE","-NE",inplace=True)
df_sap["DOKVR"].replace("NF","-NF",inplace=True)
df_sap["DOKVR"].replace("NG","-NG",inplace=True)
df_sap["DOKVR"].replace("NH","-NH",inplace=True)
df_sap["DOKVR"].replace("NI","-NI",inplace=True)
df_sap["DOKVR"].replace("NJ","-NJ",inplace=True)
df_sap["DOKVR"].replace("NK","-NK",inplace=True)
df_sap["DOKVR"].replace("NL","-NL",inplace=True)
df_sap["DOKVR"].replace("NM","-NM",inplace=True)
df_sap["DOKVR"].replace("NN","-NN",inplace=True)
df_sap["DOKVR"].replace("NO","-NO",inplace=True)
df_sap["DOKVR"].replace("NP","-NP",inplace=True)
df_sap["DOKVR"].replace("NQ","-NQ",inplace=True)
df_sap["DOKVR"].replace("NR","-NR",inplace=True)
df_sap["DOKVR"].replace("NS","-NS",inplace=True)
df_sap["DOKVR"].replace("NT","-NT",inplace=True)
df_sap["DOKVR"].replace("NU","-NU",inplace=True)
df_sap["DOKVR"].replace("NV","-NV",inplace=True)
df_sap["DOKVR"].replace("NW","-NW",inplace=True)
df_sap["DOKVR"].replace("NX","-NX",inplace=True)
df_sap["DOKVR"].replace("NY","-NY",inplace=True)
df_sap["DOKVR"].replace("NZ","-NZ",inplace=True)
df_sap["DOKVR"].replace("OA","-OA",inplace=True)
df_sap["DOKVR"].replace("OB","-OB",inplace=True)
df_sap["DOKVR"].replace("OC","-OC",inplace=True)
df_sap["DOKVR"].replace("OD","-OD",inplace=True)
df_sap["DOKVR"].replace("OE","-OE",inplace=True)
df_sap["DOKVR"].replace("OF","-OF",inplace=True)
df_sap["DOKVR"].replace("OG","-OG",inplace=True)
df_sap["DOKVR"].replace("OH","-OH",inplace=True)
df_sap["DOKVR"].replace("OI","-OI",inplace=True)
df_sap["DOKVR"].replace("OJ","-OJ",inplace=True)
df_sap["DOKVR"].replace("OK","-OK",inplace=True)
df_sap["DOKVR"].replace("OL","-OL",inplace=True)
df_sap["DOKVR"].replace("OM","-OM",inplace=True)
df_sap["DOKVR"].replace("ON","-ON",inplace=True)
df_sap["DOKVR"].replace("OO","-OO",inplace=True)
df_sap["DOKVR"].replace("OP","-OP",inplace=True)
df_sap["DOKVR"].replace("OQ","-OQ",inplace=True)
df_sap["DOKVR"].replace("OR","-OR",inplace=True)
df_sap["DOKVR"].replace("OS","-OS",inplace=True)
df_sap["DOKVR"].replace("OT","-OT",inplace=True)
df_sap["DOKVR"].replace("OU","-OU",inplace=True)
df_sap["DOKVR"].replace("OV","-OV",inplace=True)
df_sap["DOKVR"].replace("OW","-OW",inplace=True)
df_sap["DOKVR"].replace("OX","-OX",inplace=True)
df_sap["DOKVR"].replace("OY","-OY",inplace=True)
df_sap["DOKVR"].replace("OZ","-OZ",inplace=True)
df_sap["DOKVR"].replace("PA","-PA",inplace=True)
df_sap["DOKVR"].replace("PB","-PB",inplace=True)
df_sap["DOKVR"].replace("PC","-PC",inplace=True)
df_sap["DOKVR"].replace("PD","-PD",inplace=True)
df_sap["DOKVR"].replace("PE","-PE",inplace=True)
df_sap["DOKVR"].replace("PF","-PF",inplace=True)
df_sap["DOKVR"].replace("PG","-PG",inplace=True)
df_sap["DOKVR"].replace("PH","-PH",inplace=True)
df_sap["DOKVR"].replace("PI","-PI",inplace=True)
df_sap["DOKVR"].replace("PJ","-PJ",inplace=True)
df_sap["DOKVR"].replace("PK","-PK",inplace=True)
df_sap["DOKVR"].replace("PL","-PL",inplace=True)
df_sap["DOKVR"].replace("PM","-PM",inplace=True)
df_sap["DOKVR"].replace("PN","-PN",inplace=True)
df_sap["DOKVR"].replace("PO","-PO",inplace=True)
df_sap["DOKVR"].replace("PP","-PP",inplace=True)
df_sap["DOKVR"].replace("PQ","-PQ",inplace=True)
df_sap["DOKVR"].replace("PR","-PR",inplace=True)
df_sap["DOKVR"].replace("PS","-PS",inplace=True)
df_sap["DOKVR"].replace("PT","-PT",inplace=True)
df_sap["DOKVR"].replace("PU","-PU",inplace=True)
df_sap["DOKVR"].replace("PV","-PV",inplace=True)
df_sap["DOKVR"].replace("PW","-PW",inplace=True)
df_sap["DOKVR"].replace("PX","-PX",inplace=True)
df_sap["DOKVR"].replace("PY","-PY",inplace=True)
df_sap["DOKVR"].replace("PZ","-PZ",inplace=True)
df_sap["DOKVR"].replace("QA","-QA",inplace=True)
df_sap["DOKVR"].replace("QB","-QB",inplace=True)
df_sap["DOKVR"].replace("QC","-QC",inplace=True)
df_sap["DOKVR"].replace("QD","-QD",inplace=True)
df_sap["DOKVR"].replace("QE","-QE",inplace=True)
df_sap["DOKVR"].replace("QF","-QF",inplace=True)
df_sap["DOKVR"].replace("QG","-QG",inplace=True)
df_sap["DOKVR"].replace("QH","-QH",inplace=True)
df_sap["DOKVR"].replace("QI","-QI",inplace=True)
df_sap["DOKVR"].replace("QJ","-QJ",inplace=True)
df_sap["DOKVR"].replace("QK","-QK",inplace=True)
df_sap["DOKVR"].replace("QL","-QL",inplace=True)
df_sap["DOKVR"].replace("QM","-QM",inplace=True)
df_sap["DOKVR"].replace("QN","-QN",inplace=True)
df_sap["DOKVR"].replace("QO","-QO",inplace=True)
df_sap["DOKVR"].replace("QP","-QP",inplace=True)
df_sap["DOKVR"].replace("QQ","-QQ",inplace=True)
df_sap["DOKVR"].replace("QR","-QR",inplace=True)
df_sap["DOKVR"].replace("QS","-QS",inplace=True)
df_sap["DOKVR"].replace("QT","-QT",inplace=True)
df_sap["DOKVR"].replace("QU","-QU",inplace=True)
df_sap["DOKVR"].replace("QV","-QV",inplace=True)
df_sap["DOKVR"].replace("QW","-QW",inplace=True)
df_sap["DOKVR"].replace("QX","-QX",inplace=True)
df_sap["DOKVR"].replace("QY","-QY",inplace=True)
df_sap["DOKVR"].replace("QZ","-QZ",inplace=True)
df_sap["DOKVR"].replace("RA","-RA",inplace=True)
df_sap["DOKVR"].replace("RB","-RB",inplace=True)
df_sap["DOKVR"].replace("RC","-RC",inplace=True)
df_sap["DOKVR"].replace("RD","-RD",inplace=True)
df_sap["DOKVR"].replace("RE","-RE",inplace=True)
df_sap["DOKVR"].replace("RF","-RF",inplace=True)
df_sap["DOKVR"].replace("RG","-RG",inplace=True)
df_sap["DOKVR"].replace("RH","-RH",inplace=True)
df_sap["DOKVR"].replace("RI","-RI",inplace=True)
df_sap["DOKVR"].replace("RJ","-RJ",inplace=True)
df_sap["DOKVR"].replace("RK","-RK",inplace=True)
df_sap["DOKVR"].replace("RL","-RL",inplace=True)
df_sap["DOKVR"].replace("RM","-RM",inplace=True)
df_sap["DOKVR"].replace("RN","-RN",inplace=True)
df_sap["DOKVR"].replace("RO","-RO",inplace=True)
df_sap["DOKVR"].replace("RP","-RP",inplace=True)
df_sap["DOKVR"].replace("RQ","-RQ",inplace=True)
df_sap["DOKVR"].replace("RR","-RR",inplace=True)
df_sap["DOKVR"].replace("RS","-RS",inplace=True)
df_sap["DOKVR"].replace("RT","-RT",inplace=True)
df_sap["DOKVR"].replace("RU","-RU",inplace=True)
df_sap["DOKVR"].replace("RV","-RV",inplace=True)
df_sap["DOKVR"].replace("RW","-RW",inplace=True)
df_sap["DOKVR"].replace("RX","-RX",inplace=True)
df_sap["DOKVR"].replace("RY","-RY",inplace=True)
df_sap["DOKVR"].replace("RZ","-RZ",inplace=True)
df_sap["DOKVR"].replace("SA","-SA",inplace=True)
df_sap["DOKVR"].replace("SB","-SB",inplace=True)
df_sap["DOKVR"].replace("SC","-SC",inplace=True)
df_sap["DOKVR"].replace("SD","-SD",inplace=True)
df_sap["DOKVR"].replace("SE","-SE",inplace=True)
df_sap["DOKVR"].replace("SF","-SF",inplace=True)
df_sap["DOKVR"].replace("SG","-SG",inplace=True)
df_sap["DOKVR"].replace("SH","-SH",inplace=True)
df_sap["DOKVR"].replace("SI","-SI",inplace=True)
df_sap["DOKVR"].replace("SJ","-SJ",inplace=True)
df_sap["DOKVR"].replace("SK","-SK",inplace=True)
df_sap["DOKVR"].replace("SL","-SL",inplace=True)
df_sap["DOKVR"].replace("SM","-SM",inplace=True)
df_sap["DOKVR"].replace("SN","-SN",inplace=True)
df_sap["DOKVR"].replace("SO","-SO",inplace=True)
df_sap["DOKVR"].replace("SP","-SP",inplace=True)
df_sap["DOKVR"].replace("SQ","-SQ",inplace=True)
df_sap["DOKVR"].replace("SR","-SR",inplace=True)
df_sap["DOKVR"].replace("SS","-SS",inplace=True)
df_sap["DOKVR"].replace("ST","-ST",inplace=True)
df_sap["DOKVR"].replace("SU","-SU",inplace=True)
df_sap["DOKVR"].replace("SV","-SV",inplace=True)
df_sap["DOKVR"].replace("SW","-SW",inplace=True)
df_sap["DOKVR"].replace("SX","-SX",inplace=True)
df_sap["DOKVR"].replace("SY","-SY",inplace=True)
df_sap["DOKVR"].replace("SZ","-SZ",inplace=True)



    # Concatenar PN com Letra de Revisão.
df_sap['FullPN']=df_sap.MFRPN.str.cat(df_sap['DOKVR'],'')

    # Renomear colunas.
df_sap = df_sap.rename(columns={'TIPO_DOC_GRD':'DOCUMENTO_DE_MODIFICACAO'})
df_sap = df_sap.rename(columns={'NUM_DOC_GRD':'NUMERO_DOCUMENTO_DE_MODIFICACAO'})
df_sap = df_sap.rename(columns={'IND_STAT_PN':'STATUS_SAP_PN'})
df_sap = df_sap.rename(columns={'EXP_DATE':'DATA_PREVISTA'})

# Formatação de data

    # Alterando data 00000000 para 20010101
        # Localizar e substituir.
df_sap['DATA_PREVISTA'].replace('00000000','20010101',inplace=True)
df_sap['DATA_PREVISTA'].replace('EXP_DATE','20010101',inplace=True)
df_sap['DATA_PREVISTA'].replace('30130903','20010101',inplace=True)

        # Algum dado está com o timestamp fora do range coberto pelo python, sendo assim o dado não é válido e a função
        #abaixo elimina esse dado da base.
df_sap['DATA_PREVISTA'] = pd.to_datetime(df_sap['DATA_PREVISTA'], errors = 'coerce')

        # Formatar a string para ano, mes e dia.
df_sap['DATA_PREVISTA_FORMATADA'] = pd.to_datetime(df_sap['DATA_PREVISTA'], format='%Y%m%d')

    # Filtrar os status desejados.
df_sap = df_sap[df_sap.STATUS_SAP_PN != 'CANC']

    # Remove colunas sem utilidade.
df_sap = df_sap[['FullPN', 'DOCUMENTO_DE_MODIFICACAO', 'NUMERO_DOCUMENTO_DE_MODIFICACAO', 'STATUS_SAP_PN', 'DATA_PREVISTA_FORMATADA']]

    # Remover informações com data menor que 2015-01-01.
df_sap = df_sap[df_sap.DATA_PREVISTA_FORMATADA >= '2015-01-01']

    # Filtra OE com iniciais 170, 190.
df_sap  = df_sap.loc[(df_sap['NUMERO_DOCUMENTO_DE_MODIFICACAO'].str.startswith('170', na=False))|(df_sap['NUMERO_DOCUMENTO_DE_MODIFICACAO'].str.startswith('190', na=False))]

    # Exportar planilha SAP.
df_sap.to_csv('df_sap_fullpn.txt', sep=';')






# - - - - - - - - 3DCOM E1-170 - - - - - - - -- - - - - - - - 3DCOM E1-170 - - - - - - - -- - - - - - 3DCOM E1-170 - -

    # Abrir a base de dados do 3DCOM (VPM_VISIB_REL-PART-E170ENG.csv)
df_e170_vpm = pd.read_csv(r'C:\Users\grizzi\05-PycharmProjects\LiberacaoPNs\ActionList170.txt', sep=' ', encoding='utf-8', low_memory=False)

    # Separar os dados contidos em uma única coluna.
df_e170_vpm_split = df_e170_vpm['Action'].str.split()

    # Exportar a base organizada para um novo arquivo txt.
df_e170_vpm_split.to_csv('df_e170_splited.txt', sep=';')

    # Importar a base organizada.
df_e170_vpm_1 = pd.read_csv(r'C:\Users\grizzi\05-PycharmProjects\LiberacaoPNs\df_e170_splited.txt', sep=' ', encoding='utf-8', low_memory=False)

    # Renomear as colunas.
df_e170_vpm_1.columns = ['Action Id', 'Action Priority', 'Action Owner', 'Action Start Date', 'Action End Date', 'Action Status', 'Action Description', 'Action Type', 'Part Number', 'Part Instance', 'Part Conc Version', 'Part Version', 'Part Responsible', 'Part Org Responsible', 'Part Type', 'Part Origin', 'Part Design', 'Part Production', 'Irrelevante']

    # Remover digitos sem utililidades nas colunas
df_e170_vpm_1['Part Number'] = df_e170_vpm_1['Part Number'].str.replace("'", "")

df_e170_vpm_1['Action Owner'] = df_e170_vpm_1['Action Owner'].str.replace("'", "")
df_e170_vpm_1['Action Owner'] = df_e170_vpm_1['Action Owner'].str.replace(",", "")

df_e170_vpm_1['Action Start Date'] = df_e170_vpm_1['Action Start Date'].str.replace("'", "")
df_e170_vpm_1['Action Start Date'] = df_e170_vpm_1['Action Start Date'].str.replace(",", "")

df_e170_vpm_1['Action End Date'] = df_e170_vpm_1['Action End Date'].str.replace("'", "")
df_e170_vpm_1['Action End Date'] = df_e170_vpm_1['Action End Date'].str.replace(",", "")

df_e170_vpm_1['Action Status'] = df_e170_vpm_1['Action Status'].str.replace("'", "")
df_e170_vpm_1['Action Status'] = df_e170_vpm_1['Action Status'].str.replace(",", "")

df_e170_vpm_1['Action Description'] = df_e170_vpm_1['Action Description'].str.replace("'", "")
df_e170_vpm_1['Action Description'] = df_e170_vpm_1['Action Description'].str.replace(",", "")

df_e170_vpm_1['Action Type'] = df_e170_vpm_1['Action Type'].str.replace("'", "")
df_e170_vpm_1['Action Type'] = df_e170_vpm_1['Action Type'].str.replace(",", "")

df_e170_vpm_1['Part Responsible'] = df_e170_vpm_1['Part Responsible'].str.replace("'", "")
df_e170_vpm_1['Part Responsible'] = df_e170_vpm_1['Part Responsible'].str.replace(",", "")

df_e170_vpm_1['Part Org Responsible'] = df_e170_vpm_1['Part Org Responsible'].str.replace("'", "")
df_e170_vpm_1['Part Org Responsible'] = df_e170_vpm_1['Part Org Responsible'].str.replace(",", "")

df_e170_vpm_1['Action Owner'] = df_e170_vpm_1['Action Owner'].str.replace("'", "")
df_e170_vpm_1['Action Owner'] = df_e170_vpm_1['Action Owner'].str.replace(",", "")

df_e170_vpm_1['Part Design'] = df_e170_vpm_1['Part Design'].str.replace("'", "")
df_e170_vpm_1['Part Design'] = df_e170_vpm_1['Part Design'].str.replace(",", "")

    # Criar nova coluna com somente com a informação desejada.
df_e170_vpm_1['Correct_Part_Number'] = df_e170_vpm_1['Part Number'].str.extract('(...-.....-...)', expand = True)

    # Remover aspas na coluna Part Version.
df_e170_vpm_1['Part Version'] = df_e170_vpm_1['Part Version'].str.replace("'", "")

    # Para separar letra de revisão.
df_e170_vpm_1['Correct_Revision_Letter'] = df_e170_vpm_1['Part Version'].str.extract('(...)', expand = True)

    # Exportar planilha.
df_e170_vpm_1.to_csv('df_e170_vpm.txt', sep=';')

    # Importar planilha.
df_e170_vpm_fullpn = pd.read_csv(r'C:\Users\grizzi\05-PycharmProjects\LiberacaoPNs\df_e170_vpm.txt', sep=';', encoding='utf-8', low_memory=False)

    # Concatenar PN com Letra de Revisão.
df_e170_vpm_fullpn['FullPN']=df_e170_vpm_fullpn.Correct_Part_Number.str.cat(df_e170_vpm_fullpn['Correct_Revision_Letter'], '')

    # Renomear Colunas
df_e170_vpm_fullpn = df_e170_vpm_fullpn.rename(columns={'Action Owner': 'ACTION_OWNER'})
df_e170_vpm_fullpn = df_e170_vpm_fullpn.rename(columns={'Part Responsible': 'RESPONSAVEL'})
df_e170_vpm_fullpn = df_e170_vpm_fullpn.rename(columns={'Action Status': 'STATUS_DA_ACTION'})
df_e170_vpm_fullpn = df_e170_vpm_fullpn.rename(columns={'Part Org Responsible': 'TECNOLOGIA'})


    # Selecionar somente colunas com dados relevantes.
df_e170_vpm_fullpn = df_e170_vpm_fullpn[['FullPN', 'RESPONSAVEL', 'STATUS_DA_ACTION', 'Action Start Date', 'Action End Date', 'TECNOLOGIA']]

    # Exportar planilha.
df_e170_vpm_fullpn.to_csv('df_e170_vpm_fullpn.txt', sep=';')







#- - - - 3DCOM E1-190 - - - - - - - -- - - - - - - - 3DCOM E1-190 - - - - - - - -- - - - - - 3DCOM E1-190 - -

    # Abrir a base de dados do 3DCOM (VPM_VISIB_REL-PART-E170ENG.csv)
df_e190_vpm = pd.read_csv(r'C:\Users\grizzi\05-PycharmProjects\LiberacaoPNs\ActionList190.txt', sep=' ', encoding='utf-8')

    # Separar os dados contidos em uma única coluna.
df_e190_vpm = df_e190_vpm['Action'].str.split('\t', expand=True)

    # Renomear colunas.
df_e190_vpm = df_e190_vpm.rename(columns={0:'Action Id', 1:'Action Priority', 2:'Action Owner', 3:'Action Start Date', 4:'Action End Date', 5:'Action Status', 6:'Action Description', 7:'Action Type', 8:'Part Number', 9:'Part Instance', 10:'Part Conc Version', 11:'Part Version', 12:'Part Responsible', 13:'Part Org Responsible', 14:'Part Type', 15:'Part Origin', 16:'Part Design', 17:'Part Production', 18:'Irrelevante'})

    # Criar nova coluna com somente com a informação desejada.
df_e190_vpm['Correct_Part_Number'] = df_e190_vpm['Part Number'].str.extract('(...-.....-...)', expand = True)

    # Concatenar PN com Letra de Revisão.
df_e190_vpm['FullPN']=df_e190_vpm.Correct_Part_Number.str.cat(df_e190_vpm['Part Version'], '')

    # Renomear Colunas
df_e190_vpm = df_e190_vpm.rename(columns={'Action Owner': 'ACTION_OWNER'})
df_e190_vpm = df_e190_vpm.rename(columns={'Part Responsible': 'RESPONSAVEL'})
df_e190_vpm = df_e190_vpm.rename(columns={'Action Status': 'STATUS_DA_ACTION'})
df_e190_vpm = df_e190_vpm.rename(columns={'Part Org Responsible': 'TECNOLOGIA'})

    # Selecionar somente colunas com dados relevantes.
df_e190_vpm = df_e190_vpm[['FullPN', 'RESPONSAVEL', 'STATUS_DA_ACTION', 'Action Start Date', 'Action End Date', 'TECNOLOGIA']]

    # Exportar base vpm.
df_e190_vpm.to_csv('df_e190_vpm_fullpn.txt', sep=';')









# - -Junção VPM & SAP - - - - - - - - -Junção VPM & SAP - - - - - - - - -Junção VPM & SAP - - - - - - - - -Junção VPM & SAP - - - - - - -
    # Importar VPM e170 reorganizado.
df_e170_vpm_fullpn_1 = pd.read_csv(r'C:\Users\grizzi\05-PycharmProjects\LiberacaoPNs\df_e170_vpm_fullpn.txt', sep=';', encoding='utf-8', low_memory=False)

    # Importar VPM e190 reorganizado.
df_e190_vpm_fullpn_1 = pd.read_csv(r'C:\Users\grizzi\05-PycharmProjects\LiberacaoPNs\df_e190_vpm_fullpn.txt', sep=';', encoding='utf-8', low_memory=False)

    # Importar SAP e170 reorganizado.
df_sap_fullpn_1 = pd.read_csv(r'C:\Users\grizzi\05-PycharmProjects\LiberacaoPNs\df_sap_fullpn.txt', sep=';', encoding='utf-8', low_memory=False)

    # Append vpm e170 com e190
df_vpm_append = df_e170_vpm_fullpn_1.append(df_e190_vpm_fullpn_1, sort=True)

    # Exportar append vpm e170 + e190
df_vpm_append.to_csv('df_vpm_append.txt', sep=';')

    # Mesclar VPM com SAP
df_vpm_x_sap = pd.merge(df_sap_fullpn_1, df_vpm_append, how="left", on=['FullPN'])


#df_merge_TESTE = pd.merge(df_sap_fullpn_1, df_vpm_append, how="left", on=['FullPN'])
#df_merge_TESTE.to_csv('mergeTESTE.txt', sep=';')

    # Exportar VPM x SAP
    # Planilha com a Junção do SAP e VPM (E170 e E190)
df_vpm_x_sap.to_csv('df_vpm_x_sap.txt', sep=';')







# - - TRATAR VPM + SAP - - TRATAR VPM + SAP - - TRATAR VPM + SAP - - TRATAR VPM + SAP - - TRATAR VPM + SAP

    # Importar.
df_vpm_x_sap_1 = pd.read_csv(r'C:\Users\grizzi\05-PycharmProjects\LiberacaoPNs\df_vpm_x_sap.txt', sep=';', encoding='utf-8', low_memory=False)

    # Remover Duplicatas.
df_vpm_x_sap_1 = df_vpm_x_sap_1.drop_duplicates(subset='FullPN', keep='first')

    # Remover linhas sem informação de PN.
df_vpm_x_sap_1 = df_vpm_x_sap_1.dropna(subset=['FullPN'])

    # Importar df com o nome dos usuários.
df_vpm_user = pd.read_csv(r'C:\Users\grizzi\05-PycharmProjects\LiberacaoPNs\VPM_VISIB_REL-PERSON-prd170.csv', sep=';', encoding='utf-8', low_memory=False)

    # Alterar o nome da Coluna PERSON ID para RESPONSAVEL
df_vpm_user = df_vpm_user.rename(columns={'PERSON ID': 'RESPONSAVEL'})

    # Mesclar para adicionar o nome dos usuarios ao invés de role.
df_vpm_x_sap_2 = df_vpm_x_sap_1.merge(df_vpm_user, on='RESPONSAVEL')

    # Remover colunas sem utilidade.
df_vpm_x_sap_2 = df_vpm_x_sap_2.drop(columns=['Unnamed: 0', 'Unnamed: 0_x', 'Unnamed: 0_y', 'Organization', 'First Name', 'Phone Number', 'Area'])

df_vpm_x_sap_2.to_csv('df_vpm_x_sap_2.txt', sep=';')








#-------------FILTROS---------------------FILTROS---------------------FILTROS--------------------FILTROS---------------

    # Importar planilha VPM x SAP
df_vpm_x_sap_3 = pd.read_csv(r'C:\Users\grizzi\05-PycharmProjects\LiberacaoPNs\df_vpm_x_sap_2.txt', sep=';', encoding='utf-8', low_memory=False)

    # Alterar data para DateTime
df_vpm_x_sap_3['DATA_OE'] = pd.to_datetime(df_vpm_x_sap_3['DATA_PREVISTA_FORMATADA']).dt.date
df_vpm_x_sap_3['DATA_OE'] = pd.to_datetime(df_vpm_x_sap_3['DATA_PREVISTA_FORMATADA'])

    # TODO Comparar conteúdo da planilha do SAP x VPM para verificar PNs para liberar sem action enviada.

df_sap_fullpn_2 = pd.read_csv(r'C:\Users\grizzi\05-PycharmProjects\LiberacaoPNs\df_sap_fullpn.txt', sep=';')
df_vpm_append_1 = pd.read_csv(r'C:\Users\grizzi\05-PycharmProjects\LiberacaoPNs\df_vpm_append.txt', sep=';')

compare_teste = df_sap_fullpn_2.merge(df_vpm_append_1, on='FullPN')

compare_teste.to_csv('compare_teste.txt', sep=';')

    # PNs para liberar nos próximos 2 dias em action.
today = pd.datetime.today().date()
end_date_2d = pd.datetime.today()+timedelta(days=2)
gr_pn_next_2d = df_vpm_x_sap_3[(df_vpm_x_sap_3['DATA_OE'] >= today) & (df_vpm_x_sap_3['DATA_OE'] < end_date_2d)]

gr_pn_next_2d.to_csv('gr_pn_next_2d.txt', sep=';')

    # TODO PNs para liberar nos próximos 2 dias sem action.

    # PNs para liberar nos próximos 15 dias em action.
today = pd.datetime.today().date()
end_date_15d = pd.datetime.today()+timedelta(days=15)
gr_pn_next_15d = df_vpm_x_sap_3[(df_vpm_x_sap_3['DATA_OE'] >= today) & (df_vpm_x_sap_3['DATA_OE'] < end_date_15d)]

gr_pn_next_15d.to_csv('gr_pn_next_15d.txt', sep=';')

    # TODO PNs para liberar nos próximos 15 dias sem action.

    # PNs para liberar nos próximos 30 dias em action.
today = pd.datetime.today().date()
end_date_30d = pd.datetime.today()+timedelta(days=30)
gr_pn_next_30d = df_vpm_x_sap_3[(df_vpm_x_sap_3['DATA_OE'] >= today) & (df_vpm_x_sap_3['DATA_OE'] < end_date_30d)]

gr_pn_next_30d.to_csv('gr_pn_next_30d.txt', sep=';')

    # TODO PNs para liberar nos próximos 30 dias sem action.