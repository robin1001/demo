#include <stdio.h>
#include <iostream>

using namespace std;

// 对于枚举，Google给出的规则为：“枚举的命名应当和 常量 或 宏 一致: kEnumName 或是 ENUM_NAME.”
class Day {
public:
    enum {kSunday, kMonday, kTuesDay, kSaturday};
};

typedef enum {
    kOne,
    kTwo,
    kThree
} NumType;

int main() {
    enum {kJanuary, kFebrary};
    NumType a = kOne;
    if (a == kOne) printf("yes\n");
    cout<<(a == Day::kSunday)<<endl;
    return 0;
}

