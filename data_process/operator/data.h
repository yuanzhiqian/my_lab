#ifndef DATA_H
#define DATA_H

struct OperCodeStr {
    int code; // 运营商code
    char oper[64]; //运营商名字
    char country[64];//所在国家
};

struct OperCodeStrExt {
    int code; // 运营商code
    char oper[64]; //运营商名字
    char country[64];//所在国家
    char status[64];//operational or not
};

#if 0
struct OperCodeStrExt : public OperCodeStr {
    char status[64];//operational or not
};
#endif

#endif
