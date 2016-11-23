#include <iostream>
#include <string>
#include "json/json/json-forwards.h"
#include "json/json/json.h"

using namespace std;

struct OperCodeStr {
    int code; // 运营商code
    char oper[64]; //运营商名字
    char country[64];//所在国家
};

struct OperCodeStr arr[] =
{
{20201, "Cosmote", "GR"},

{20205, "Vodafone GR", "GR"},

{20210, "TELESTET", "GR"},

{20404, "Vodafone NL", "NL"},

{20408, "KPN", "NL"},

{20412, "O2 - NL", "NL"},

{20416, "Ben", "NL"},

{20420, "dutchtone", "NL"},

{20601, "Proximus", "BE"},

{20610, "Mobistar", "BE"},

{20620, "Orange", "BE"},

{20801, "Orange", "FR"},

{20810, "SFR", "FR"},

{20820, "BOUYGTEL", "FR"},

{21303, "Mobiland", "AD"},

{21401, "Vodafone E", "ES"},

{21402, "MoviStar", "ES"},

{21403, "AMENA", "ES"},

{21404, "Xfera", "ES"},

{21407, "MoviStar", "ES"},

{21601, "Pannon GSM", "HU"},

{21630, "Westel", "HU"},

{21670, "Vodafone", "HU"},

{21803, "ERONET", "BA"},

{21805, "Mobilna Srpska", "BA"},

{21890, "GSM BiH", "BA"},

{21901, "CRONET", "HR"},

{21910, "VIP", "HR"},

{22001, "MOBTEL", "YU"},

{22002, "ProMonte", "YU"},

{22003, "Telekom Srbija", "YU"},

{22004, "MONET", "YU"},

{22201, "TIM", "IT"},

{22210, "Vodafone IT", "IT"},

{22288, "WIND", "IT"},

{22298, "Blu SpA", "IT"},

{22601, "CONNEX", "RO"},

{22603, "Cosmorom", "RO"},

{22610, "dialog", "RO"},

{22801, "Swiss GSM", "CH"},

{22802, "sunrise", "CH"},

{22803, "Orange", "CH"},

{23001, "PAEGAS", "CZ"},

{23002, "EUROTEL", "CZ"},

{23003, "OSKAR", "CZ"},

{23101, "GLOBTEL", "SK"},

{23102, "EUROTEL", "SK"},

{23201, "A1", "AT"},

{23203, "T-Mobile", "AT"},

{23205, "ONE", "AT"},

{23207, "tele.ring", "AT"},

{23410, "O2 - UK", "GB"},

{23415, "Vodafone", "GB"},

{23430, "T-Mobile UK", "GB"},

{23431, "T-Mobile UK", "GB"},

{23432, "T-Mobile UK", "GB"},

{23433, "Orange", "GB"},

{23450, "JT GSM", "GB"},

{23455, "GUERNSEY TEL", "GB"},

{23458, "MANX", "GB"},

{23801, "TDK-MOBIL", "DK"},

{23802, "SONOFON", "DK"},

{23820, "Telia", "DK"},

{23830, "Orange", "DK"},

{24001, "Telia S", "SE"},

{24007, "IQ", "SE"},

{24008, "Vodafone", "SE"},

{24201, "TELENOR", "NO"},

{24202, "NetCom", "NO"},

{24403, "Telia", "FI"},

{24405, "RADIOLINJA", "FI"},

{24409, "FINNET", "FI"},

{24412, "2G", "FI"},

{24414, "AMT", "FI"},

{24491, "SONERA", "FI"},

{24601, "OMNITEL", "LT"},

{24602, "Bite GSM", "LT"},

{24603, "TELE2", "LT"},

{24701, "LMT GSM", "LV"},

{24702, "BALTCOM", "LV"},

{24801, "EMT GSM", "EE"},

{24802, "RLE", "EE"},

{24803, "Q GSM", "EE"},

{25001, "MTS", "RU"},

{25002, "NorthWest GSM", "RU"},

{25003, "NCC", "RU"},

{25005, "SCS", "RU"},

{25007, "SMARTS", "RU"},

{25010, "DTC", "RU"},

{25011, "Orensot", "RU"},

{25012, "Far East", "RU"},

{25013, "Kuban GSM", "RU"},

{25016, "NTC", "RU"},

{25017, "Ermak RMS", "RU"},

{25028, "EXTEL", "RU"},

{25039, "Uraltel", "RU"},

{25044, "NC-GSM", "RU"},

{25091, "Sonic Duo", "RU"},

{25092, "Primtel", "RU"},

{25093, "JSC Telecom XXI", "RU"},

{25099, "Bee Line", "RU"},

{25501, "UMC", "UA"},

{25502, "WellCOM", "UA"},

{25503, "Kyivstar", "UA"},

{25505, "Golden Telecom", "UA"},

{25701, "VELCOM", "BY"},

{25901, "VOXTEL", "MD"},

{25902, "MOLDCELL", "MD"},

{26001, "Plus GSM", "PL"},

{26002, "Era GSM", "PL"},

{26003, "IDEA", "PL"},

{26201, "T-Mobile", "DE"},

{26202, "Vodafone D2", "DE"},

{26203, "E-Plus", "DE"},

{26207, "O2 - DE", "DE"},

{26213, "Mobilcom", "DE"},

{26601, "GIBTEL", "GI"},

{26801, "Vodafone", "PT"},

{26803, "OPTIMUS", "PT"},

{26806, "TMN", "PT"},

{27001, "LUXGSM", "LU"},

{27077, "TANGO", "LU"},

{27201, "Vodafone IRL", "IE"},

{27202, "O2 - IRL", "IE"},

{27203, "METEOR", "IE"},

{27401, "SIMINN", "IS"},

{27402, "TAL", "IS"},

{27404, "Viking", "IS"},

{27601, "AMC", "AL"},

{27602, "Vodafone", "AL"},

{27801, "Vodafone Malta", "MT"},

{27821, "go mobile", "MT"},

{28001, "CYTAGSM", "CY"},

{28201, "GEOCELL", "GE"},

{28202, "Magti GSM", "GE"},

{28203, "GEO 03", "GE"},

{28301, "ARMGSM", "AM"},

{28401, "M-TEL GSM", "BG"},

{28601, "TURKCELL", "TR"},

{28602, "TELSIM", "TR"},

{28603, "ARIA", "TR"},

{28604, "AYCELL", "TR"},

{28801, "FT GSM", "FO"},

{29001, "TELE Greenland", "GR"},

{29340, "SI.MOBIL", "SI"},

{29341, "MOBITEL", "SI"},

{29401, "MOBIMAK", "MK"},

{29501, "TELECOM", "LI"},

{29502, "MONTEL", "LI"},

{29505, "FL1", "LI"},

{29577, "LI TANGO", "LI"},

{30237, "Microcell", "CA"},

{30272, "Rogers AT&T", "CA"},

{31001, "Cellnet", "US"},

{31011, "Wireless 2000", "US"},

{31015, "Cingular", "US"},

{31016, "T-Mobile", "US"},

{31017, "Cingular", "US"},

{31018, "Cingular", "US"},

{31020, "T-Mobile", "US"},

{31021, "T-Mobile", "US"},

{31022, "T-Mobile", "US"},

{31023, "T-Mobile", "US"},

{31024, "T-Mobile", "US"},

{31025, "T-Mobile", "US"},

{31026, "T-Mobile", "US"},

{31027, "T-Mobile", "US"},

{31031, "T-Mobile", "US"},

{31034, "WestLink", "US"},

{31035, "Carolina", "US"},

{31038, "AT&T Wireless", "US"},

{31041, "Cingular", "US"},

{31046, "TMP Corp", "US"},

{31058, "T-Mobile", "US"},

{31061, "Epic Touch", "US"},

{31063, "AmeriLink", "US"},

{31064, "Einstein PCS", "US"},

{31066, "T-Mobile", "US"},

{31067, "Wireless 2000", "US"},

{31068, "NPI Wireless", "US"},

{31069, "Conestoga", "US"},

{31074, "Telemetrix", "US"},

{31076, "PTSI", "US"},

{31077, "Iowa Wireless", "US"},

{31078, "Airlink PCS", "US"},

{31079, "PinPoint", "US"},

{31080, "T-Mobile", "US"},

{31098, "AWS", "US"},

{31114, "Sprocket", "UNKNOWN_COUNTRY_CODE"},

{31601, "Nextel", "UNKNOWN_COUNTRY_CODE"},

{33805, "Digicel", "JM"},

{34001, "Orange ", "FW"},

{34020, "Bouygues", "FW"},

{34430, "APUA PCS", "AG"},

{35001, "Telecom", "BM"},

{36251, "Telcell GSM", "AN"},

{36801, "C_Com", "CU"},

{37001, "Orange", "DO"},

{40001, "AZERCELL GSM", "AZ"},

{40002, "BAKCELL GSM 2000", "AZ"},

{40101, "K-MOBILE", "KZ"},

{40102, "K'CELL", "KZ"},

{40401, "Hutch", "IN"},

{40402, "Airtel", "IN"},

{40403, "Airtel", "IN"},

{40404, "IDEA", "IN"},

{40405, "Hutch", "IN"},

{40407, "IDEA", "IN"},

{40409, "Reliance", "IN"},

{40410, "Airtel", "IN"},

{40411, "Hutch", "IN"},

{40412, "IDEA", "IN"},

{40413, "Hutch", "IN"},

{40414, "Spice", "IN"},

{40415, "Hutch", "IN"},

{40416, "Airtel", "IN"},

{40418, "Reliance", "IN"},

{40419, "IDEA", "IN"},

{40420, "Hutch", "IN"},

{40421, "BPL Mobile", "IN"},

{40422, "IDEA", "IN"},

{40424, "IDEA", "IN"},

{40427, "Hutch", "IN"},

{40429, "Aircel", "IN"},

{40430, "Hutch", "IN"},

{40431, "Airtel", "IN"},

{40434, "Cellone", "IN"},

{40436, "Reliance", "IN"},

{40437, "Aircel", "IN"},

{40438, "Cellone", "IN"},

{40440, "Airtel", "IN"},

{40441, "RPG", "IN"},

{40443, "Hutch", "IN"},

{40444, "Spice", "IN"},

{40445, "Airtel", "IN"},

{40446, "Hutch", "IN"},

{40449, "Airtel", "IN"},

{40450, "Reliance", "IN"},

{40451, "Cellone", "IN"},

{40452, "Reliance", "IN"},

{40453, "Cellone", "IN"},

{40454, "Cellone", "IN"},

{40455, "Cellone", "IN"},

{40456, "IDEA", "IN"},

{40457, "Cellone", "IN"},

{40458, "Cellone", "IN"},

{40459, "Cellone", "IN"},

{40460, "Hutch", "IN"},

{40462, "Cellone", "IN"},

{40464, "Cellone", "IN"},

{40466, "Cellone", "IN"},

{40467, "Reliance", "IN"},

{40468, "DOLPHIN", "IN"},

{40469, "MTNL", "IN"},

{40470, "Airtel", "IN"},

{40471, "Cellone", "IN"},

{40472, "Cellone", "IN"},

{40473, "Cellone", "IN"},

{40474, "Cellone", "IN"},

{40475, "Cellone", "IN"},

{40476, "Cellone", "IN"},

{40477, "Cellone", "IN"},

{40478, "IDEA", "IN"},

{40479, "Cellone", "IN"},

{40480, "Cellone", "IN"},

{40481, "Cellone", "IN"},

{40482, "IDEA", "IN"},

{40483, "Reliance", "IN"},

{40484, "Hutch", "IN"},

{40485, "Reliance", "IN"},

{40486, "Hutch", "IN"},

{40487, "IDEA", "IN"},

{40488, "Hutch", "IN"},

{40489, "IDEA", "IN"},

{40490, "Airtel", "IN"},

{40492, "Airtel", "IN"},

{40493, "Airtel", "IN"},

{40494, "Airtel", "IN"},

{40495, "Airtel", "IN"},

{40496, "Airtel", "IN"},

{40497, "Airtel", "IN"},

{40498, "Airtel", "IN"},

{40551, "Airtel", "IN"},

{40552, "Airtel", "IN"},

{40553, "Airtel", "IN"},

{40554, "Airtel", "IN"},

{40555, "Airtel", "IN"},

{40556, "Airtel", "IN"},

{40566, "Hutch", "IN"},

{40567, "Hutch", "IN" },

{41001, "Mobilink", "PK"},

{41302, "DIALOG", "LK"},

{41303, "CELLTEL", "LK"},

{41401, "MM 900", "MM"},

{41501, "Cellis", "LB"},

{41503, "LibanCell", "LB"},

{41601, "Fastlink", "JO"},

{41677, "MobileCom", "JO"},

{41702, "Spacetel", "SY"},

{41709, "MOBILE SYRIA", "SY"},

{41902, "MTCNet", "KW"},

{41903, "WATANIYA", "KW"},

{42001, "Al-Jawal", "SA"},

{42007, "EAE", "SA"},

{42102, "Spacetel", "YE"},

{42202, "OMAN MOBILE", "OM"},

{42402, "ETISALAT", "AE"},

{42501, "Orange", "IL"},

{42505, "JAWWAL", "IL"},

{42601, "MOBILE PLUS", "BH"},

{42701, "QATARNET", "QA"},

{42899, "MobiCom", "MN"},

{42901, "NTC", "NP"},

{43211, "TCI", "IR"},

{43214, "KISH", "IR"},

{43401, "Buztel", "UZ"},

{43402, "Uzmacom", "UZ"},

{43404, "UZB DAEWOO-GSM", "UZ"},

{43405, "Coscom", "UZ"},

{43701, "BITEL", "KG"},

{43801, "BCTI", "TM"},

{45201, "MOBIFONE", "VN"},

{45202, "VINAFONE", "VN"},

{45400, "CSL", "HK"},

{45401, "NEW WORLD", "HK"},

{45402, "CSL", "HK"},

{45404, "Orange", "HK"},

{45406, "SMC", "HK"},

{45410, "NEW WORLD", "HK"},

{45412, "PEOPLES", "HK"},

{45416, "SUNDAY", "HK"},

{45418, "HK TELECOM", "HK"},

{45500, "SmarTone", "UNKNOWN_COUNTRY_CODE"},

{45501, "CTMGSM", "UNKNOWN_COUNTRY_CODE"},

{45503, "HT Macau", "UNKNOWN_COUNTRY_CODE"},

{45601, "MobiTel", "KH"},

{45602, "SAMART-GSM", "KH"},

{45701, "LAO GSM", "LA"},

{46000, "CHINA MOBILE", "CN"},

{46001, "CHN-CUGSM", "CN"},

{46002, "CHINA MOBILE", "CN"},

{46601, "Far EasTone", "TW"},

{46606, "TUNTEX", "TW"},

{46668, "ACeS", "TW"},

{46688, "KGT", "TW"},

{46692, "Chunghwa", "TW"},

{46693, "MobiTai", "TW"},

{46697, "TWN GSM", "TW"},

{46699, "TransAsia", "TW"},

{47001, "GrameemPhone", "BD"},

{47002, "AKTEL", "BD"},

{47003, "ShebaWorld", "BD"},

{47019, "Mobile 2000", "BD"},

{47201, "DHIMOBILE", "MV"},

{50212, "Maxis Mobile", "MY"},

{50213, "TM Touch", "MY"},

{50216, "DiGi", "MY"},

{50217, "ADAM", "MY"},

{50219, "CELCOM", "MY"},

{50501, "MobileNet", "AU"},

{50502, "OPTUS", "AU"},

{50503, "Vodafone", "AU"},

{50508, "One.Tel", "AU"},

{51000, "ACeS", "ID"},

{51001, "SATELINDOCEL", "ID"},

{51008, "LIPPO TEL", "ID"},

{51010, "TELKOMSEL", "ID"},

{51011, "GSM-XL", "ID"},

{51021, "INDOSAT", "ID"},

{51501, "ISLACOM", "PH"},

{51502, "Globe", "PH"},

{51503, "SMART", "PH"},

{51505, "Digitel", "PH"},

{51511, "ACeS", "PH"},

{52001, "AIS GSM", "TH"},

{52015, "ACT Mobile", "TH"},

{52018, "WP-1800", "TH"},

{52020, "ACeS", "TH"},

{52023, "HELLO", "TH"},

{52099, "Orange", "TH"},

{52501, "ST-GSM-SGP", "SG"},

{52502, "ST-GSM1800-SGP", "SG"},

{52503, "M1-GSM-SGP", "SG"},

{52504, "SGP-M1-3GSM", "SG"},

{52505, "STARHUB-SGP", "SG"},

{52811, "BRU TSTCom", "BN"},

{53001, "Vodafone", "NZ"},

{53901, "Tonga Comm.", "TO"},

{54100, "ACeS", "VU"},

{54101, "SMILE", "VU"},

{54201, "Vodafone", "FJ"},

{54411, "Blue Sky", "AS"},

{54601, "MOBILIS", "NC"},

{54720, "VINI", "PF"},

{55001, "FSM", "FM"},

{60201, "MobiNiL", "EG"},

{60202, "CLICK GSM", "EG"},

{60301, "AMN", "DZ"},

{60400, "Meditel", "MA"},

{60401, "IAM", "MA"},

{60502, "TUNICELL", "TN"},

{60801, "ALIZE", "SN"},

{60802, "SENTEL", "SN"},

{61001, "MALITEL", "ML"},

{61101, "MOBILIS", "GN"},

{61102, "LAGUI", "GN"},

{61201, "CORA", "CI"},

{61203, "Ivoiris", "CI"},

{61205, "TELECEL", "CI"},

{61302, "CELTEL", "BF"},

{61402, "CELTEL", "NE"},

{61501, "TOGOCEL", "TG"},

{61601, "LIBERCOM", "BJ"},

{61602, "Telecel Benin", "BJ"},

{61603, "BENINCELL", "BJ"},

{61701, "CELLPLUS", "MU"},

{61710, "EMTEL", "MU"},

{61801, "Omega", "LR"},

{62001, "SPACEFON", "GH"},

{62002, "ONEtouch", "GH"},

{62003, "MOBITEL", "GH"},

{62100, "MTN", "NG"},

{62120, "ECONET", "NG"},

{62130, "MTN", "NG"},

{62140, "NITEL GSM", "NG"},

{62201, "CELTEL", "TD"},

{62202, "LIBERTIS", "TD"},

{62401, "MTN-CAM", "CM"},

{62402, "MOBILIS", "CM"},

{62501, "CPV MOVEL", "CV"},

{62801, "LIBERTIS", "GA"},

{62802, "GO Celtel", "GA"},

{62803, "CELTEL", "GA"},

{62901, "CELTEL", "CG"},

{62910, "LIBERTIS", "CG"},

{63001, "CELLNET", "CD"},

{63002, "CELTEL", "CD"},

{63004, "CELLCO", "CD"},

{63089, "OASIS", "CD"},

{63301, "SEYCEL", "SC"},

{63310, "AIRTEL", "SC"},

{63401, "MobiTel", "MZ"},

{63510, "Rwandacell", "RW"},

{63601, "ETMTN", "ET"},

{63701, "BARAKAAT", "SO"},

{63902, "Safaricom", "KE"},

{63903, "KENCELL", "KE"},

{64001, "TRITEL", "TZ"},

{64002, "MobiTel", "TZ"},

{64003, "ZANTEL", "TZ"},

{64004, "Vodacom", "TZ"},

{64005, "CELTEL", "TZ"},

{64101, "CelTel", "UG"},

{64110, "MTN-UGANDA", "UG"},

{64111, "UTL TELECEL", "UG"},

{64201, "Spacetel", "BI"},

{64202, "SAFARIS", "BI"},

{64301, "mCel", "UNKNOWN_COUNTRY_CODE"},

{64501, "ZAMCELL", "UNKNOWN_COUNTRY_CODE" },

{64502, "TELECEL", "UNKNOWN_COUNTRY_CODE"},

{64601, "Madacom", "MG"},

{64602, "ANTARIS", "MG"},

{64700, "Orange Reunion", "RE"},

{64710, "SFR Reunion", "RE"},

{64801, "NET*ONE", "ZW"},

{64803, "TELECEL", "ZW"},

{64804, "ECONET", "ZW"},

{64901, "MTC", "NA"},

{65001, "CALLPOINT 90", "MW"},

{65010, "CelTel", "MW"},

{65101, "Vodacom", "LS"},

{65201, "MASCOM", "BW"},

{65202, "VISTA", "BW"},

{65310, "SwaziMTN", "SZ"},

{65501, "Vodacom", "ZA"},

{65507, "Cell C (Pty) Ltd", "ZA"},

{65510, "MTN", "ZA"},

{70601, "PERSONAL", "SV"},

{70602, "DIGICEL", "SV"},

{71610, "TIM", "PE"},

{72207, "UNIFON", "AR"},

{72234, "Telecom Personal", "AR"},

{72235, "PORT-HABLE", "AR"},

{72402, "TIM BRASIL", "BR"},

{72403, "TIM BRASIL", "BR"},

{72404, "TIM BRASIL", "BR"},

{72405, "Claro", "BR"},

{72416, "BrTCel", "BR"},

{73001, "ENTEL PCS", "CL"},

{73010, "ENTEL PCS", "CL"},

{73401, "INFONET", "VE"},

{73402, "DIGITEL", "VE"},

{73601, "NUEVATEL", "BO"},

{73602, "ENTEL", "BO"},

{74401, "VOX", "PY"},

{74402, "PY 02", "PY"},

{74601, "ICMS", "SR"},

{90105, "Thuraya", "UNKNOWN_COUNTRY_CODE"},
};

int main() {
  Json::Value root;

  for (struct OperCodeStr &obj : arr) {
    root[obj.country][obj.oper].append(obj.code); 
  }

  Json::FastWriter writer;

  string str = writer.write(root);   

  cout << str << endl;

  return 0;
}

