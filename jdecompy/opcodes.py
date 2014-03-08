INFINITY = -1
OPC = {}

OPC[0] = {'num_args': 0, 'name' : 'nop'}
OPC[1] = {'num_args': 0, 'name' : 'aconst_null'}
OPC[2] = {'num_args': 0, 'name' : 'iconst_m1'}
OPC[3] = {'num_args': 0, 'name' : 'iconst_0'}
OPC[4] = {'num_args': 0, 'name' : 'iconst_1'}
OPC[5] = {'num_args': 0, 'name' : 'iconst_2'}
OPC[6] = {'num_args': 0, 'name' : 'iconst_3'}
OPC[7] = {'num_args': 0, 'name' : 'iconst_4'}
OPC[8] = {'num_args': 0, 'name' : 'iconst_5'}
OPC[9] = {'num_args': 0, 'name' : 'lconst_0'}
OPC[10] = {'num_args': 0, 'name' : 'lconst_1'}
OPC[11] = {'num_args': 0, 'name' : 'fconst_0'}
OPC[12] = {'num_args': 0, 'name' : 'fconst_1'}
OPC[13] = {'num_args': 0, 'name' : 'fconst_2'}
OPC[14] = {'num_args': 0, 'name' : 'dconst_0'}
OPC[15] = {'num_args': 0, 'name' : 'dconst_1'}
OPC[16] = {'num_args': 1, 'name' : 'bipush'}
OPC[17] = {'num_args': 2, 'name' : 'sipush'}
OPC[18] = {'num_args': 1, 'name' : 'ldc'}
OPC[19] = {'num_args': 2, 'name' : 'ldc_w'}
OPC[20] = {'num_args': 2, 'name' : 'ldc2_w'}
OPC[21] = {'num_args': 1, 'name' : 'iload'}
OPC[22] = {'num_args': 1, 'name' : 'lload'}
OPC[23] = {'num_args': 1, 'name' : 'fload'}
OPC[24] = {'num_args': 1, 'name' : 'dload'}
OPC[25] = {'num_args': 1, 'name' : 'aload'}
OPC[26] = {'num_args': 0, 'name' : 'iload_0'}
OPC[27] = {'num_args': 0, 'name' : 'iload_1'}
OPC[28] = {'num_args': 0, 'name' : 'iload_2'}
OPC[29] = {'num_args': 0, 'name' : 'iload_3'}
OPC[30] = {'num_args': 0, 'name' : 'lload_0'}
OPC[31] = {'num_args': 0, 'name' : 'lload_1'}
OPC[32] = {'num_args': 0, 'name' : 'lload_2'}
OPC[33] = {'num_args': 0, 'name' : 'lload_3'}
OPC[34] = {'num_args': 0, 'name' : 'fload_0'}
OPC[35] = {'num_args': 0, 'name' : 'fload_1'}
OPC[36] = {'num_args': 0, 'name' : 'fload_2'}
OPC[37] = {'num_args': 0, 'name' : 'fload_3'}
OPC[38] = {'num_args': 0, 'name' : 'dload_0'}
OPC[39] = {'num_args': 0, 'name' : 'dload_1'}
OPC[40] = {'num_args': 0, 'name' : 'dload_2'}
OPC[41] = {'num_args': 0, 'name' : 'dload_3'}
OPC[42] = {'num_args': 0, 'name' : 'aload_0'}
OPC[43] = {'num_args': 0, 'name' : 'aload_1'}
OPC[44] = {'num_args': 0, 'name' : 'aload_2'}
OPC[45] = {'num_args': 0, 'name' : 'aload_3'}
OPC[46] = {'num_args': 0, 'name' : 'iaload'}
OPC[47] = {'num_args': 0, 'name' : 'laload'}
OPC[48] = {'num_args': 0, 'name' : 'faload'}
OPC[49] = {'num_args': 0, 'name' : 'daload'}
OPC[50] = {'num_args': 0, 'name' : 'aaload'}
OPC[51] = {'num_args': 0, 'name' : 'baload'}
OPC[52] = {'num_args': 0, 'name' : 'caload'}
OPC[53] = {'num_args': 0, 'name' : 'saload'}
OPC[54] = {'num_args': 1, 'name' : 'istore'}
OPC[55] = {'num_args': 1, 'name' : 'lstore'}
OPC[56] = {'num_args': 1, 'name' : 'fstore'}
OPC[57] = {'num_args': 1, 'name' : 'dstore'}
OPC[58] = {'num_args': 1, 'name' : 'astore'}
OPC[59] = {'num_args': 0, 'name' : 'istore_0'}
OPC[60] = {'num_args': 0, 'name' : 'istore_1'}
OPC[61] = {'num_args': 0, 'name' : 'istore_2'}
OPC[62] = {'num_args': 0, 'name' : 'istore_3'}
OPC[63] = {'num_args': 0, 'name' : 'lstore_0'}
OPC[64] = {'num_args': 0, 'name' : 'lstore_1'}
OPC[65] = {'num_args': 0, 'name' : 'lstore_2'}
OPC[66] = {'num_args': 0, 'name' : 'lstore_3'}
OPC[67] = {'num_args': 0, 'name' : 'fstore_0'}
OPC[68] = {'num_args': 0, 'name' : 'fstore_1'}
OPC[69] = {'num_args': 0, 'name' : 'fstore_2'}
OPC[70] = {'num_args': 0, 'name' : 'fstore_3'}
OPC[71] = {'num_args': 0, 'name' : 'dstore_0'}
OPC[72] = {'num_args': 0, 'name' : 'dstore_1'}
OPC[73] = {'num_args': 0, 'name' : 'dstore_2'}
OPC[74] = {'num_args': 0, 'name' : 'dstore_3'}
OPC[75] = {'num_args': 0, 'name' : 'astore_0'}
OPC[76] = {'num_args': 0, 'name' : 'astore_1'}
OPC[77] = {'num_args': 0, 'name' : 'astore_2'}
OPC[78] = {'num_args': 0, 'name' : 'astore_3'}
OPC[79] = {'num_args': 0, 'name' : 'iastore'}
OPC[80] = {'num_args': 0, 'name' : 'lastore'}
OPC[81] = {'num_args': 0, 'name' : 'fastore'}
OPC[82] = {'num_args': 0, 'name' : 'dastore'}
OPC[83] = {'num_args': 0, 'name' : 'aastore'}
OPC[84] = {'num_args': 0, 'name' : 'bastore'}
OPC[85] = {'num_args': 0, 'name' : 'castore'}
OPC[86] = {'num_args': 0, 'name' : 'sastore'}
OPC[87] = {'num_args': 0, 'name' : 'pop'}
OPC[88] = {'num_args': 0, 'name' : 'pop2'}
OPC[89] = {'num_args': 0, 'name' : 'dup'}
OPC[90] = {'num_args': 0, 'name' : 'dup_x1'}
OPC[91] = {'num_args': 0, 'name' : 'dup_x2'}
OPC[92] = {'num_args': 0, 'name' : 'dup2'}
OPC[93] = {'num_args': 0, 'name' : 'dup2_x1'}
OPC[94] = {'num_args': 0, 'name' : 'dup2_x2'}
OPC[95] = {'num_args': 0, 'name' : 'swap'}
OPC[96] = {'num_args': 0, 'name' : 'iadd'}
OPC[97] = {'num_args': 0, 'name' : 'ladd'}
OPC[98] = {'num_args': 0, 'name' : 'fadd'}
OPC[99] = {'num_args': 0, 'name' : 'dadd'}
OPC[100] = {'num_args': 0, 'name' : 'isub'}
OPC[101] = {'num_args': 0, 'name' : 'lsub'}
OPC[102] = {'num_args': 0, 'name' : 'fsub'}
OPC[103] = {'num_args': 0, 'name' : 'dsub'}
OPC[104] = {'num_args': 0, 'name' : 'imul'}
OPC[105] = {'num_args': 0, 'name' : 'lmul'}
OPC[106] = {'num_args': 0, 'name' : 'fmul'}
OPC[107] = {'num_args': 0, 'name' : 'dmul'}
OPC[108] = {'num_args': 0, 'name' : 'idiv'}
OPC[109] = {'num_args': 0, 'name' : 'ldiv'}
OPC[110] = {'num_args': 0, 'name' : 'fdiv'}
OPC[111] = {'num_args': 0, 'name' : 'ddiv'}
OPC[112] = {'num_args': 0, 'name' : 'irem'}
OPC[113] = {'num_args': 0, 'name' : 'lrem'}
OPC[114] = {'num_args': 0, 'name' : 'frem'}
OPC[115] = {'num_args': 0, 'name' : 'drem'}
OPC[116] = {'num_args': 0, 'name' : 'ineg'}
OPC[117] = {'num_args': 0, 'name' : 'lneg'}
OPC[118] = {'num_args': 0, 'name' : 'fneg'}
OPC[119] = {'num_args': 0, 'name' : 'dneg'}
OPC[120] = {'num_args': 0, 'name' : 'ishl'}
OPC[121] = {'num_args': 0, 'name' : 'lshl'}
OPC[122] = {'num_args': 0, 'name' : 'ishr'}
OPC[123] = {'num_args': 0, 'name' : 'lshr'}
OPC[124] = {'num_args': 0, 'name' : 'iushr'}
OPC[125] = {'num_args': 0, 'name' : 'lushr'}
OPC[126] = {'num_args': 0, 'name' : 'iand'}
OPC[127] = {'num_args': 0, 'name' : 'land'}
OPC[128] = {'num_args': 0, 'name' : 'ior'}
OPC[129] = {'num_args': 0, 'name' : 'lor'}
OPC[130] = {'num_args': 0, 'name' : 'ixor'}
OPC[131] = {'num_args': 0, 'name' : 'lxor'}
OPC[132] = {'num_args': 2, 'name' : 'iinc'}
OPC[133] = {'num_args': 0, 'name' : 'i2l'}
OPC[134] = {'num_args': 0, 'name' : 'i2f'}
OPC[135] = {'num_args': 0, 'name' : 'i2d'}
OPC[136] = {'num_args': 0, 'name' : 'l2i'}
OPC[137] = {'num_args': 0, 'name' : 'l2f'}
OPC[138] = {'num_args': 0, 'name' : 'l2d'}
OPC[139] = {'num_args': 0, 'name' : 'f2i'}
OPC[140] = {'num_args': 0, 'name' : 'f2l'}
OPC[141] = {'num_args': 0, 'name' : 'f2d'}
OPC[142] = {'num_args': 0, 'name' : 'd2i'}
OPC[143] = {'num_args': 0, 'name' : 'd2l'}
OPC[144] = {'num_args': 0, 'name' : 'd2f'}
OPC[145] = {'num_args': 0, 'name' : 'i2b'}
OPC[146] = {'num_args': 0, 'name' : 'i2c'}
OPC[147] = {'num_args': 0, 'name' : 'i2s'}
OPC[148] = {'num_args': 0, 'name' : 'lcmp'}
OPC[149] = {'num_args': 0, 'name' : 'fcmpl'}
OPC[150] = {'num_args': 0, 'name' : 'fcmpg'}
OPC[151] = {'num_args': 0, 'name' : 'dcmpl'}
OPC[152] = {'num_args': 0, 'name' : 'dcmpg'}
OPC[153] = {'num_args': 2, 'name' : 'ifeq'}
OPC[154] = {'num_args': 2, 'name' : 'ifne'}
OPC[155] = {'num_args': 2, 'name' : 'iflt'}
OPC[156] = {'num_args': 2, 'name' : 'ifge'}
OPC[157] = {'num_args': 2, 'name' : 'ifgt'}
OPC[158] = {'num_args': 2, 'name' : 'ifle'}
OPC[159] = {'num_args': 2, 'name' : 'if_icmpeq'}
OPC[160] = {'num_args': 2, 'name' : 'if_icmpne'}
OPC[161] = {'num_args': 2, 'name' : 'if_icmplt'}
OPC[162] = {'num_args': 2, 'name' : 'if_icmpge'}
OPC[163] = {'num_args': 2, 'name' : 'if_icmpgt'}
OPC[164] = {'num_args': 2, 'name' : 'if_icmple'}
OPC[165] = {'num_args': 2, 'name' : 'if_acmpeq'}
OPC[166] = {'num_args': 2, 'name' : 'if_acmpne'}
OPC[167] = {'num_args': 2, 'name' : 'goto'}
OPC[168] = {'num_args': 2, 'name' : 'jsr'}
OPC[169] = {'num_args': 1, 'name' : 'ret'}
OPC[170] = {'num_args': INFINITY, 'name' : 'tableswitch'}
OPC[171] = {'num_args': INFINITY, 'name' : 'lookupswitch'}
OPC[172] = {'num_args': 0, 'name' : 'ireturn'}
OPC[173] = {'num_args': 0, 'name' : 'lreturn'}
OPC[174] = {'num_args': 0, 'name' : 'freturn'}
OPC[175] = {'num_args': 0, 'name' : 'dreturn'}
OPC[176] = {'num_args': 0, 'name' : 'areturn'}
OPC[177] = {'num_args': 0, 'name' : 'return'}
OPC[178] = {'num_args': 2, 'name' : 'getstatic'}
OPC[179] = {'num_args': 2, 'name' : 'putstatic'}
OPC[180] = {'num_args': 2, 'name' : 'getfield'}
OPC[181] = {'num_args': 2, 'name' : 'putfield'}
OPC[182] = {'num_args': 2, 'name' : 'invokevirtual'}
OPC[183] = {'num_args': 2, 'name' : 'invokespecial'}
OPC[184] = {'num_args': 2, 'name' : 'invokestatic'}
OPC[185] = {'num_args': 4, 'name' : 'invokeinterface'}
OPC[186] = {'num_args': 0, 'name' : 'reserved'}
OPC[187] = {'num_args': 2, 'name' : 'new'}
OPC[188] = {'num_args': 1, 'name' : 'newarray'}
OPC[189] = {'num_args': 2, 'name' : 'anewarray'}
OPC[190] = {'num_args': 0, 'name' : 'arraylength'}
OPC[191] = {'num_args': 0, 'name' : 'athrow'}
OPC[192] = {'num_args': 2, 'name' : 'checkcast'}
OPC[193] = {'num_args': 2, 'name' : 'instanceof'}
OPC[194] = {'num_args': 0, 'name' : 'monitorenter'}
OPC[195] = {'num_args': 0, 'name' : 'monitorexit'}
OPC[196] = {'num_args': INFINITY, 'name' : 'wide'}
OPC[197] = {'num_args': 3, 'name' : 'multianewarray'}
OPC[198] = {'num_args': 2, 'name' : 'ifnull'}
OPC[199] = {'num_args': 2, 'name' : 'ifnonnull'}
OPC[200] = {'num_args': 4, 'name' : 'goto_w'}
OPC[201] = {'num_args': 4, 'name' : 'jsr_w'}
OPC[202] = {'num_args': 0, 'name' : 'breakpoint'}
OPC[203] = {'num_args': 1, 'name' : 'ldc_quick'}
OPC[204] = {'num_args': 2, 'name' : 'ldc_w_quick'}
OPC[205] = {'num_args': 2, 'name' : 'ldc2_w_quick'}
OPC[206] = {'num_args': 2, 'name' : 'getfield_quick'}
OPC[207] = {'num_args': 2, 'name' : 'putfield_quick'}
OPC[208] = {'num_args': 2, 'name' : 'getfield2_quick'}
OPC[209] = {'num_args': 2, 'name' : 'putfield2_quick'}
OPC[210] = {'num_args': 2, 'name' : 'getstatic_quick'}
OPC[211] = {'num_args': 2, 'name' : 'putstatic_quick'}
OPC[212] = {'num_args': 2, 'name' : 'getstatic2_quick'}
OPC[213] = {'num_args': 2, 'name' : 'putstatic2_quick'}
OPC[214] = {'num_args': 2, 'name' : 'invokevirtual_quick'}
OPC[215] = {'num_args': 2, 'name' : 'invokenonvirtual_quick'}
OPC[216] = {'num_args': 2, 'name' : 'invokesuper_quick'}
OPC[217] = {'num_args': 2, 'name' : 'invokestatic_quick'}
OPC[218] = {'num_args': 4, 'name' : 'invokeinterface_quick'}
OPC[219] = {'num_args': 2, 'name' : 'invokevirtualobject_quick'}
OPC[220] = {'num_args': 2, 'name' : 'invokeignored_quick'}
OPC[221] = {'num_args': 2, 'name' : 'new_quick'}
OPC[222] = {'num_args': 2, 'name' : 'anewarray_quick'}
OPC[223] = {'num_args': 3, 'name' : 'multianewarray_quick'}
OPC[224] = {'num_args': 2, 'name' : 'checkcast_quick'}
OPC[225] = {'num_args': 2, 'name' : 'instanceof_quick'}
OPC[226] = {'num_args': 2, 'name' : 'invokevirtual_quick_w'}
OPC[227] = {'num_args': 2, 'name' : 'getfield_quick_w'}
OPC[228] = {'num_args': 2, 'name' : 'putfield_quick_w'}
OPC[229] = {'num_args': 0, 'name' : 'nonnull_quick'}
OPC[230] = {'num_args': 0, 'name' : 'reserved'}
OPC[231] = {'num_args': 0, 'name' : 'reserved'}
OPC[232] = {'num_args': 0, 'name' : 'reserved'}
OPC[233] = {'num_args': 0, 'name' : 'reserved'}
OPC[234] = {'num_args': 0, 'name' : 'reserved'}
OPC[235] = {'num_args': 0, 'name' : 'reserved'}
OPC[236] = {'num_args': 0, 'name' : 'reserved'}
OPC[237] = {'num_args': 0, 'name' : 'reserved'}
OPC[238] = {'num_args': 0, 'name' : 'reserved'}
OPC[239] = {'num_args': 0, 'name' : 'reserved'}
OPC[240] = {'num_args': 0, 'name' : 'reserved'}
OPC[241] = {'num_args': 0, 'name' : 'reserved'}
OPC[242] = {'num_args': 0, 'name' : 'reserved'}
OPC[243] = {'num_args': 0, 'name' : 'reserved'}
OPC[244] = {'num_args': 0, 'name' : 'reserved'}
OPC[245] = {'num_args': 0, 'name' : 'reserved'}
OPC[246] = {'num_args': 0, 'name' : 'reserved'}
OPC[247] = {'num_args': 0, 'name' : 'reserved'}
OPC[248] = {'num_args': 0, 'name' : 'reserved'}
OPC[249] = {'num_args': 0, 'name' : 'reserved'}
OPC[250] = {'num_args': 0, 'name' : 'reserved'}
OPC[251] = {'num_args': 0, 'name' : 'reserved'}
OPC[252] = {'num_args': 0, 'name' : 'reserved'}
OPC[253] = {'num_args': 0, 'name' : 'reserved'}
OPC[254] = {'num_args': 0, 'name' : 'software'}
OPC[255] = {'num_args': 0, 'name' : 'hardware'}
