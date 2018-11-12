# RS-232
## Rs-232 Nedir?
R2-232 serial communications’da kullanılan, ve daha birçok kullanım alanı olan tekniktir. Seri veya asenkron olarak gönderilen verinin alınması ve iletilmesini gerçekleştiren cihazlar arasında bu tür haberleşmenin sağlanabilmesi için geliştirilen bir standartdır. İlk olarak 1962 yılında çıkmıştır ve onun üçüncü versiyonu 1969 yılında RS-232C olarak adlandırılmıştır. RS-232D standardı ise RS-232C üzerinde genişletme yapmak için 1987 yılında çıkmıştır. RS232D standardı aynı zamanda EIA-232-D olarak da bilinir.

## Rs-232’de SİNYAL KODLAMASI
![voltagelevel](https://user-images.githubusercontent.com/25572428/48372744-927c3600-e6d0-11e8-9f03-15aad96fda14.jpg)

RS-232 C hatları için gerilim seviyeleri +12 V ve -12V’dur. Fakat RS-232 hatları, +25VDc’ye kadar yüksek olan sinyal seviyeleri ile -25 V Dc’ye kadar düşük olan sinyalleri taşıyabilir. Negatif gerilimler lojik “1”i pozitif gerilimler lojik “0”’ı temsil etmektedir. 
Bilgisayardaki data iletimi ikilik sistemde(binary) olmaktadır. Lojik 1’e +5V karşılık gelirken, lojik 0’a OV seviyesi denk gelir. Bu tür bir çevrime TTL (Transistor, Transistor Lojik Level) çevrimi denir. Bu, bilgisayar içindeki haberleşme standardı kabul edilir. Bilgisayar içindeki data transferlerinde TTL seviyeli sinyallerin kullanılması birkaç sebepten dolayı avantajlıdır.
Peki Neden TTL seviyesi Rs-232 uygulanmamıştır? Çünkü TTL haberleşmesinde kısa bir mesafeden sonra çok ciddi problemler ortaya çıkmaktadır, ayrıca dışarıdan gelen (yani noise)sinyallerden çok çabuk etkilenir. Dolayısıyla sinyaldeki birkaç Voltluk kayıp sinyalin belirsiz bölgeye düşmesine sebep olur.
Başarılı bir iletimin sağlanabilmesi için RS-232 sinyalleri pozitf bir sinyal için +5V ile +15 V arasında ve negatif bir sinyal içinde -5V ile-15V değer almalıdır. Bu aralığı bu şekilde tutarak, gürültüden dolayı oluşan gerilim dalgalanmalarından etkilenmesini de minimuma indirmiş oluruz. Bu şekilde bir sinyal transmitter’dan gönderildi diyelim. RS-232 receiver’ı için ise bu sinyal aralığı +3V’dan yukarısı için pozitif sinyal, -3V ve bundan aşağı için ise negatif sinyal olduğu anlaşılır.
