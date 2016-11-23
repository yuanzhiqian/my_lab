#include <iostream>
#include <string>
#include "json/json/json-forwards.h"
#include "json/json/json.h"
#include "data.h"

using namespace std;

extern struct OperCodeStr data_arr[];
extern int array_size;

int main() {
  Json::Value root;

  int i = 0;

  for (size_t i = 0; i < array_size; ++i) {
    struct OperCodeStr &obj = data_arr[i];
    root[obj.country][obj.oper].append(obj.code); 
    i++;
  }

  Json::FastWriter writer;

  string str = writer.write(root);   

  cout << str << endl;

  return 0;
}

