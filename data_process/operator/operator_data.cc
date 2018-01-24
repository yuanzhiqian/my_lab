#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
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
      ;//continue;
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
  
  cout << "=========beautifully separated=========" << endl;

  cout << str_sel << endl;

  cout << "=========beautifully separated=========" << endl;

  for (auto country : selected.getMemberNames()) {
      for (auto oper : selected[country].getMemberNames()) {
          for (size_t i = 0; i < selected[country][oper].size(); ++i) {
              //cout << 191919 << endl;
              cout << selected[country][oper][(int)i].asInt() << endl;
          }
      }
  }

  cout << "=========beautifully separated=========" << endl;

  ifstream op_old_file("op_old");  
  ifstream op_new_file("op_new");  

  vector<int> op_old_vec;
  vector<int> op_new_vec;
 
  int temp_int;

  while (op_old_file >> temp_int)
    op_old_vec.push_back(temp_int);

  while (op_new_file >> temp_int)
    op_new_vec.push_back(temp_int);

  sort(op_old_vec.begin(), op_old_vec.end());
  sort(op_new_vec.begin(), op_new_vec.end());

  vector<int> op_diff_vec;

  set_difference(op_new_vec.begin(), op_new_vec.end(), op_old_vec.begin(), op_old_vec.end(), back_inserter(op_diff_vec));

  Json::Value root_diff;

  for (size_t i = 0; i < array_size_ext; ++i) {
    struct OperCodeStrExt &obj = data_arr_ext[i];
    if (find(op_diff_vec.begin(), op_diff_vec.end(), obj.code) == op_diff_vec.end())
      continue;
    root_diff[obj.country][obj.oper].append(obj.code); 
  }

  string str_diff = writer.write(root_diff);   
  cout << str_diff << endl;

  for (size_t i = 0; i < op_diff_vec.size(); ++i) {
    cout << op_diff_vec[i] << endl;
  }

  return 0;
}

