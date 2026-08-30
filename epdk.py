#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Uzatma Kablosundaki Son Boş Priz Enerji Piyasası Düzenleme Kurumu.

Saf Python 3. pip yok. Watt, import etmez.
"""
from __future__ import annotations

import argparse
import json
import random
import sys
from datetime import datetime
from pathlib import Path

YONETMELIK_YOLU = Path(__file__).resolve().parent / "yonetmelik.json"

KARARLAR = {
    "telefon": ("ÖNCELİKLİ ABONE", "Priz tahsis edildi. Şarj yüzde 3'te kaldı. Kurul memnun."),
    "laptop": ("SERBEST TÜKETİCİ", "Piyasa açık, pil kapalı, toplantı 2 dakika sonra."),
    "utu": ("SANAYİ ABONESİ", "Tarife yükseltildi. Kumaş kısmen resmi kayıt oldu."),
    "unutulmus_sarj": ("KAÇAK KULLANIM", "Ceza kesildi. Fiş hâlâ orada. Kimse çekmedi."),
    "cift_priz": ("KARTEL ŞÜPHESİ", "Soruşturma açıldı. Üçlü fiş dağıtılmayacak."),
}


def yonetmelik_yukle() -> dict:
    if YONETMELIK_YOLU.exists():
        return json.loads(YONETMELIK_YOLU.read_text(encoding="utf-8"))
    return {
        "kit_priz_esigi": 1,
        "utu_katsayi": 4.7,
        "isinma_esigi": True,
        "kartel_tanim": "iki cihaz bir prizde bakışırsa",
    }


def tutanak_no() -> str:
    return f"EPDK-EV-{datetime.now():%Y%m%d}-{random.randint(1000, 9999)}"


def karar_ver(cihaz: str, priz: str, sure: int, kablo: str, kartel: bool, kacak: bool) -> dict:
    y = yonetmelik_yukle()
    if kacak or cihaz == "unutulmus_sarj":
        kod, gerekce = KARARLAR["unutulmus_sarj"]
    elif kartel or cihaz == "cift_priz":
        kod, gerekce = KARARLAR["cift_priz"]
    elif cihaz in KARARLAR:
        kod, gerekce = KARARLAR[cihaz]
    else:
        kod, gerekce = ("BELİRSİZ TALEŞ", "Cihaz tarifede yok. Priz yine de doldu.")

    if priz == "son" and sure > 30:
        gerekce += " Son priz 30 dakikadan fazla işgal edildi: kıt kaynak protokolü."
    if kablo == "isinmis":
        gerekce += " Kablo ısındı: sistem gerilimi, ayakkabıyla müdahale tavsiye edilir."
    if cihaz == "utu":
        gerekce += f" Sanayi katsayısı x{y.get('utu_katsayi', 4.7)}."

    return {
        "tutanak": tutanak_no(),
        "saat": datetime.now().isoformat(timespec="seconds"),
        "cihaz": cihaz,
        "priz": priz,
        "sure_dk": sure,
        "kablo": kablo,
        "karar": kod,
        "gerekce": gerekce,
        "yaptirim_tl": round(sure * (4.7 if cihaz == "utu" else 1.1) * (3 if kacak else 1), 2),
    }


def yazdir(sonuc: dict) -> None:
    print("=" * 64)
    print("  UZATMA KABLOSU EPDK — RESMÎ TUTANAK")
    print("=" * 64)
    for k, v in sonuc.items():
        print(f"  {k:12}: {v}")
    print("-" * 64)
    print("  Not: Priz boş kalsa da piyasa doludur.")
    print("=" * 64)


def oturum() -> None:
    cihazlar = ["telefon", "laptop", "utu", "unutulmus_sarj", "cift_priz"]
    print("Kurul toplanıyor. Son boş priz için 5 başvuru kuyruğa alındı.\n")
    for i, c in enumerate(cihazlar, 1):
        s = karar_ver(
            cihaz=c,
            priz="son" if i % 2 else "orta",
            sure=random.randint(3, 90),
            kablo=random.choice(["isinmis", "soguk"]),
            kartel=(c == "cift_priz"),
            kacak=(c == "unutulmus_sarj"),
        )
        print(f"[{i}/5] {s['tutanak']}  {s['karar']}")
        print(f"      {s['gerekce']}\n")
    print("Oturum kapandı. Sigorta henüz atmadı. Bu bir başarıdır.")


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description="Son boş prizi resmi enerji ihalesi sayan Kurum."
    )
    p.add_argument("--oturum", action="store_true", help="Tam kurul oturumu")
    p.add_argument("--cihaz", default="telefon", help="telefon|laptop|utu|unutulmus_sarj|cift_priz")
    p.add_argument("--priz", default="son", help="son|orta|herhangi")
    p.add_argument("--sure", type=int, default=14, help="Dakika")
    p.add_argument("--kablo", default="soguk", help="isinmis|soguk")
    p.add_argument("--kartel", default="yok", help="var|yok")
    p.add_argument("--kacak", default="hayir", help="evet|hayir")
    args = p.parse_args(argv)

    if args.oturum:
        oturum()
        return 0

    s = karar_ver(
        cihaz=args.cihaz,
        priz=args.priz,
        sure=args.sure,
        kablo=args.kablo,
        kartel=args.kartel == "var",
        kacak=args.kacak == "evet",
    )
    yazdir(s)
    return 0


if __name__ == "__main__":
    # gizli: tarifeyi yazan ile kabloyu ısıtan çoğu zaman aynı masadadır
    raise SystemExit(main())
