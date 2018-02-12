#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_263 = SymVar_0
ref_278 = ref_263 # MOV operation
ref_141565 = ref_278 # MOV operation
ref_141641 = ref_141565 # MOV operation
ref_141655 = (ref_141641 >> (0x5 & 0x3F)) # SHR operation
ref_141880 = ref_141655 # MOV operation
ref_141886 = (0x1376783EF7559EA & ref_141880) # AND operation
ref_142817 = ref_141886 # MOV operation
ref_142819 = ((ref_142817 >> 56) & 0xFF) # Byte reference - MOV operation
ref_142820 = ((ref_142817 >> 48) & 0xFF) # Byte reference - MOV operation
ref_142821 = ((ref_142817 >> 40) & 0xFF) # Byte reference - MOV operation
ref_142822 = ((ref_142817 >> 32) & 0xFF) # Byte reference - MOV operation
ref_142823 = ((ref_142817 >> 24) & 0xFF) # Byte reference - MOV operation
ref_142824 = ((ref_142817 >> 16) & 0xFF) # Byte reference - MOV operation
ref_142825 = ((ref_142817 >> 8) & 0xFF) # Byte reference - MOV operation
ref_142826 = (ref_142817 & 0xFF) # Byte reference - MOV operation
ref_143735 = ref_142817 # MOV operation
ref_143935 = ref_143735 # MOV operation
ref_143941 = (0x7063FB7 & ref_143935) # AND operation
ref_144895 = ref_278 # MOV operation
ref_144971 = ref_144895 # MOV operation
ref_144985 = (0x1A5612E2 | ref_144971) # OR operation
ref_145086 = ref_144985 # MOV operation
ref_145098 = ref_143941 # MOV operation
ref_145100 = ((ref_145098 + ref_145086) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_146032 = ref_145100 # MOV operation
ref_146034 = ((ref_146032 >> 56) & 0xFF) # Byte reference - MOV operation
ref_146035 = ((ref_146032 >> 48) & 0xFF) # Byte reference - MOV operation
ref_146036 = ((ref_146032 >> 40) & 0xFF) # Byte reference - MOV operation
ref_146037 = ((ref_146032 >> 32) & 0xFF) # Byte reference - MOV operation
ref_146038 = ((ref_146032 >> 24) & 0xFF) # Byte reference - MOV operation
ref_146039 = ((ref_146032 >> 16) & 0xFF) # Byte reference - MOV operation
ref_146040 = ((ref_146032 >> 8) & 0xFF) # Byte reference - MOV operation
ref_146041 = (ref_146032 & 0xFF) # Byte reference - MOV operation
ref_146865 = ref_278 # MOV operation
ref_147065 = ref_146865 # MOV operation
ref_147071 = ((ref_147065 - 0x2907943) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_147079 = ref_147071 # MOV operation
ref_148577 = ref_146032 # MOV operation
ref_148653 = ref_148577 # MOV operation
ref_148667 = (ref_148653 >> (0x3 & 0x3F)) # SHR operation
ref_148892 = ref_148667 # MOV operation
ref_148898 = (0xF & ref_148892) # AND operation
ref_148999 = ref_148898 # MOV operation
ref_149013 = (0x1 | ref_148999) # OR operation
ref_149126 = ref_149013 # MOV operation
ref_149128 = ((0x40 - ref_149126) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_149136 = ref_149128 # MOV operation
ref_149360 = ref_149136 # MOV operation
ref_149362 = (0x3162E74F >> ((ref_149360 & 0xFF) & 0x3F)) # SHR operation
ref_150633 = ref_146032 # MOV operation
ref_150709 = ref_150633 # MOV operation
ref_150723 = (ref_150709 >> (0x3 & 0x3F)) # SHR operation
ref_150948 = ref_150723 # MOV operation
ref_150954 = (0xF & ref_150948) # AND operation
ref_151055 = ref_150954 # MOV operation
ref_151069 = (0x1 | ref_151055) # OR operation
ref_151182 = ref_151069 # MOV operation
ref_151184 = (ref_151182 & 0xFFFFFFFF) # MOV operation
ref_151186 = ((0x3162E74F << ((ref_151184 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_151193 = ref_151186 # MOV operation
ref_151289 = ref_151193 # MOV operation
ref_151301 = ref_149362 # MOV operation
ref_151303 = (ref_151301 | ref_151289) # OR operation
ref_151404 = ref_151303 # MOV operation
ref_151418 = (ref_151404 >> (0x4 & 0x3F)) # SHR operation
ref_151643 = ref_151418 # MOV operation
ref_151649 = (0x7 & ref_151643) # AND operation
ref_151750 = ref_151649 # MOV operation
ref_151764 = (0x1 | ref_151750) # OR operation
ref_151873 = ref_147079 # MOV operation
ref_151877 = ref_151764 # MOV operation
ref_151879 = (ref_151877 & 0xFFFFFFFF) # MOV operation
ref_151881 = ((ref_151873 << ((ref_151879 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_151888 = ref_151881 # MOV operation
ref_152814 = ref_151888 # MOV operation
ref_153647 = ref_278 # MOV operation
ref_153847 = ref_153647 # MOV operation
ref_153853 = ((ref_153847 - 0x3C563FC) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_153861 = ref_153853 # MOV operation
ref_154787 = ref_153861 # MOV operation
ref_157010 = ref_146032 # MOV operation
ref_157210 = ref_157010 # MOV operation
ref_157216 = (0xF & ref_157210) # AND operation
ref_157441 = ref_157216 # MOV operation
ref_157449 = ((ref_157441 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_157456 = ref_157449 # MOV operation
ref_158374 = ref_154787 # MOV operation
ref_158450 = ref_158374 # MOV operation
ref_158462 = ref_157456 # MOV operation
ref_158464 = (ref_158462 | ref_158450) # OR operation
ref_159395 = ref_158464 # MOV operation
ref_160313 = ref_159395 # MOV operation
ref_160513 = ref_160313 # MOV operation
ref_160519 = (0x1F & ref_160513) # AND operation
ref_160744 = ref_160519 # MOV operation
ref_160752 = ((ref_160744 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_160759 = ref_160752 # MOV operation
ref_161677 = ref_152814 # MOV operation
ref_161753 = ref_161677 # MOV operation
ref_161765 = ref_160759 # MOV operation
ref_161767 = (ref_161765 | ref_161753) # OR operation
ref_162698 = ref_161767 # MOV operation
ref_163936 = ref_146032 # MOV operation
ref_164136 = ref_163936 # MOV operation
ref_164142 = (0xF & ref_164136) # AND operation
ref_164367 = ref_164142 # MOV operation
ref_164375 = ((ref_164367 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_164382 = ref_164375 # MOV operation
ref_165300 = ref_159395 # MOV operation
ref_165376 = ref_165300 # MOV operation
ref_165388 = ref_164382 # MOV operation
ref_165390 = (ref_165388 | ref_165376) # OR operation
ref_166321 = ref_165390 # MOV operation
ref_168864 = ref_166321 # MOV operation
ref_169064 = ref_168864 # MOV operation
ref_169070 = (0xF & ref_169064) # AND operation
ref_169295 = ref_169070 # MOV operation
ref_169303 = ((ref_169295 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_169310 = ref_169303 # MOV operation
ref_170228 = ref_166321 # MOV operation
ref_170304 = ref_170228 # MOV operation
ref_170316 = ref_169310 # MOV operation
ref_170318 = (ref_170316 | ref_170304) # OR operation
ref_171249 = ref_170318 # MOV operation
ref_172167 = ref_171249 # MOV operation
ref_172367 = ref_172167 # MOV operation
ref_172373 = (0x1F & ref_172367) # AND operation
ref_172598 = ref_172373 # MOV operation
ref_172606 = ((ref_172598 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_172613 = ref_172606 # MOV operation
ref_173531 = ref_162698 # MOV operation
ref_173607 = ref_173531 # MOV operation
ref_173619 = ref_172613 # MOV operation
ref_173621 = (ref_173619 | ref_173607) # OR operation
ref_174552 = ref_173621 # MOV operation
ref_174554 = ((ref_174552 >> 56) & 0xFF) # Byte reference - MOV operation
ref_174555 = ((ref_174552 >> 48) & 0xFF) # Byte reference - MOV operation
ref_174556 = ((ref_174552 >> 40) & 0xFF) # Byte reference - MOV operation
ref_174557 = ((ref_174552 >> 32) & 0xFF) # Byte reference - MOV operation
ref_174558 = ((ref_174552 >> 24) & 0xFF) # Byte reference - MOV operation
ref_174559 = ((ref_174552 >> 16) & 0xFF) # Byte reference - MOV operation
ref_174560 = ((ref_174552 >> 8) & 0xFF) # Byte reference - MOV operation
ref_174561 = (ref_174552 & 0xFF) # Byte reference - MOV operation
ref_175790 = ref_171249 # MOV operation
ref_175990 = ref_175790 # MOV operation
ref_175996 = (0xF & ref_175990) # AND operation
ref_176221 = ref_175996 # MOV operation
ref_176229 = ((ref_176221 << (0x3 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_176236 = ref_176229 # MOV operation
ref_177154 = ref_171249 # MOV operation
ref_177230 = ref_177154 # MOV operation
ref_177242 = ref_176236 # MOV operation
ref_177244 = (ref_177242 | ref_177230) # OR operation
ref_178175 = ref_177244 # MOV operation
ref_185307 = ref_174552 # MOV operation
ref_186205 = ref_174552 # MOV operation
ref_186281 = ref_186205 # MOV operation
ref_186293 = ref_185307 # MOV operation
ref_186295 = ((ref_186293 + ref_186281) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_186521 = ref_186295 # MOV operation
ref_186527 = (0x7 & ref_186521) # AND operation
ref_186752 = ref_186527 # MOV operation
ref_186760 = ((ref_186752 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_186767 = ref_186760 # MOV operation
ref_187685 = ref_178175 # MOV operation
ref_187761 = ref_187685 # MOV operation
ref_187773 = ref_186767 # MOV operation
ref_187775 = (ref_187773 | ref_187761) # OR operation
ref_188706 = ref_187775 # MOV operation
ref_190230 = ((((ref_174554) << 8 | ref_174555) << 8 | ref_174556) << 8 | ref_174557) # MOV operation
ref_190438 = (ref_190230 & 0xFFFFFFFF) # MOV operation
ref_191958 = ((((ref_174558) << 8 | ref_174559) << 8 | ref_174560) << 8 | ref_174561) # MOV operation
ref_193466 = (ref_191958 & 0xFFFFFFFF) # MOV operation
ref_193468 = (((ref_193466 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_193469 = (((ref_193466 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_193470 = (((ref_193466 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_193471 = ((ref_193466 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_193686 = (ref_190438 & 0xFFFFFFFF) # MOV operation
ref_195194 = (ref_193686 & 0xFFFFFFFF) # MOV operation
ref_195196 = (((ref_195194 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_195197 = (((ref_195194 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_195198 = (((ref_195194 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_195199 = ((ref_195194 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_196842 = ref_142821 # MOVZX operation
ref_196918 = (ref_196842 & 0xFF) # MOVZX operation
ref_199862 = ref_142822 # MOVZX operation
ref_199938 = (ref_199862 & 0xFF) # MOVZX operation
ref_199940 = (ref_199938 & 0xFF) # Byte reference - MOV operation
ref_201582 = (ref_196918 & 0xFF) # MOVZX operation
ref_201658 = (ref_201582 & 0xFF) # MOVZX operation
ref_201660 = (ref_201658 & 0xFF) # Byte reference - MOV operation
ref_203302 = ref_142820 # MOVZX operation
ref_203378 = (ref_203302 & 0xFF) # MOVZX operation
ref_206322 = ref_142826 # MOVZX operation
ref_206398 = (ref_206322 & 0xFF) # MOVZX operation
ref_206400 = (ref_206398 & 0xFF) # Byte reference - MOV operation
ref_208042 = (ref_203378 & 0xFF) # MOVZX operation
ref_208118 = (ref_208042 & 0xFF) # MOVZX operation
ref_208120 = (ref_208118 & 0xFF) # Byte reference - MOV operation
ref_209634 = ((((ref_146038) << 8 | ref_146039) << 8 | ref_146040) << 8 | ref_146041) # MOV operation
ref_209842 = (ref_209634 & 0xFFFFFFFF) # MOV operation
ref_211362 = ((((ref_146034) << 8 | ref_146035) << 8 | ref_146036) << 8 | ref_146037) # MOV operation
ref_212870 = (ref_211362 & 0xFFFFFFFF) # MOV operation
ref_212872 = (((ref_212870 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_212873 = (((ref_212870 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_212874 = (((ref_212870 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_212875 = ((ref_212870 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_213090 = (ref_209842 & 0xFFFFFFFF) # MOV operation
ref_214598 = (ref_213090 & 0xFFFFFFFF) # MOV operation
ref_214600 = (((ref_214598 & 0xFFFFFFFF) >> 24) & 0xFF) # Byte reference - MOV operation
ref_214601 = (((ref_214598 & 0xFFFFFFFF) >> 16) & 0xFF) # Byte reference - MOV operation
ref_214602 = (((ref_214598 & 0xFFFFFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_214603 = ((ref_214598 & 0xFFFFFFFF) & 0xFF) # Byte reference - MOV operation
ref_216901 = ((((((((ref_142819) << 8 | ref_206400) << 8 | ref_199940) << 8 | ref_201660) << 8 | ref_142823) << 8 | ref_142824) << 8 | ref_142825) << 8 | ref_208120) # MOV operation
ref_217101 = ref_216901 # MOV operation
ref_217107 = (0x3F & ref_217101) # AND operation
ref_217332 = ref_217107 # MOV operation
ref_217340 = ((ref_217332 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_217347 = ref_217340 # MOV operation
ref_218353 = ((((((((ref_214600) << 8 | ref_214601) << 8 | ref_214602) << 8 | ref_214603) << 8 | ref_212872) << 8 | ref_212873) << 8 | ref_212874) << 8 | ref_212875) # MOV operation
ref_218429 = ref_218353 # MOV operation
ref_218441 = ref_217347 # MOV operation
ref_218443 = (ref_218441 | ref_218429) # OR operation
ref_219462 = ref_218443 # MOV operation
ref_221846 = ref_188706 # MOV operation
ref_223092 = ref_219462 # MOV operation
ref_223168 = ref_223092 # MOV operation
ref_223182 = (ref_223168 >> (0x3 & 0x3F)) # SHR operation
ref_223407 = ref_223182 # MOV operation
ref_223413 = (0xF & ref_223407) # AND operation
ref_223514 = ref_223413 # MOV operation
ref_223528 = (0x1 | ref_223514) # OR operation
ref_223641 = ref_223528 # MOV operation
ref_223643 = ((0x40 - ref_223641) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_223651 = ref_223643 # MOV operation
ref_223755 = ref_221846 # MOV operation
ref_223759 = ref_223651 # MOV operation
ref_223761 = (ref_223759 & 0xFFFFFFFF) # MOV operation
ref_223763 = ((ref_223755 << ((ref_223761 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_223770 = ref_223763 # MOV operation
ref_224920 = ref_219462 # MOV operation
ref_224996 = ref_224920 # MOV operation
ref_225010 = (ref_224996 >> (0x3 & 0x3F)) # SHR operation
ref_225235 = ref_225010 # MOV operation
ref_225241 = (0xF & ref_225235) # AND operation
ref_225342 = ref_225241 # MOV operation
ref_225356 = (0x1 | ref_225342) # OR operation
ref_226279 = ref_188706 # MOV operation
ref_226355 = ref_226279 # MOV operation
ref_226367 = ref_225356 # MOV operation
ref_226369 = (ref_226355 >> ((ref_226367 & 0xFF) & 0x3F)) # SHR operation
ref_226470 = ref_226369 # MOV operation
ref_226482 = ref_223770 # MOV operation
ref_226484 = (ref_226482 | ref_226470) # OR operation
ref_226709 = ref_226484 # MOV operation
ref_226715 = (0xF & ref_226709) # AND operation
ref_226940 = ref_226715 # MOV operation
ref_226948 = ((ref_226940 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_226955 = ref_226948 # MOV operation
ref_227873 = ((((((((ref_193468) << 8 | ref_193469) << 8 | ref_193470) << 8 | ref_193471) << 8 | ref_195196) << 8 | ref_195197) << 8 | ref_195198) << 8 | ref_195199) # MOV operation
ref_227949 = ref_227873 # MOV operation
ref_227961 = ref_226955 # MOV operation
ref_227963 = (ref_227961 | ref_227949) # OR operation
ref_228894 = ref_227963 # MOV operation
ref_229812 = ref_188706 # MOV operation
ref_230710 = ref_228894 # MOV operation
ref_230786 = ref_230710 # MOV operation
ref_230798 = ref_229812 # MOV operation
ref_230800 = (ref_230798 | ref_230786) # OR operation
ref_231723 = ((((((((ref_142819) << 8 | ref_206400) << 8 | ref_199940) << 8 | ref_201660) << 8 | ref_142823) << 8 | ref_142824) << 8 | ref_142825) << 8 | ref_208120) # MOV operation
ref_232853 = ref_219462 # MOV operation
ref_232929 = ref_232853 # MOV operation
ref_232943 = (ref_232929 >> (0x3 & 0x3F)) # SHR operation
ref_233168 = ref_232943 # MOV operation
ref_233174 = (0x7 & ref_233168) # AND operation
ref_233275 = ref_233174 # MOV operation
ref_233289 = (0x1 | ref_233275) # OR operation
ref_233398 = ref_231723 # MOV operation
ref_233402 = ref_233289 # MOV operation
ref_233404 = (ref_233402 & 0xFFFFFFFF) # MOV operation
ref_233406 = ((ref_233398 << ((ref_233404 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_233413 = ref_233406 # MOV operation
ref_233509 = ref_233413 # MOV operation
ref_233521 = ref_230800 # MOV operation
ref_233523 = (ref_233521 | ref_233509) # OR operation
ref_234378 = ref_233523 # MOV operation
ref_234589 = ref_234378 # MOV operation
ref_234591 = ref_234589 # MOV operation

print ref_234591 & 0xffffffffffffffff