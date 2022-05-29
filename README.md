# ug-stegano

Run zad1.py script. It will encode all images in 'img' dir with messages array
from script. Encoded images will be saved in 'encoded_img' dir. Script outputs
time of execution (each encryption and decryption) as well as size comparison
before and after encryption.

Results:
=== Encoding ===

Testing method: LSB
---
test #1, message len = 4
encode time: 0.0938732624s
size before = 427926, size after = 425187 (-2739)
---
test #2, message len = 11
encode time: 0.1121904850s
size before = 427926, size after = 425229 (-2697)
---
test #3, message len = 27
encode time: 0.0792958736s
size before = 427926, size after = 425316 (-2610)
---
test #4, message len = 186
encode time: 0.1744368076s
size before = 427926, size after = 425729 (-2197)
---
test #5, message len = 5000
encode time: 0.2313752174s
size before = 427926, size after = 426234 (-1692)
---
test #6, message len = 4
encode time: 0.0468752384s
size before = 31555, size after = 31663 (+108)
---
test #7, message len = 11
encode time: 0.0291180611s
size before = 31555, size after = 31676 (+121)
---
test #8, message len = 27
encode time: 0.0280501842s
size before = 31555, size after = 31718 (+163)
---
test #9, message len = 186
encode time: 0.0175254345s
size before = 31555, size after = 31938 (+383)
---
test #10, message len = 5000
encode time: 0.1442449093s
size before = 31555, size after = 31719 (+164)
---
test #11, message len = 4
encode time: 1.3342540264s
size before = 1932070, size after = 1974617 (+42547)
---
test #12, message len = 11
encode time: 1.1304440498s
size before = 1932070, size after = 1974626 (+42556)
---
test #13, message len = 27
encode time: 1.2607665062s
size before = 1932070, size after = 1974632 (+42562)
---
test #14, message len = 186
encode time: 0.9982011318s
size before = 1932070, size after = 1974717 (+42647)
---
test #15, message len = 5000
encode time: 1.1975979805s
size before = 1932070, size after = 1973441 (+41371)
---
test #16, message len = 4
encode time: 19.3914873600s
size before = 51400850, size after = 52686866 (+1286016)
---
test #17, message len = 11
encode time: 18.6995098591s
size before = 51400850, size after = 52686921 (+1286071)
---
test #18, message len = 27
encode time: 18.8192646503s
size before = 51400850, size after = 52686980 (+1286130)
---
test #19, message len = 186
encode time: 18.5872662067s
size before = 51400850, size after = 52687539 (+1286689)
---
test #20, message len = 5000
encode time: 18.5591824055s
size before = 51400850, size after = 52689946 (+1289096)

Testing method: LSB-eratosthenes
---
test #1, message len = 4
encode time: 0.3384957314s
size before = 427926, size after = 425239 (-2687)
---
test #2, message len = 11
encode time: 0.1873788834s
size before = 427926, size after = 425328 (-2598)
---
test #3, message len = 27
encode time: 0.1871309280s
size before = 427926, size after = 425524 (-2402)
---
test #4, message len = 186
encode time: 0.1795566082s
size before = 427926, size after = 426564 (-1362)
---
test #5, message len = 5000
encode time: 0.2707228661s
size before = 427926, size after = 451813 (+23887)
---
test #6, message len = 4
encode time: 0.0277335644s
size before = 31555, size after = 31683 (+128)
---
test #7, message len = 11
encode time: 0.0278637409s
size before = 31555, size after = 31728 (+173)
---
test #8, message len = 27
encode time: 0.0276088715s
size before = 31555, size after = 31803 (+248)
---
test #9, message len = 186
encode time: 0.1160655022s
size before = 31555, size after = 32940 (+1385)
---
test #10, message len = 5000
message len 5000 too large for image size 31555
---
test #11, message len = 4
encode time: 1.3244936466s
size before = 1932070, size after = 1974614 (+42544)
---
test #12, message len = 11
encode time: 1.2610094547s
size before = 1932070, size after = 1974617 (+42547)
---
test #13, message len = 27
encode time: 1.3430528641s
size before = 1932070, size after = 1974647 (+42577)
---
test #14, message len = 186
encode time: 1.3635699749s
size before = 1932070, size after = 1974777 (+42707)
---
test #15, message len = 5000
encode time: 1.4423785210s
size before = 1932070, size after = 1978950 (+46880)
---
test #16, message len = 4
encode time: 44.2040128708s
size before = 51400850, size after = 52686899 (+1286049)
---
test #17, message len = 11
encode time: 35.5119762421s
size before = 51400850, size after = 52686971 (+1286121)
---
test #18, message len = 27
encode time: 33.3425390720s
size before = 51400850, size after = 52687158 (+1286308)
---
test #19, message len = 186
encode time: 33.7013645172s
size before = 51400850, size after = 52689379 (+1288529)
---
test #20, message len = 5000
encode time: 36.6086828709s
size before = 51400850, size after = 52723754 (+1322904)

Testing method: LSB-fibonacci
---
test #1, message len = 4
encode time: 0.4588050842s
size before = 427926, size after = 425246 (-2680)
---
test #2, message len = 11
message len 11 too large for image size 427926
---
test #3, message len = 27
message len 27 too large for image size 427926
---
test #4, message len = 186
message len 186 too large for image size 427926
---
test #5, message len = 5000
message len 5000 too large for image size 427926
---
test #6, message len = 4
encode time: 0.0927522182s
size before = 31555, size after = 31724 (+169)
---
test #7, message len = 11
message len 11 too large for image size 31555
---
test #8, message len = 27
message len 27 too large for image size 31555
---
test #9, message len = 186
message len 186 too large for image size 31555
---
test #10, message len = 5000
message len 5000 too large for image size 31555
---
test #11, message len = 4
encode time: 1.4064929485s
size before = 1932070, size after = 1974616 (+42546)
---
test #12, message len = 11
message len 11 too large for image size 1932070
---
test #13, message len = 27
message len 27 too large for image size 1932070
---
test #14, message len = 186
message len 186 too large for image size 1932070
---
test #15, message len = 5000
message len 5000 too large for image size 1932070
---
test #16, message len = 4
encode time: 33.2676296234s
size before = 51400850, size after = 52686931 (+1286081)
---
test #17, message len = 11
encode time: 33.0967295170s
size before = 51400850, size after = 52687051 (+1286201)
---
test #18, message len = 27
message len 27 too large for image size 51400850
---
test #19, message len = 186
message len 186 too large for image size 51400850
---
test #20, message len = 5000
message len 5000 too large for image size 51400850

=== Decoding ===
Testing method: LSB
---
test #1, message len = 4
image size = 425187
decode time: 0.8837954998s
---
test #2, message len = 11
image size = 425229
decode time: 0.1759741306s
---
test #3, message len = 27
image size = 425316
decode time: 0.1948642731s
---
test #4, message len = 186
image size = 425729
decode time: 0.1187407970s
---
test #5, message len = 5000
image size = 426234
decode time: 0.1886768341s
---
test #6, message len = 4
image size = 31663
decode time: 0.2089195251s
---
test #7, message len = 11
image size = 31676
decode time: 0.0974147320s
---
test #8, message len = 27
image size = 31718
decode time: 0.0754351616s
---
test #9, message len = 186
image size = 31938
decode time: 0.0651860237s
---
test #10, message len = 5000
image size = 31719
decode time: 0.1268053055s
---
test #11, message len = 4
image size = 1974617
decode time: 0.2896289825s
---
test #12, message len = 11
image size = 1974626
decode time: 0.2513196468s
---
test #13, message len = 27
image size = 1974632
decode time: 0.2179472446s
---
test #14, message len = 186
image size = 1974717
decode time: 0.1830852032s
---
test #15, message len = 5000
image size = 1973441
decode time: 0.1983270645s
---
test #16, message len = 4
image size = 52686866
decode time: 3.1841888428s
---
test #17, message len = 11
image size = 52686921
decode time: 5.5123524666s
---
test #18, message len = 27
image size = 52686980
decode time: 5.2907376289s
---
test #19, message len = 186
image size = 52687539
decode time: 3.2431807518s
---
test #20, message len = 5000
image size = 52689946
decode time: 3.1597123146s

Testing method: LSB-eratosthenes
---
test #1, message len = 4
image size = 425239
decode time: 0.1732747555s
---
test #2, message len = 11
image size = 425328
decode time: 0.2243347168s
---
test #3, message len = 27
image size = 425524
decode time: 0.1687748432s
---
test #4, message len = 186
image size = 426564
decode time: 0.1841230392s
---
test #5, message len = 5000
image size = 451813
decode time: 0.3033723831s
---
test #6, message len = 4
image size = 31683
decode time: 0.0501008034s
---
test #7, message len = 11
image size = 31728
decode time: 0.1242854595s
---
test #8, message len = 27
image size = 31803
decode time: 0.1011819839s
---
test #9, message len = 186
image size = 32940
decode time: 0.0468211174s
---
test #10, message len = 5000
missing image
---
test #11, message len = 4
image size = 1974614
decode time: 0.3405208588s
---
test #12, message len = 11
image size = 1974617
decode time: 0.3422858715s
---
test #13, message len = 27
image size = 1974647
decode time: 0.3924860954s
---
test #14, message len = 186
image size = 1974777
decode time: 0.3608305454s
---
test #15, message len = 5000
image size = 1978950
decode time: 0.4711575508s
---
test #16, message len = 4
image size = 52686899
decode time: 12.2962408066s
---
test #17, message len = 11
image size = 52686971
decode time: 11.9498965740s
---
test #18, message len = 27
image size = 52687158
decode time: 12.9389412403s
---
test #19, message len = 186
image size = 52689379
decode time: 11.6630039215s
---
test #20, message len = 5000
image size = 52723754
decode time: 16.0110900402s

Testing method: LSB-fibonacci
---
test #1, message len = 4
image size = 425246
decode time: 0.2652831078s
---
test #2, message len = 11
missing image
---
test #3, message len = 27
missing image
---
test #4, message len = 186
missing image
---
test #5, message len = 5000
missing image
---
test #6, message len = 4
image size = 31724
decode time: 0.1266610622s
---
test #7, message len = 11
missing image
---
test #8, message len = 27
missing image
---
test #9, message len = 186
missing image
---
test #10, message len = 5000
missing image
---
test #11, message len = 4
image size = 1974616
decode time: 0.4198918343s
---
test #12, message len = 11
missing image
---
test #13, message len = 27
missing image
---
test #14, message len = 186
missing image
---
test #15, message len = 5000
missing image
---
test #16, message len = 4
image size = 52686931
decode time: 11.9332549572s
---
test #17, message len = 11
image size = 52687051
decode time: 11.9375922680s
---
test #18, message len = 27
missing image
---
test #19, message len = 186
missing image
---
test #20, message len = 5000
missing image
