; ModuleID = ""
target triple = "x86_64-pc-linux-gnu"
target datalayout = ""

define i64 @"SECRET"(i64 %"SymVar_0") nounwind
{
.3:
  %".4" = lshr i64 %"SymVar_0", 32
  %".5" = trunc i64 %".4" to i8
  %".6" = zext i8 %".5" to i32
  %".7" = lshr i64 %"SymVar_0", 40
  %".8" = trunc i64 %".7" to i8
  %".9" = zext i8 %".8" to i32
  %".10" = shl i32 %".9", 8
  %".11" = or i32 %".6", %".10"
  %".12" = lshr i64 %"SymVar_0", 48
  %".13" = trunc i64 %".12" to i8
  %".14" = zext i8 %".13" to i32
  %".15" = shl i32 %".14", 16
  %".16" = or i32 %".11", %".15"
  %".17" = lshr i64 %"SymVar_0", 56
  %".18" = trunc i64 %".17" to i8
  %".19" = zext i8 %".18" to i32
  %".20" = shl i32 %".19", 24
  %".21" = or i32 %".16", %".20"
  %".22" = zext i32 %".21" to i64
  %".23" = trunc i64 %".22" to i32
  %".24" = zext i32 %".23" to i64
  %".25" = trunc i64 %".24" to i32
  %".26" = zext i32 %".25" to i64
  %".27" = trunc i64 %".26" to i32
  %".28" = zext i32 %".27" to i64
  %".29" = trunc i64 %"SymVar_0" to i8
  %".30" = zext i8 %".29" to i32
  %".31" = lshr i64 %"SymVar_0", 8
  %".32" = trunc i64 %".31" to i8
  %".33" = zext i8 %".32" to i32
  %".34" = shl i32 %".33", 8
  %".35" = or i32 %".30", %".34"
  %".36" = lshr i64 %"SymVar_0", 16
  %".37" = trunc i64 %".36" to i8
  %".38" = zext i8 %".37" to i32
  %".39" = shl i32 %".38", 16
  %".40" = or i32 %".35", %".39"
  %".41" = lshr i64 %"SymVar_0", 24
  %".42" = trunc i64 %".41" to i8
  %".43" = zext i8 %".42" to i32
  %".44" = shl i32 %".43", 24
  %".45" = or i32 %".40", %".44"
  %".46" = zext i32 %".45" to i64
  %".47" = trunc i64 %".46" to i32
  %".48" = zext i32 %".47" to i64
  %".49" = trunc i64 %".48" to i32
  %".50" = zext i32 %".49" to i64
  %".51" = trunc i64 %".50" to i32
  %".52" = zext i32 %".51" to i64
  %".53" = mul i64 %".52", 8
  %".54" = add i64 0, %".53"
  %".55" = add i64 0, %".54"
  %".56" = add i64 8, %".55"
  %".57" = xor i64 %".28", %".56"
  %".58" = sext i64 %".57" to i128
  %".59" = zext i8 105 to i64
  %".60" = zext i8 45 to i64
  %".61" = shl i64 %".60", 8
  %".62" = or i64 %".59", %".61"
  %".63" = zext i8 56 to i64
  %".64" = shl i64 %".63", 16
  %".65" = or i64 %".62", %".64"
  %".66" = zext i8 235 to i64
  %".67" = shl i64 %".66", 24
  %".68" = or i64 %".65", %".67"
  %".69" = zext i8 8 to i64
  %".70" = shl i64 %".69", 32
  %".71" = or i64 %".68", %".70"
  %".72" = zext i8 234 to i64
  %".73" = shl i64 %".72", 40
  %".74" = or i64 %".71", %".73"
  %".75" = zext i8 223 to i64
  %".76" = shl i64 %".75", 48
  %".77" = or i64 %".74", %".76"
  %".78" = zext i8 157 to i64
  %".79" = shl i64 %".78", 56
  %".80" = or i64 %".77", %".79"
  %".81" = sext i64 %".80" to i128
  %".82" = mul i128 %".58", %".81"
  %".83" = trunc i128 %".82" to i64
  %".84" = and i64 47, 63
  %".85" = lshr i64 %".83", %".84"
  %".86" = xor i64 %".83", %".85"
  %".87" = xor i64 %".28", %".86"
  %".88" = sext i64 %".87" to i128
  %".89" = zext i8 105 to i64
  %".90" = zext i8 45 to i64
  %".91" = shl i64 %".90", 8
  %".92" = or i64 %".89", %".91"
  %".93" = zext i8 56 to i64
  %".94" = shl i64 %".93", 16
  %".95" = or i64 %".92", %".94"
  %".96" = zext i8 235 to i64
  %".97" = shl i64 %".96", 24
  %".98" = or i64 %".95", %".97"
  %".99" = zext i8 8 to i64
  %".100" = shl i64 %".99", 32
  %".101" = or i64 %".98", %".100"
  %".102" = zext i8 234 to i64
  %".103" = shl i64 %".102", 40
  %".104" = or i64 %".101", %".103"
  %".105" = zext i8 223 to i64
  %".106" = shl i64 %".105", 48
  %".107" = or i64 %".104", %".106"
  %".108" = zext i8 157 to i64
  %".109" = shl i64 %".108", 56
  %".110" = or i64 %".107", %".109"
  %".111" = sext i64 %".110" to i128
  %".112" = mul i128 %".88", %".111"
  %".113" = trunc i128 %".112" to i64
  %".114" = and i64 47, 63
  %".115" = lshr i64 %".113", %".114"
  %".116" = xor i64 %".113", %".115"
  %".117" = sext i64 %".116" to i128
  %".118" = zext i8 105 to i64
  %".119" = zext i8 45 to i64
  %".120" = shl i64 %".119", 8
  %".121" = or i64 %".118", %".120"
  %".122" = zext i8 56 to i64
  %".123" = shl i64 %".122", 16
  %".124" = or i64 %".121", %".123"
  %".125" = zext i8 235 to i64
  %".126" = shl i64 %".125", 24
  %".127" = or i64 %".124", %".126"
  %".128" = zext i8 8 to i64
  %".129" = shl i64 %".128", 32
  %".130" = or i64 %".127", %".129"
  %".131" = zext i8 234 to i64
  %".132" = shl i64 %".131", 40
  %".133" = or i64 %".130", %".132"
  %".134" = zext i8 223 to i64
  %".135" = shl i64 %".134", 48
  %".136" = or i64 %".133", %".135"
  %".137" = zext i8 157 to i64
  %".138" = shl i64 %".137", 56
  %".139" = or i64 %".136", %".138"
  %".140" = sext i64 %".139" to i128
  %".141" = mul i128 %".117", %".140"
  %".142" = trunc i128 %".141" to i64
  ret i64 %".142"
}
