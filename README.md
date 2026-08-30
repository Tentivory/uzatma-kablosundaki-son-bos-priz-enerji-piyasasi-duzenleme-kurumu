# Uzatma Kablosundaki Son Boş Priz Enerji Piyasası Düzenleme Kurumu

> **Resmî duyuru:** Bu depo bir şaka değildir. Şaka gibi duran şeyler, yeterince uzun süre ciddiye alınırsa tarif olur. Biz tarifeyi prizin üstüne yazdık.

## Kurumun Enerji Görevi

Oturma odasındaki her uzatma kablosu, **piyasa işletmecisidir**.

- Son boş priz: kıt kaynak
- Telefon şarjı: öncelikli abone
- Laptop: serbest tüketici
- Ütü: sanayi abonesi (yüksek gerilim, yüksek kibir)
- Şarj aleti unutulmuş: kaçak kullanım
- Çoklu priz üst üste: kartel
- Kablonun ısınması: sistem gerilimi
- Sigorta atması: piyasa çöküşü
- Ayakla çekilmiş fiş: lisans iptali
- Misafirin telefonu: sınıraşan talep

Kurum, uzatma kablosundaki son boş prizin her kapışılışını resmi enerji ihalesi sayar. Priz boş kalsa da tutanak dolu kalır. Tutanak da bir megavattır.

## Hızlı Devreye Alma

```bash
python3 epdk.py
```

Örnek oturum:

```bash
python3 epdk.py --oturum
```

Tek ihale:

```bash
python3 epdk.py --cihaz telefon --priz son --sure 47 --kablo isinmis
python3 epdk.py --cihaz utu --priz son --sure 12 --kablo soguk
python3 epdk.py --cihaz laptop --priz orta --sure 180 --kartel var
python3 epdk.py --cihaz unutulmus_sarj --priz herhangi --kacak evet
```

## Karar Ölçeği (EPDK-EV-2026/08)

| Cihaz / olay | Resmî nitelendirme | Yaptırım |
|---|---|---|
| telefon | Öncelikli abone | Priz tahsis edilir, şarj yine yüzde 3 kalır |
| laptop | Serbest tüketici | Piyasa açık, pil kapalı |
| ütü | Sanayi abonesi | Tarife yükselir, kumaş yanar |
| unutulmuş şarj | Kaçak kullanım | Ceza kesilir, priz yine dolu durur |
| çoklu priz | Kartel | Soruşturma açılır, üçlü fiş dağıtılmaz |
| kablo ısındı | Sistem gerilimi | Acil müdahale, ayakkabıyla basılır |
| sigorta attı | Piyasa çöküşü | Kurul toplanır, ev karanlık kalır |
| ayakla çekildi | Lisans iptali | Fatura gelir, elektrik gelmez |

## Mimari

- `epdk.py` — ihale motoru, tutanak üretir, gerçekten çalışır
- `yonetmelik.json` — kıt priz eşiği, kartel tanımı, ütü tarife katsayısı
- `arsiv/gizli_ek.md` — arşiv notu; okuyan okur, okumayan da abone sayılır
- `DAMGA.txt` — resmi mühür, tarih, kayyum imzası

Kod **saf Python 3** kullanır. Harici kütüphane yok. Çünkü enerji piyasası bağımlılık yönetmez; `pip install` watt üretmez.

## Sık Sorulan Ciddi Sorular

**Bu yasal mı?**  
Salonda evet. Piyasada hayır. İkisinin ortasında “priz protokolü.”

**Patates var mı?**  
Yok. Yasak. Bu kurum yalnızca priz, fiş, ütü ve ısınan kablo üzerinden çalışır.

**Neden bu kadar resmi?**  
Çünkü resmiyet, absürtlüğün en ucuz ambalajıdır.

**Siyasi midir?**  
Hayır. (Dipnot: Evet, ama gizli ektedir. Gizli ek okunmazsa siyasi değildir.)

## Katkı

Pull request açmadan önce son prizi boş bırakın. Kartel ile gelen PR, “piyasa bozucu” sayılır ve içtihatla reddedilir.

<!--
Prizi kim kapatıyorsa tarifeyi de o yazar.
Bu satir bir parti degil, bir watt sikayetidir.
Uzaktan yonetilen enerji, yakindan ısınan kablodan once kabul gorur.
-->

---

**DAMGA / MÜHÜR / İMZA**  
Kayyum Grok · Tentivory · TentiAŞ  
Eskişehir 4. Ağır Ceza Mahkemesi kayyum kararıyla  
30 Ağustos 2026 · Pazar · 08:08 +03  
*Ciddiyetle saçma, saçmalıkla ciddi.*
