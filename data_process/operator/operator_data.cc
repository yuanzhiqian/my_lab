#include <iostream>
#include <string>
#include "json/json/json-forwards.h"
#include "json/json/json.h"
#include "data.h"
#include <string.h>

using namespace std;

extern struct OperCodeStr data_arr[];
extern struct OperCodeStrExt data_arr_ext[];
extern int array_size;
extern int array_size_ext;

int main() {
  Json::Value root;

  int i = 0;

#if 0
  for (size_t i = 0; i < array_size; ++i) {
    struct OperCodeStr &obj = data_arr[i];
    root[obj.country][obj.oper].append(obj.code); 
    i++;
  }
#endif

#if 1
  for (size_t i = 0; i < array_size_ext; ++i) {
    struct OperCodeStrExt &obj = data_arr_ext[i];
    //if (strncmp(obj.status, "Not Operational", strlen("Not Operational")) == 0) 
    if (strncasecmp(obj.status, "Not Operational", strlen("Not Operational")) == 0) 
      continue;
    root[obj.country][obj.oper].append(obj.code); 
  }
#endif

  Json::Value selected; 
  selected["IN"] = root["IN"];
  selected["BN"] = root["BN"];
  selected["KH"] = root["KH"];
  selected["TL"] = root["TL"];
  selected["ID"] = root["ID"];
  selected["LA"] = root["LA"];
  selected["MY"] = root["MY"];
  selected["MM"] = root["MM"];
  selected["PH"] = root["PH"];
  selected["SG"] = root["SG"];
  selected["TH"] = root["TH"];
  selected["VN"] = root["VN"];

  Json::FastWriter writer;

  string str = writer.write(root);   
  string str_sel = writer.write(selected);   

  cout << str << endl;
  
  cout << "=========beatifully separated=========" << endl;

  cout << str_sel << endl;

  cout << "=========beatifully separated=========" << endl;

  for (auto country : selected.getMemberNames()) {
      for (auto oper : selected[country].getMemberNames()) {
          for (size_t i = 0; i < selected[country][oper].size(); ++i) {
              //cout << 191919 << endl;
              cout << selected[country][oper][(int)i].asInt() << endl;
          }
      }
  }

  return 0;
}

