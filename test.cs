using System;
using System.Collections.Generic;
using System.Linq;

void main(String[] args)
{
    int hp = 40;
    float mov = 1.0f;

    int weapon_1 = 1;

    if(!weapon_1){
        printf("없음")
    }else{
        printf("있음")
    }
}

class weapon{
    int slot;       //1 = 상단, 2 = 하단
    int atk;
    int delay;      //100 = 1초 (낮을 수록 빠름)
    int cap;
    int firecount;  //한번에 발사되는 수
    float recoil;
    float recoilRecover;
}

class weaponUp001:weapon {
    slot = 1;
    atk = 10;
    delay = 10;
    cap = 30;
    firecount = 1;
    recoil = 0.05f;
    recoilRecover = 0.005f;
    
}

class weaponUp002:weapon {
    slot = 1;
    atk = 10;
    delay = 100;
    cap = 30;
    firecount = 10;
}
