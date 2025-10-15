# Generated from Java20Parser.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\u0080")
        buf.write("\u0b9b\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\tL\4M\t")
        buf.write("M\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\tU\4V\t")
        buf.write("V\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\4]\t]\4^\t^\4")
        buf.write("_\t_\4`\t`\4a\ta\4b\tb\4c\tc\4d\td\4e\te\4f\tf\4g\tg\4")
        buf.write("h\th\4i\ti\4j\tj\4k\tk\4l\tl\4m\tm\4n\tn\4o\to\4p\tp\4")
        buf.write("q\tq\4r\tr\4s\ts\4t\tt\4u\tu\4v\tv\4w\tw\4x\tx\4y\ty\4")
        buf.write("z\tz\4{\t{\4|\t|\4}\t}\4~\t~\4\177\t\177\4\u0080\t\u0080")
        buf.write("\4\u0081\t\u0081\4\u0082\t\u0082\4\u0083\t\u0083\4\u0084")
        buf.write("\t\u0084\4\u0085\t\u0085\4\u0086\t\u0086\4\u0087\t\u0087")
        buf.write("\4\u0088\t\u0088\4\u0089\t\u0089\4\u008a\t\u008a\4\u008b")
        buf.write("\t\u008b\4\u008c\t\u008c\4\u008d\t\u008d\4\u008e\t\u008e")
        buf.write("\4\u008f\t\u008f\4\u0090\t\u0090\4\u0091\t\u0091\4\u0092")
        buf.write("\t\u0092\4\u0093\t\u0093\4\u0094\t\u0094\4\u0095\t\u0095")
        buf.write("\4\u0096\t\u0096\4\u0097\t\u0097\4\u0098\t\u0098\4\u0099")
        buf.write("\t\u0099\4\u009a\t\u009a\4\u009b\t\u009b\4\u009c\t\u009c")
        buf.write("\4\u009d\t\u009d\4\u009e\t\u009e\4\u009f\t\u009f\4\u00a0")
        buf.write("\t\u00a0\4\u00a1\t\u00a1\4\u00a2\t\u00a2\4\u00a3\t\u00a3")
        buf.write("\4\u00a4\t\u00a4\4\u00a5\t\u00a5\4\u00a6\t\u00a6\4\u00a7")
        buf.write("\t\u00a7\4\u00a8\t\u00a8\4\u00a9\t\u00a9\4\u00aa\t\u00aa")
        buf.write("\4\u00ab\t\u00ab\4\u00ac\t\u00ac\4\u00ad\t\u00ad\4\u00ae")
        buf.write("\t\u00ae\4\u00af\t\u00af\4\u00b0\t\u00b0\4\u00b1\t\u00b1")
        buf.write("\4\u00b2\t\u00b2\4\u00b3\t\u00b3\4\u00b4\t\u00b4\4\u00b5")
        buf.write("\t\u00b5\4\u00b6\t\u00b6\4\u00b7\t\u00b7\4\u00b8\t\u00b8")
        buf.write("\4\u00b9\t\u00b9\4\u00ba\t\u00ba\4\u00bb\t\u00bb\4\u00bc")
        buf.write("\t\u00bc\4\u00bd\t\u00bd\4\u00be\t\u00be\4\u00bf\t\u00bf")
        buf.write("\4\u00c0\t\u00c0\4\u00c1\t\u00c1\4\u00c2\t\u00c2\4\u00c3")
        buf.write("\t\u00c3\4\u00c4\t\u00c4\4\u00c5\t\u00c5\4\u00c6\t\u00c6")
        buf.write("\4\u00c7\t\u00c7\4\u00c8\t\u00c8\4\u00c9\t\u00c9\4\u00ca")
        buf.write("\t\u00ca\4\u00cb\t\u00cb\4\u00cc\t\u00cc\4\u00cd\t\u00cd")
        buf.write("\4\u00ce\t\u00ce\4\u00cf\t\u00cf\4\u00d0\t\u00d0\4\u00d1")
        buf.write("\t\u00d1\4\u00d2\t\u00d2\4\u00d3\t\u00d3\4\u00d4\t\u00d4")
        buf.write("\4\u00d5\t\u00d5\4\u00d6\t\u00d6\4\u00d7\t\u00d7\4\u00d8")
        buf.write("\t\u00d8\4\u00d9\t\u00d9\4\u00da\t\u00da\4\u00db\t\u00db")
        buf.write("\4\u00dc\t\u00dc\4\u00dd\t\u00dd\4\u00de\t\u00de\4\u00df")
        buf.write("\t\u00df\4\u00e0\t\u00e0\4\u00e1\t\u00e1\4\u00e2\t\u00e2")
        buf.write("\4\u00e3\t\u00e3\4\u00e4\t\u00e4\4\u00e5\t\u00e5\4\u00e6")
        buf.write("\t\u00e6\4\u00e7\t\u00e7\4\u00e8\t\u00e8\4\u00e9\t\u00e9")
        buf.write("\4\u00ea\t\u00ea\4\u00eb\t\u00eb\4\u00ec\t\u00ec\4\u00ed")
        buf.write("\t\u00ed\4\u00ee\t\u00ee\4\u00ef\t\u00ef\4\u00f0\t\u00f0")
        buf.write("\4\u00f1\t\u00f1\4\u00f2\t\u00f2\4\u00f3\t\u00f3\4\u00f4")
        buf.write("\t\u00f4\4\u00f5\t\u00f5\4\u00f6\t\u00f6\4\u00f7\t\u00f7")
        buf.write("\4\u00f8\t\u00f8\4\u00f9\t\u00f9\4\u00fa\t\u00fa\3\2\3")
        buf.write("\2\3\2\3\3\3\3\5\3\u01fa\n\3\3\4\3\4\5\4\u01fe\n\4\3\5")
        buf.write("\3\5\5\5\u0202\n\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n")
        buf.write("\7\n\u020d\n\n\f\n\16\n\u0210\13\n\3\n\3\n\5\n\u0214\n")
        buf.write("\n\3\13\3\13\5\13\u0218\n\13\3\f\3\f\3\r\3\r\3\16\3\16")
        buf.write("\3\16\5\16\u0221\n\16\3\17\3\17\7\17\u0225\n\17\f\17\16")
        buf.write("\17\u0228\13\17\3\17\3\17\5\17\u022c\n\17\3\17\5\17\u022f")
        buf.write("\n\17\3\20\3\20\3\20\5\20\u0234\n\20\3\20\7\20\u0237\n")
        buf.write("\20\f\20\16\20\u023a\13\20\3\20\3\20\5\20\u023e\n\20\3")
        buf.write("\20\5\20\u0241\n\20\3\21\7\21\u0244\n\21\f\21\16\21\u0247")
        buf.write("\13\21\3\21\3\21\5\21\u024b\n\21\3\21\3\21\3\21\7\21\u0250")
        buf.write("\n\21\f\21\16\21\u0253\13\21\3\21\3\21\5\21\u0257\n\21")
        buf.write("\3\21\3\21\3\21\7\21\u025c\n\21\f\21\16\21\u025f\13\21")
        buf.write("\3\21\3\21\5\21\u0263\n\21\5\21\u0265\n\21\3\22\3\22\3")
        buf.write("\23\7\23\u026a\n\23\f\23\16\23\u026d\13\23\3\23\3\23\3")
        buf.write("\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\5\24\u027a")
        buf.write("\n\24\3\25\7\25\u027d\n\25\f\25\16\25\u0280\13\25\3\25")
        buf.write("\3\25\3\25\7\25\u0285\n\25\f\25\16\25\u0288\13\25\3\25")
        buf.write("\3\25\7\25\u028c\n\25\f\25\16\25\u028f\13\25\3\26\7\26")
        buf.write("\u0292\n\26\f\26\16\26\u0295\13\26\3\26\3\26\5\26\u0299")
        buf.write("\n\26\3\27\3\27\3\30\3\30\3\30\3\30\7\30\u02a1\n\30\f")
        buf.write("\30\16\30\u02a4\13\30\5\30\u02a6\n\30\3\31\3\31\3\31\3")
        buf.write("\32\3\32\3\32\3\32\3\33\3\33\3\33\7\33\u02b2\n\33\f\33")
        buf.write("\16\33\u02b5\13\33\3\34\3\34\5\34\u02b9\n\34\3\35\7\35")
        buf.write("\u02bc\n\35\f\35\16\35\u02bf\13\35\3\35\3\35\5\35\u02c3")
        buf.write("\n\35\3\36\3\36\3\36\3\36\5\36\u02c9\n\36\3\37\3\37\3")
        buf.write("\37\5\37\u02ce\n\37\3 \3 \3 \5 \u02d3\n \3!\3!\3!\5!\u02d8")
        buf.write("\n!\3\"\3\"\3\"\5\"\u02dd\n\"\3#\3#\3#\5#\u02e2\n#\3#")
        buf.write("\3#\3$\3$\3%\3%\3%\5%\u02eb\n%\3&\3&\5&\u02ef\n&\3\'\5")
        buf.write("\'\u02f2\n\'\3\'\7\'\u02f5\n\'\f\'\16\'\u02f8\13\'\3\'")
        buf.write("\7\'\u02fb\n\'\f\'\16\'\u02fe\13\'\3(\7(\u0301\n(\f(\16")
        buf.write("(\u0304\13(\3(\3(\3)\7)\u0309\n)\f)\16)\u030c\13)\3)\3")
        buf.write(")\3)\3)\7)\u0312\n)\f)\16)\u0315\13)\3)\3)\3*\3*\3+\3")
        buf.write("+\3+\3+\5+\u031f\n+\3,\3,\3,\3,\3-\3-\3-\3-\3-\3-\3.\3")
        buf.write(".\3.\3.\3.\3.\3.\3/\3/\3/\3/\3/\3/\3/\3\60\3\60\3\60\5")
        buf.write("\60\u033c\n\60\3\61\7\61\u033f\n\61\f\61\16\61\u0342\13")
        buf.write("\61\3\61\5\61\u0345\n\61\3\61\3\61\3\61\3\61\7\61\u034b")
        buf.write("\n\61\f\61\16\61\u034e\13\61\3\61\3\61\7\61\u0352\n\61")
        buf.write("\f\61\16\61\u0355\13\61\3\61\3\61\3\62\3\62\7\62\u035b")
        buf.write("\n\62\f\62\16\62\u035e\13\62\3\62\3\62\3\62\3\62\3\62")
        buf.write("\3\62\3\62\3\62\3\62\7\62\u0369\n\62\f\62\16\62\u036c")
        buf.write("\13\62\5\62\u036e\n\62\3\62\3\62\3\62\3\62\3\62\3\62\3")
        buf.write("\62\3\62\7\62\u0378\n\62\f\62\16\62\u037b\13\62\5\62\u037d")
        buf.write("\n\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62")
        buf.write("\3\62\3\62\7\62\u038b\n\62\f\62\16\62\u038e\13\62\3\62")
        buf.write("\3\62\5\62\u0392\n\62\3\63\3\63\3\64\3\64\3\64\5\64\u0399")
        buf.write("\n\64\3\65\7\65\u039c\n\65\f\65\16\65\u039f\13\65\3\65")
        buf.write("\3\65\3\65\5\65\u03a4\n\65\3\65\5\65\u03a7\n\65\3\65\5")
        buf.write("\65\u03aa\n\65\3\65\5\65\u03ad\n\65\3\65\3\65\3\66\3\66")
        buf.write("\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\5\66\u03bb\n")
        buf.write("\66\3\67\3\67\3\67\3\67\38\38\38\78\u03c4\n8\f8\168\u03c7")
        buf.write("\138\39\39\39\3:\3:\3:\3;\3;\3;\7;\u03d2\n;\f;\16;\u03d5")
        buf.write("\13;\3<\3<\3<\3<\7<\u03db\n<\f<\16<\u03de\13<\3=\3=\7")
        buf.write("=\u03e2\n=\f=\16=\u03e5\13=\3=\3=\3>\3>\3>\3>\5>\u03ed")
        buf.write("\n>\3?\3?\3?\3?\3?\5?\u03f4\n?\3@\7@\u03f7\n@\f@\16@\u03fa")
        buf.write("\13@\3@\3@\3@\3@\3A\3A\3A\3A\3A\3A\3A\3A\5A\u0408\nA\3")
        buf.write("B\3B\3B\7B\u040d\nB\fB\16B\u0410\13B\3C\3C\3C\5C\u0415")
        buf.write("\nC\3D\3D\5D\u0419\nD\3E\3E\5E\u041d\nE\3F\3F\5F\u0421")
        buf.write("\nF\3G\3G\5G\u0425\nG\3H\3H\3H\5H\u042a\nH\3I\3I\3I\7")
        buf.write("I\u042f\nI\fI\16I\u0432\13I\5I\u0434\nI\3I\3I\5I\u0438")
        buf.write("\nI\3I\5I\u043b\nI\3J\3J\7J\u043f\nJ\fJ\16J\u0442\13J")
        buf.write("\3J\3J\5J\u0446\nJ\3J\5J\u0449\nJ\3K\3K\5K\u044d\nK\3")
        buf.write("K\3K\5K\u0451\nK\3K\3K\7K\u0455\nK\fK\16K\u0458\13K\3")
        buf.write("K\3K\5K\u045c\nK\5K\u045e\nK\3L\3L\3M\3M\3N\3N\3N\5N\u0467")
        buf.write("\nN\3N\3N\3O\7O\u046c\nO\fO\16O\u046f\13O\3O\3O\3O\3P")
        buf.write("\3P\3P\3P\3P\3P\3P\3P\3P\3P\5P\u047e\nP\3Q\3Q\7Q\u0482")
        buf.write("\nQ\fQ\16Q\u0485\13Q\5Q\u0487\nQ\3Q\3Q\3Q\5Q\u048c\nQ")
        buf.write("\3R\3R\5R\u0490\nR\3S\3S\3S\3S\3S\5S\u0497\nS\3S\5S\u049a")
        buf.write("\nS\3S\3S\5S\u049e\nS\3T\7T\u04a1\nT\fT\16T\u04a4\13T")
        buf.write("\3T\3T\3T\3T\5T\u04aa\nT\3T\3T\3U\3U\3U\7U\u04b1\nU\f")
        buf.write("U\16U\u04b4\13U\3V\7V\u04b7\nV\fV\16V\u04ba\13V\3V\3V")
        buf.write("\3V\3V\5V\u04c0\nV\3W\7W\u04c3\nW\fW\16W\u04c6\13W\3W")
        buf.write("\3W\7W\u04ca\nW\fW\16W\u04cd\13W\3W\3W\3W\3X\3X\5X\u04d4")
        buf.write("\nX\3Y\3Y\3Y\3Z\3Z\3Z\7Z\u04dc\nZ\fZ\16Z\u04df\13Z\3[")
        buf.write("\3[\5[\u04e3\n[\3\\\3\\\5\\\u04e7\n\\\3]\3]\3^\3^\3^\3")
        buf.write("_\7_\u04ef\n_\f_\16_\u04f2\13_\3_\3_\5_\u04f6\n_\3_\3")
        buf.write("_\3`\3`\3`\3`\5`\u04fe\n`\3a\5a\u0501\na\3a\3a\3a\3a\3")
        buf.write("a\5a\u0508\na\3a\5a\u050b\na\3a\3a\3b\3b\3c\3c\5c\u0513")
        buf.write("\nc\3c\5c\u0516\nc\3c\3c\3d\5d\u051b\nd\3d\3d\3d\5d\u0520")
        buf.write("\nd\3d\3d\3d\3d\5d\u0526\nd\3d\3d\5d\u052a\nd\3d\3d\3")
        buf.write("d\5d\u052f\nd\3d\3d\3d\5d\u0534\nd\3e\7e\u0537\ne\fe\16")
        buf.write("e\u053a\13e\3e\3e\3e\5e\u053f\ne\3e\3e\3f\3f\5f\u0545")
        buf.write("\nf\3f\5f\u0548\nf\3f\5f\u054b\nf\3f\3f\3g\3g\3g\7g\u0552")
        buf.write("\ng\fg\16g\u0555\13g\3h\7h\u0558\nh\fh\16h\u055b\13h\3")
        buf.write("h\3h\3h\5h\u0560\nh\3h\5h\u0563\nh\3h\5h\u0566\nh\3i\3")
        buf.write("i\3j\3j\7j\u056c\nj\fj\16j\u056f\13j\3k\7k\u0572\nk\f")
        buf.write("k\16k\u0575\13k\3k\3k\3k\5k\u057a\nk\3k\3k\5k\u057e\n")
        buf.write("k\3k\3k\3l\3l\5l\u0584\nl\3l\3l\3m\3m\3m\7m\u058b\nm\f")
        buf.write("m\16m\u058e\13m\3n\7n\u0591\nn\fn\16n\u0594\13n\3n\3n")
        buf.write("\3n\3n\5n\u059a\nn\3o\7o\u059d\no\fo\16o\u05a0\13o\3o")
        buf.write("\3o\7o\u05a4\no\fo\16o\u05a7\13o\3o\3o\3o\3p\3p\3q\3q")
        buf.write("\7q\u05b0\nq\fq\16q\u05b3\13q\3q\3q\3r\3r\5r\u05b9\nr")
        buf.write("\3s\7s\u05bc\ns\fs\16s\u05bf\13s\3s\3s\3s\3t\3t\5t\u05c6")
        buf.write("\nt\3u\7u\u05c9\nu\fu\16u\u05cc\13u\3u\3u\3u\5u\u05d1")
        buf.write("\nu\3u\5u\u05d4\nu\3u\5u\u05d7\nu\3u\3u\3v\3v\3v\3v\3")
        buf.write("v\3v\3v\3v\3v\5v\u05e4\nv\3w\3w\3w\3x\3x\3x\3x\7x\u05ed")
        buf.write("\nx\fx\16x\u05f0\13x\3y\3y\7y\u05f4\ny\fy\16y\u05f7\13")
        buf.write("y\3y\3y\3z\3z\3z\3z\3z\5z\u0600\nz\3{\7{\u0603\n{\f{\16")
        buf.write("{\u0606\13{\3{\3{\3{\3{\3|\3|\3|\3|\5|\u0610\n|\3}\7}")
        buf.write("\u0613\n}\f}\16}\u0616\13}\3}\3}\3}\3~\3~\3~\3~\3~\3~")
        buf.write("\3~\5~\u0622\n~\3\177\7\177\u0625\n\177\f\177\16\177\u0628")
        buf.write("\13\177\3\177\3\177\3\177\3\177\3\177\3\u0080\3\u0080")
        buf.write("\7\u0080\u0631\n\u0080\f\u0080\16\u0080\u0634\13\u0080")
        buf.write("\3\u0080\3\u0080\3\u0081\3\u0081\3\u0081\3\u0081\3\u0081")
        buf.write("\5\u0081\u063d\n\u0081\3\u0082\7\u0082\u0640\n\u0082\f")
        buf.write("\u0082\16\u0082\u0643\13\u0082\3\u0082\3\u0082\3\u0082")
        buf.write("\3\u0082\3\u0082\5\u0082\u064a\n\u0082\3\u0082\5\u0082")
        buf.write("\u064d\n\u0082\3\u0082\3\u0082\3\u0083\3\u0083\3\u0083")
        buf.write("\5\u0083\u0654\n\u0083\3\u0084\3\u0084\3\u0084\3\u0085")
        buf.write("\3\u0085\3\u0085\5\u0085\u065c\n\u0085\3\u0086\3\u0086")
        buf.write("\3\u0086\3\u0086\5\u0086\u0662\n\u0086\3\u0086\3\u0086")
        buf.write("\3\u0087\3\u0087\3\u0087\7\u0087\u0669\n\u0087\f\u0087")
        buf.write("\16\u0087\u066c\13\u0087\3\u0088\3\u0088\3\u0088\3\u0088")
        buf.write("\3\u0089\3\u0089\3\u0089\5\u0089\u0675\n\u0089\3\u008a")
        buf.write("\3\u008a\5\u008a\u0679\n\u008a\3\u008a\5\u008a\u067c\n")
        buf.write("\u008a\3\u008a\3\u008a\3\u008b\3\u008b\3\u008b\7\u008b")
        buf.write("\u0683\n\u008b\f\u008b\16\u008b\u0686\13\u008b\3\u008c")
        buf.write("\3\u008c\3\u008c\3\u008d\3\u008d\3\u008d\3\u008d\3\u008d")
        buf.write("\3\u008d\3\u008e\3\u008e\5\u008e\u0693\n\u008e\3\u008e")
        buf.write("\5\u008e\u0696\n\u008e\3\u008e\3\u008e\3\u008f\3\u008f")
        buf.write("\3\u008f\7\u008f\u069d\n\u008f\f\u008f\16\u008f\u06a0")
        buf.write("\13\u008f\3\u0090\3\u0090\5\u0090\u06a4\n\u0090\3\u0090")
        buf.write("\3\u0090\3\u0091\3\u0091\7\u0091\u06aa\n\u0091\f\u0091")
        buf.write("\16\u0091\u06ad\13\u0091\3\u0092\3\u0092\3\u0092\5\u0092")
        buf.write("\u06b2\n\u0092\3\u0093\3\u0093\5\u0093\u06b6\n\u0093\3")
        buf.write("\u0094\7\u0094\u06b9\n\u0094\f\u0094\16\u0094\u06bc\13")
        buf.write("\u0094\3\u0094\3\u0094\3\u0094\3\u0095\3\u0095\5\u0095")
        buf.write("\u06c3\n\u0095\3\u0096\3\u0096\3\u0096\3\u0097\3\u0097")
        buf.write("\3\u0097\3\u0097\3\u0097\3\u0097\5\u0097\u06ce\n\u0097")
        buf.write("\3\u0098\3\u0098\3\u0098\3\u0098\3\u0098\5\u0098\u06d5")
        buf.write("\n\u0098\3\u0099\3\u0099\3\u0099\3\u0099\3\u0099\3\u0099")
        buf.write("\3\u0099\3\u0099\3\u0099\3\u0099\3\u0099\3\u0099\3\u0099")
        buf.write("\5\u0099\u06e4\n\u0099\3\u009a\3\u009a\3\u009b\3\u009b")
        buf.write("\3\u009b\3\u009b\3\u009c\3\u009c\3\u009c\3\u009c\3\u009d")
        buf.write("\3\u009d\3\u009d\3\u009e\3\u009e\3\u009e\3\u009e\3\u009e")
        buf.write("\3\u009e\3\u009e\5\u009e\u06fa\n\u009e\3\u009f\3\u009f")
        buf.write("\3\u009f\3\u009f\3\u009f\3\u009f\3\u00a0\3\u00a0\3\u00a0")
        buf.write("\3\u00a0\3\u00a0\3\u00a0\3\u00a0\3\u00a0\3\u00a1\3\u00a1")
        buf.write("\3\u00a1\3\u00a1\3\u00a1\3\u00a1\3\u00a1\3\u00a1\3\u00a2")
        buf.write("\3\u00a2\3\u00a2\3\u00a2\5\u00a2\u0716\n\u00a2\3\u00a2")
        buf.write("\3\u00a2\3\u00a3\3\u00a3\3\u00a3\3\u00a3\3\u00a3\3\u00a3")
        buf.write("\3\u00a4\3\u00a4\3\u00a4\7\u00a4\u0723\n\u00a4\f\u00a4")
        buf.write("\16\u00a4\u0726\13\u00a4\3\u00a4\3\u00a4\3\u00a4\3\u00a4")
        buf.write("\7\u00a4\u072c\n\u00a4\f\u00a4\16\u00a4\u072f\13\u00a4")
        buf.write("\3\u00a4\3\u00a4\3\u00a4\7\u00a4\u0734\n\u00a4\f\u00a4")
        buf.write("\16\u00a4\u0737\13\u00a4\3\u00a4\5\u00a4\u073a\n\u00a4")
        buf.write("\3\u00a5\3\u00a5\3\u00a5\3\u00a5\3\u00a5\3\u00a5\3\u00a5")
        buf.write("\5\u00a5\u0743\n\u00a5\3\u00a6\3\u00a6\3\u00a6\3\u00a6")
        buf.write("\3\u00a6\7\u00a6\u074a\n\u00a6\f\u00a6\16\u00a6\u074d")
        buf.write("\13\u00a6\3\u00a6\3\u00a6\3\u00a7\3\u00a7\3\u00a7\3\u00a7")
        buf.write("\7\u00a7\u0755\n\u00a7\f\u00a7\16\u00a7\u0758\13\u00a7")
        buf.write("\3\u00a7\5\u00a7\u075b\n\u00a7\3\u00a8\3\u00a8\3\u00a9")
        buf.write("\3\u00a9\3\u00a9\3\u00a9\3\u00a9\3\u00a9\3\u00aa\3\u00aa")
        buf.write("\3\u00aa\3\u00aa\3\u00aa\3\u00aa\3\u00ab\3\u00ab\3\u00ab")
        buf.write("\3\u00ab\3\u00ab\3\u00ab\3\u00ab\3\u00ab\3\u00ac\3\u00ac")
        buf.write("\5\u00ac\u0775\n\u00ac\3\u00ad\3\u00ad\5\u00ad\u0779\n")
        buf.write("\u00ad\3\u00ae\3\u00ae\3\u00ae\5\u00ae\u077e\n\u00ae\3")
        buf.write("\u00ae\3\u00ae\5\u00ae\u0782\n\u00ae\3\u00ae\3\u00ae\5")
        buf.write("\u00ae\u0786\n\u00ae\3\u00ae\3\u00ae\3\u00ae\3\u00af\3")
        buf.write("\u00af\3\u00af\5\u00af\u078e\n\u00af\3\u00af\3\u00af\5")
        buf.write("\u00af\u0792\n\u00af\3\u00af\3\u00af\5\u00af\u0796\n\u00af")
        buf.write("\3\u00af\3\u00af\3\u00af\3\u00b0\3\u00b0\5\u00b0\u079d")
        buf.write("\n\u00b0\3\u00b1\3\u00b1\3\u00b2\3\u00b2\3\u00b2\7\u00b2")
        buf.write("\u07a4\n\u00b2\f\u00b2\16\u00b2\u07a7\13\u00b2\3\u00b3")
        buf.write("\3\u00b3\3\u00b3\3\u00b3\3\u00b3\3\u00b3\3\u00b3\3\u00b3")
        buf.write("\3\u00b4\3\u00b4\3\u00b4\3\u00b4\3\u00b4\3\u00b4\3\u00b4")
        buf.write("\3\u00b4\3\u00b5\3\u00b5\5\u00b5\u07bb\n\u00b5\3\u00b5")
        buf.write("\3\u00b5\3\u00b6\3\u00b6\5\u00b6\u07c1\n\u00b6\3\u00b6")
        buf.write("\3\u00b6\3\u00b7\3\u00b7\5\u00b7\u07c7\n\u00b7\3\u00b7")
        buf.write("\3\u00b7\3\u00b8\3\u00b8\3\u00b8\3\u00b8\3\u00b9\3\u00b9")
        buf.write("\3\u00b9\3\u00b9\3\u00b9\3\u00b9\3\u00ba\3\u00ba\3\u00ba")
        buf.write("\3\u00ba\3\u00ba\3\u00ba\3\u00ba\3\u00ba\3\u00ba\3\u00ba")
        buf.write("\3\u00ba\5\u00ba\u07e0\n\u00ba\3\u00ba\3\u00ba\3\u00ba")
        buf.write("\5\u00ba\u07e5\n\u00ba\3\u00bb\3\u00bb\7\u00bb\u07e9\n")
        buf.write("\u00bb\f\u00bb\16\u00bb\u07ec\13\u00bb\3\u00bc\3\u00bc")
        buf.write("\3\u00bc\3\u00bc\3\u00bc\3\u00bc\3\u00bd\7\u00bd\u07f5")
        buf.write("\n\u00bd\f\u00bd\16\u00bd\u07f8\13\u00bd\3\u00bd\3\u00bd")
        buf.write("\3\u00bd\3\u00be\3\u00be\3\u00be\7\u00be\u0800\n\u00be")
        buf.write("\f\u00be\16\u00be\u0803\13\u00be\3\u00bf\3\u00bf\3\u00bf")
        buf.write("\3\u00c0\3\u00c0\3\u00c0\3\u00c0\5\u00c0\u080c\n\u00c0")
        buf.write("\3\u00c0\5\u00c0\u080f\n\u00c0\3\u00c1\3\u00c1\3\u00c1")
        buf.write("\5\u00c1\u0814\n\u00c1\3\u00c1\3\u00c1\3\u00c2\3\u00c2")
        buf.write("\3\u00c2\7\u00c2\u081b\n\u00c2\f\u00c2\16\u00c2\u081e")
        buf.write("\13\u00c2\3\u00c3\3\u00c3\5\u00c3\u0822\n\u00c3\3\u00c4")
        buf.write("\3\u00c4\5\u00c4\u0826\n\u00c4\3\u00c5\3\u00c5\3\u00c5")
        buf.write("\3\u00c5\3\u00c6\3\u00c6\3\u00c7\3\u00c7\3\u00c8\3\u00c8")
        buf.write("\5\u00c8\u0832\n\u00c8\3\u00c9\3\u00c9\5\u00c9\u0836\n")
        buf.write("\u00c9\3\u00ca\3\u00ca\5\u00ca\u083a\n\u00ca\3\u00ca\3")
        buf.write("\u00ca\5\u00ca\u083e\n\u00ca\3\u00ca\3\u00ca\5\u00ca\u0842")
        buf.write("\n\u00ca\3\u00ca\3\u00ca\3\u00ca\3\u00ca\5\u00ca\u0848")
        buf.write("\n\u00ca\3\u00ca\3\u00ca\3\u00ca\3\u00ca\5\u00ca\u084e")
        buf.write("\n\u00ca\3\u00ca\3\u00ca\5\u00ca\u0852\n\u00ca\3\u00ca")
        buf.write("\3\u00ca\3\u00ca\3\u00ca\5\u00ca\u0858\n\u00ca\3\u00ca")
        buf.write("\3\u00ca\3\u00ca\3\u00ca\5\u00ca\u085e\n\u00ca\3\u00ca")
        buf.write("\3\u00ca\3\u00ca\3\u00ca\5\u00ca\u0864\n\u00ca\3\u00ca")
        buf.write("\3\u00ca\3\u00ca\3\u00ca\5\u00ca\u086a\n\u00ca\3\u00ca")
        buf.write("\3\u00ca\3\u00ca\3\u00ca\3\u00ca\3\u00ca\5\u00ca\u0872")
        buf.write("\n\u00ca\3\u00ca\3\u00ca\3\u00ca\3\u00ca\3\u00ca\5\u00ca")
        buf.write("\u0879\n\u00ca\3\u00ca\3\u00ca\3\u00ca\3\u00ca\3\u00ca")
        buf.write("\5\u00ca\u0880\n\u00ca\3\u00ca\3\u00ca\3\u00ca\5\u00ca")
        buf.write("\u0885\n\u00ca\3\u00ca\3\u00ca\5\u00ca\u0889\n\u00ca\3")
        buf.write("\u00ca\3\u00ca\3\u00ca\5\u00ca\u088e\n\u00ca\3\u00ca\3")
        buf.write("\u00ca\3\u00ca\5\u00ca\u0893\n\u00ca\3\u00ca\3\u00ca\5")
        buf.write("\u00ca\u0897\n\u00ca\3\u00ca\3\u00ca\3\u00ca\5\u00ca\u089c")
        buf.write("\n\u00ca\3\u00ca\3\u00ca\3\u00ca\5\u00ca\u08a1\n\u00ca")
        buf.write("\3\u00ca\3\u00ca\5\u00ca\u08a5\n\u00ca\3\u00ca\3\u00ca")
        buf.write("\3\u00ca\5\u00ca\u08aa\n\u00ca\3\u00ca\3\u00ca\3\u00ca")
        buf.write("\5\u00ca\u08af\n\u00ca\3\u00ca\3\u00ca\5\u00ca\u08b3\n")
        buf.write("\u00ca\3\u00ca\3\u00ca\3\u00ca\5\u00ca\u08b8\n\u00ca\3")
        buf.write("\u00ca\3\u00ca\3\u00ca\5\u00ca\u08bd\n\u00ca\3\u00ca\3")
        buf.write("\u00ca\5\u00ca\u08c1\n\u00ca\3\u00ca\3\u00ca\3\u00ca\3")
        buf.write("\u00ca\3\u00ca\5\u00ca\u08c8\n\u00ca\3\u00ca\3\u00ca\3")
        buf.write("\u00ca\5\u00ca\u08cd\n\u00ca\3\u00ca\3\u00ca\5\u00ca\u08d1")
        buf.write("\n\u00ca\3\u00ca\3\u00ca\3\u00ca\5\u00ca\u08d6\n\u00ca")
        buf.write("\3\u00ca\3\u00ca\5\u00ca\u08da\n\u00ca\3\u00ca\3\u00ca")
        buf.write("\3\u00ca\5\u00ca\u08df\n\u00ca\3\u00ca\3\u00ca\5\u00ca")
        buf.write("\u08e3\n\u00ca\3\u00ca\3\u00ca\3\u00ca\5\u00ca\u08e8\n")
        buf.write("\u00ca\3\u00ca\3\u00ca\5\u00ca\u08ec\n\u00ca\3\u00ca\3")
        buf.write("\u00ca\3\u00ca\5\u00ca\u08f1\n\u00ca\3\u00ca\3\u00ca\5")
        buf.write("\u00ca\u08f5\n\u00ca\3\u00ca\3\u00ca\3\u00ca\3\u00ca\3")
        buf.write("\u00ca\5\u00ca\u08fc\n\u00ca\3\u00ca\3\u00ca\5\u00ca\u0900")
        buf.write("\n\u00ca\3\u00ca\3\u00ca\3\u00ca\5\u00ca\u0905\n\u00ca")
        buf.write("\3\u00ca\3\u00ca\5\u00ca\u0909\n\u00ca\3\u00ca\3\u00ca")
        buf.write("\3\u00ca\3\u00ca\5\u00ca\u090f\n\u00ca\5\u00ca\u0911\n")
        buf.write("\u00ca\3\u00cb\3\u00cb\3\u00cb\5\u00cb\u0916\n\u00cb\3")
        buf.write("\u00cb\3\u00cb\3\u00cb\5\u00cb\u091b\n\u00cb\3\u00cb\3")
        buf.write("\u00cb\3\u00cb\3\u00cb\5\u00cb\u0921\n\u00cb\3\u00cb\3")
        buf.write("\u00cb\5\u00cb\u0925\n\u00cb\3\u00cb\3\u00cb\3\u00cb\5")
        buf.write("\u00cb\u092a\n\u00cb\3\u00cb\3\u00cb\5\u00cb\u092e\n\u00cb")
        buf.write("\3\u00cb\3\u00cb\5\u00cb\u0932\n\u00cb\3\u00cb\3\u00cb")
        buf.write("\5\u00cb\u0936\n\u00cb\5\u00cb\u0938\n\u00cb\3\u00cc\3")
        buf.write("\u00cc\3\u00cc\7\u00cc\u093d\n\u00cc\f\u00cc\16\u00cc")
        buf.write("\u0940\13\u00cc\3\u00cc\3\u00cc\3\u00cc\3\u00cc\3\u00cc")
        buf.write("\3\u00cc\7\u00cc\u0948\n\u00cc\f\u00cc\16\u00cc\u094b")
        buf.write("\13\u00cc\3\u00cc\3\u00cc\3\u00cc\3\u00cc\3\u00cc\3\u00cc")
        buf.write("\7\u00cc\u0953\n\u00cc\f\u00cc\16\u00cc\u0956\13\u00cc")
        buf.write("\3\u00cc\3\u00cc\3\u00cc\3\u00cc\3\u00cc\5\u00cc\u095d")
        buf.write("\n\u00cc\3\u00cd\3\u00cd\3\u00cd\3\u00cd\3\u00cd\3\u00cd")
        buf.write("\3\u00cd\3\u00cd\3\u00cd\5\u00cd\u0968\n\u00cd\3\u00ce")
        buf.write("\3\u00ce\5\u00ce\u096c\n\u00ce\3\u00ce\3\u00ce\3\u00ce")
        buf.write("\5\u00ce\u0971\n\u00ce\3\u00ce\3\u00ce\5\u00ce\u0975\n")
        buf.write("\u00ce\3\u00cf\7\u00cf\u0978\n\u00cf\f\u00cf\16\u00cf")
        buf.write("\u097b\13\u00cf\3\u00cf\3\u00cf\3\u00cf\7\u00cf\u0980")
        buf.write("\n\u00cf\f\u00cf\16\u00cf\u0983\13\u00cf\3\u00cf\7\u00cf")
        buf.write("\u0986\n\u00cf\f\u00cf\16\u00cf\u0989\13\u00cf\3\u00cf")
        buf.write("\5\u00cf\u098c\n\u00cf\3\u00d0\3\u00d0\5\u00d0\u0990\n")
        buf.write("\u00d0\3\u00d1\3\u00d1\5\u00d1\u0994\n\u00d1\3\u00d2\3")
        buf.write("\u00d2\3\u00d2\3\u00d2\5\u00d2\u099a\n\u00d2\3\u00d2\3")
        buf.write("\u00d2\3\u00d2\3\u00d2\5\u00d2\u09a0\n\u00d2\5\u00d2\u09a2")
        buf.write("\n\u00d2\3\u00d3\3\u00d3\3\u00d3\3\u00d3\3\u00d3\3\u00d3")
        buf.write("\3\u00d3\3\u00d3\3\u00d3\3\u00d3\5\u00d3\u09ae\n\u00d3")
        buf.write("\3\u00d4\3\u00d4\7\u00d4\u09b2\n\u00d4\f\u00d4\16\u00d4")
        buf.write("\u09b5\13\u00d4\3\u00d5\7\u00d5\u09b8\n\u00d5\f\u00d5")
        buf.write("\16\u00d5\u09bb\13\u00d5\3\u00d5\3\u00d5\3\u00d5\3\u00d5")
        buf.write("\3\u00d6\3\u00d6\3\u00d6\3\u00d6\3\u00d6\3\u00d6\3\u00d6")
        buf.write("\3\u00d6\3\u00d6\3\u00d6\3\u00d6\3\u00d6\3\u00d6\3\u00d6")
        buf.write("\3\u00d6\5\u00d6\u09d0\n\u00d6\3\u00d7\3\u00d7\3\u00d7")
        buf.write("\3\u00d7\3\u00d7\3\u00d7\3\u00d7\3\u00d7\3\u00d7\3\u00d7")
        buf.write("\3\u00d7\3\u00d7\3\u00d7\5\u00d7\u09df\n\u00d7\3\u00d8")
        buf.write("\3\u00d8\3\u00d8\5\u00d8\u09e4\n\u00d8\3\u00d8\3\u00d8")
        buf.write("\3\u00d8\3\u00d8\3\u00d8\5\u00d8\u09eb\n\u00d8\3\u00d8")
        buf.write("\3\u00d8\3\u00d8\5\u00d8\u09f0\n\u00d8\3\u00d8\3\u00d8")
        buf.write("\3\u00d8\3\u00d8\3\u00d8\5\u00d8\u09f7\n\u00d8\3\u00d8")
        buf.write("\3\u00d8\3\u00d8\5\u00d8\u09fc\n\u00d8\3\u00d8\3\u00d8")
        buf.write("\3\u00d8\3\u00d8\3\u00d8\5\u00d8\u0a03\n\u00d8\3\u00d8")
        buf.write("\3\u00d8\3\u00d8\5\u00d8\u0a08\n\u00d8\3\u00d8\3\u00d8")
        buf.write("\3\u00d8\3\u00d8\3\u00d8\5\u00d8\u0a0f\n\u00d8\3\u00d8")
        buf.write("\3\u00d8\3\u00d8\5\u00d8\u0a14\n\u00d8\3\u00d8\3\u00d8")
        buf.write("\3\u00d8\3\u00d8\3\u00d8\3\u00d8\3\u00d8\5\u00d8\u0a1d")
        buf.write("\n\u00d8\3\u00d8\3\u00d8\3\u00d8\5\u00d8\u0a22\n\u00d8")
        buf.write("\3\u00d8\3\u00d8\5\u00d8\u0a26\n\u00d8\3\u00d9\3\u00d9")
        buf.write("\3\u00d9\7\u00d9\u0a2b\n\u00d9\f\u00d9\16\u00d9\u0a2e")
        buf.write("\13\u00d9\3\u00da\3\u00da\3\u00da\5\u00da\u0a33\n\u00da")
        buf.write("\3\u00da\3\u00da\3\u00da\3\u00da\3\u00da\5\u00da\u0a3a")
        buf.write("\n\u00da\3\u00da\3\u00da\3\u00da\3\u00da\3\u00da\5\u00da")
        buf.write("\u0a41\n\u00da\3\u00da\3\u00da\3\u00da\3\u00da\3\u00da")
        buf.write("\5\u00da\u0a48\n\u00da\3\u00da\3\u00da\3\u00da\3\u00da")
        buf.write("\3\u00da\3\u00da\5\u00da\u0a50\n\u00da\3\u00da\3\u00da")
        buf.write("\3\u00da\3\u00da\3\u00da\5\u00da\u0a57\n\u00da\3\u00da")
        buf.write("\3\u00da\3\u00da\3\u00da\3\u00da\3\u00da\5\u00da\u0a5f")
        buf.write("\n\u00da\3\u00db\3\u00db\5\u00db\u0a63\n\u00db\3\u00db")
        buf.write("\3\u00db\5\u00db\u0a67\n\u00db\5\u00db\u0a69\n\u00db\3")
        buf.write("\u00dc\3\u00dc\5\u00dc\u0a6d\n\u00dc\3\u00dc\3\u00dc\5")
        buf.write("\u00dc\u0a71\n\u00dc\5\u00dc\u0a73\n\u00dc\3\u00dd\3\u00dd")
        buf.write("\3\u00dd\3\u00de\3\u00de\3\u00de\3\u00df\3\u00df\3\u00df")
        buf.write("\3\u00df\3\u00df\3\u00df\3\u00df\5\u00df\u0a82\n\u00df")
        buf.write("\3\u00e0\3\u00e0\3\u00e0\3\u00e1\3\u00e1\3\u00e1\3\u00e2")
        buf.write("\3\u00e2\3\u00e2\3\u00e2\3\u00e2\3\u00e2\3\u00e2\5\u00e2")
        buf.write("\u0a91\n\u00e2\3\u00e3\3\u00e3\3\u00e3\3\u00e3\3\u00e3")
        buf.write("\3\u00e3\3\u00e3\3\u00e3\7\u00e3\u0a9b\n\u00e3\f\u00e3")
        buf.write("\16\u00e3\u0a9e\13\u00e3\3\u00e3\3\u00e3\3\u00e3\3\u00e3")
        buf.write("\3\u00e3\3\u00e3\7\u00e3\u0aa6\n\u00e3\f\u00e3\16\u00e3")
        buf.write("\u0aa9\13\u00e3\3\u00e3\3\u00e3\3\u00e3\5\u00e3\u0aae")
        buf.write("\n\u00e3\3\u00e4\3\u00e4\3\u00e4\3\u00e4\3\u00e4\3\u00e4")
        buf.write("\3\u00e4\3\u00e4\3\u00e4\3\u00e4\3\u00e4\3\u00e4\7\u00e4")
        buf.write("\u0abc\n\u00e4\f\u00e4\16\u00e4\u0abf\13\u00e4\3\u00e5")
        buf.write("\3\u00e5\3\u00e5\3\u00e5\3\u00e5\3\u00e5\3\u00e5\3\u00e5")
        buf.write("\3\u00e5\7\u00e5\u0aca\n\u00e5\f\u00e5\16\u00e5\u0acd")
        buf.write("\13\u00e5\3\u00e6\3\u00e6\3\u00e6\3\u00e6\3\u00e6\3\u00e6")
        buf.write("\3\u00e6\3\u00e6\3\u00e6\3\u00e6\3\u00e6\3\u00e6\3\u00e6")
        buf.write("\3\u00e6\3\u00e6\3\u00e6\7\u00e6\u0adf\n\u00e6\f\u00e6")
        buf.write("\16\u00e6\u0ae2\13\u00e6\3\u00e7\3\u00e7\3\u00e7\3\u00e7")
        buf.write("\3\u00e7\3\u00e7\3\u00e7\3\u00e7\3\u00e7\3\u00e7\3\u00e7")
        buf.write("\3\u00e7\3\u00e7\3\u00e7\3\u00e7\3\u00e7\3\u00e7\3\u00e7")
        buf.write("\3\u00e7\5\u00e7\u0af7\n\u00e7\7\u00e7\u0af9\n\u00e7\f")
        buf.write("\u00e7\16\u00e7\u0afc\13\u00e7\3\u00e8\3\u00e8\3\u00e8")
        buf.write("\3\u00e8\3\u00e8\3\u00e8\3\u00e8\3\u00e8\3\u00e8\7\u00e8")
        buf.write("\u0b07\n\u00e8\f\u00e8\16\u00e8\u0b0a\13\u00e8\3\u00e9")
        buf.write("\3\u00e9\3\u00e9\3\u00e9\3\u00e9\3\u00e9\7\u00e9\u0b12")
        buf.write("\n\u00e9\f\u00e9\16\u00e9\u0b15\13\u00e9\3\u00ea\3\u00ea")
        buf.write("\3\u00ea\3\u00ea\3\u00ea\3\u00ea\7\u00ea\u0b1d\n\u00ea")
        buf.write("\f\u00ea\16\u00ea\u0b20\13\u00ea\3\u00eb\3\u00eb\3\u00eb")
        buf.write("\3\u00eb\3\u00eb\3\u00eb\7\u00eb\u0b28\n\u00eb\f\u00eb")
        buf.write("\16\u00eb\u0b2b\13\u00eb\3\u00ec\3\u00ec\3\u00ec\3\u00ec")
        buf.write("\3\u00ec\3\u00ec\7\u00ec\u0b33\n\u00ec\f\u00ec\16\u00ec")
        buf.write("\u0b36\13\u00ec\3\u00ed\3\u00ed\3\u00ed\3\u00ed\3\u00ed")
        buf.write("\3\u00ed\7\u00ed\u0b3e\n\u00ed\f\u00ed\16\u00ed\u0b41")
        buf.write("\13\u00ed\3\u00ee\3\u00ee\3\u00ee\3\u00ee\3\u00ee\3\u00ee")
        buf.write("\3\u00ee\3\u00ee\3\u00ee\3\u00ee\3\u00ee\3\u00ee\3\u00ee")
        buf.write("\5\u00ee\u0b50\n\u00ee\3\u00ef\3\u00ef\5\u00ef\u0b54\n")
        buf.write("\u00ef\3\u00f0\3\u00f0\3\u00f0\3\u00f0\3\u00f1\3\u00f1")
        buf.write("\3\u00f1\5\u00f1\u0b5d\n\u00f1\3\u00f2\3\u00f2\3\u00f3")
        buf.write("\3\u00f3\3\u00f3\3\u00f3\3\u00f4\3\u00f4\5\u00f4\u0b67")
        buf.write("\n\u00f4\3\u00f4\3\u00f4\5\u00f4\u0b6b\n\u00f4\3\u00f5")
        buf.write("\3\u00f5\3\u00f5\7\u00f5\u0b70\n\u00f5\f\u00f5\16\u00f5")
        buf.write("\u0b73\13\u00f5\3\u00f5\3\u00f5\3\u00f5\7\u00f5\u0b78")
        buf.write("\n\u00f5\f\u00f5\16\u00f5\u0b7b\13\u00f5\5\u00f5\u0b7d")
        buf.write("\n\u00f5\3\u00f6\7\u00f6\u0b80\n\u00f6\f\u00f6\16\u00f6")
        buf.write("\u0b83\13\u00f6\3\u00f6\3\u00f6\3\u00f6\3\u00f6\5\u00f6")
        buf.write("\u0b89\n\u00f6\3\u00f7\3\u00f7\5\u00f7\u0b8d\n\u00f7\3")
        buf.write("\u00f8\3\u00f8\5\u00f8\u0b91\n\u00f8\3\u00f9\3\u00f9\3")
        buf.write("\u00f9\3\u00f9\3\u00f9\3\u00f9\3\u00fa\3\u00fa\3\u00fa")
        buf.write("\2\f\u01c6\u01c8\u01ca\u01cc\u01ce\u01d0\u01d2\u01d4\u01d6")
        buf.write("\u01d8\u00fb\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"")
        buf.write("$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz")
        buf.write("|~\u0080\u0082\u0084\u0086\u0088\u008a\u008c\u008e\u0090")
        buf.write("\u0092\u0094\u0096\u0098\u009a\u009c\u009e\u00a0\u00a2")
        buf.write("\u00a4\u00a6\u00a8\u00aa\u00ac\u00ae\u00b0\u00b2\u00b4")
        buf.write("\u00b6\u00b8\u00ba\u00bc\u00be\u00c0\u00c2\u00c4\u00c6")
        buf.write("\u00c8\u00ca\u00cc\u00ce\u00d0\u00d2\u00d4\u00d6\u00d8")
        buf.write("\u00da\u00dc\u00de\u00e0\u00e2\u00e4\u00e6\u00e8\u00ea")
        buf.write("\u00ec\u00ee\u00f0\u00f2\u00f4\u00f6\u00f8\u00fa\u00fc")
        buf.write("\u00fe\u0100\u0102\u0104\u0106\u0108\u010a\u010c\u010e")
        buf.write("\u0110\u0112\u0114\u0116\u0118\u011a\u011c\u011e\u0120")
        buf.write("\u0122\u0124\u0126\u0128\u012a\u012c\u012e\u0130\u0132")
        buf.write("\u0134\u0136\u0138\u013a\u013c\u013e\u0140\u0142\u0144")
        buf.write("\u0146\u0148\u014a\u014c\u014e\u0150\u0152\u0154\u0156")
        buf.write("\u0158\u015a\u015c\u015e\u0160\u0162\u0164\u0166\u0168")
        buf.write("\u016a\u016c\u016e\u0170\u0172\u0174\u0176\u0178\u017a")
        buf.write("\u017c\u017e\u0180\u0182\u0184\u0186\u0188\u018a\u018c")
        buf.write("\u018e\u0190\u0192\u0194\u0196\u0198\u019a\u019c\u019e")
        buf.write("\u01a0\u01a2\u01a4\u01a6\u01a8\u01aa\u01ac\u01ae\u01b0")
        buf.write("\u01b2\u01b4\u01b6\u01b8\u01ba\u01bc\u01be\u01c0\u01c2")
        buf.write("\u01c4\u01c6\u01c8\u01ca\u01cc\u01ce\u01d0\u01d2\u01d4")
        buf.write("\u01d6\u01d8\u01da\u01dc\u01de\u01e0\u01e2\u01e4\u01e6")
        buf.write("\u01e8\u01ea\u01ec\u01ee\u01f0\u01f2\2\13\4\2\3\5\7\23")
        buf.write("\b\2\3\5\7\b\n\n\f\f\16\20\22\22\4\2\3\5\7\22\3\2GM\7")
        buf.write("\2\30\30\33\33..\60\6088\4\2!!\'\'\4\2\17\1799\4\2;;>")
        buf.write(">\4\2ZZr|\2\u0c9d\2\u01f4\3\2\2\2\4\u01f9\3\2\2\2\6\u01fd")
        buf.write("\3\2\2\2\b\u0201\3\2\2\2\n\u0203\3\2\2\2\f\u0205\3\2\2")
        buf.write("\2\16\u0207\3\2\2\2\20\u0209\3\2\2\2\22\u020e\3\2\2\2")
        buf.write("\24\u0217\3\2\2\2\26\u0219\3\2\2\2\30\u021b\3\2\2\2\32")
        buf.write("\u0220\3\2\2\2\34\u0222\3\2\2\2\36\u0233\3\2\2\2 \u0264")
        buf.write("\3\2\2\2\"\u0266\3\2\2\2$\u026b\3\2\2\2&\u0279\3\2\2\2")
        buf.write("(\u027e\3\2\2\2*\u0293\3\2\2\2,\u029a\3\2\2\2.\u029c\3")
        buf.write("\2\2\2\60\u02a7\3\2\2\2\62\u02aa\3\2\2\2\64\u02ae\3\2")
        buf.write("\2\2\66\u02b8\3\2\2\28\u02bd\3\2\2\2:\u02c8\3\2\2\2<\u02ca")
        buf.write("\3\2\2\2>\u02cf\3\2\2\2@\u02d4\3\2\2\2B\u02d9\3\2\2\2")
        buf.write("D\u02e1\3\2\2\2F\u02e5\3\2\2\2H\u02e7\3\2\2\2J\u02ee\3")
        buf.write("\2\2\2L\u02f1\3\2\2\2N\u0302\3\2\2\2P\u030a\3\2\2\2R\u0318")
        buf.write("\3\2\2\2T\u031e\3\2\2\2V\u0320\3\2\2\2X\u0324\3\2\2\2")
        buf.write("Z\u032a\3\2\2\2\\\u0331\3\2\2\2^\u033b\3\2\2\2`\u0340")
        buf.write("\3\2\2\2b\u0391\3\2\2\2d\u0393\3\2\2\2f\u0398\3\2\2\2")
        buf.write("h\u039d\3\2\2\2j\u03ba\3\2\2\2l\u03bc\3\2\2\2n\u03c0\3")
        buf.write("\2\2\2p\u03c8\3\2\2\2r\u03cb\3\2\2\2t\u03ce\3\2\2\2v\u03d6")
        buf.write("\3\2\2\2x\u03df\3\2\2\2z\u03ec\3\2\2\2|\u03f3\3\2\2\2")
        buf.write("~\u03f8\3\2\2\2\u0080\u0407\3\2\2\2\u0082\u0409\3\2\2")
        buf.write("\2\u0084\u0411\3\2\2\2\u0086\u0416\3\2\2\2\u0088\u041c")
        buf.write("\3\2\2\2\u008a\u0420\3\2\2\2\u008c\u0424\3\2\2\2\u008e")
        buf.write("\u0429\3\2\2\2\u0090\u0433\3\2\2\2\u0092\u043c\3\2\2\2")
        buf.write("\u0094\u045d\3\2\2\2\u0096\u045f\3\2\2\2\u0098\u0461\3")
        buf.write("\2\2\2\u009a\u0466\3\2\2\2\u009c\u046d\3\2\2\2\u009e\u047d")
        buf.write("\3\2\2\2\u00a0\u0486\3\2\2\2\u00a2\u048f\3\2\2\2\u00a4")
        buf.write("\u0491\3\2\2\2\u00a6\u04a2\3\2\2\2\u00a8\u04ad\3\2\2\2")
        buf.write("\u00aa\u04bf\3\2\2\2\u00ac\u04c4\3\2\2\2\u00ae\u04d3\3")
        buf.write("\2\2\2\u00b0\u04d5\3\2\2\2\u00b2\u04d8\3\2\2\2\u00b4\u04e2")
        buf.write("\3\2\2\2\u00b6\u04e6\3\2\2\2\u00b8\u04e8\3\2\2\2\u00ba")
        buf.write("\u04ea\3\2\2\2\u00bc\u04f0\3\2\2\2\u00be\u04fd\3\2\2\2")
        buf.write("\u00c0\u0500\3\2\2\2\u00c2\u050e\3\2\2\2\u00c4\u0510\3")
        buf.write("\2\2\2\u00c6\u0533\3\2\2\2\u00c8\u0538\3\2\2\2\u00ca\u0542")
        buf.write("\3\2\2\2\u00cc\u054e\3\2\2\2\u00ce\u0559\3\2\2\2\u00d0")
        buf.write("\u0567\3\2\2\2\u00d2\u0569\3\2\2\2\u00d4\u0573\3\2\2\2")
        buf.write("\u00d6\u0581\3\2\2\2\u00d8\u0587\3\2\2\2\u00da\u0599\3")
        buf.write("\2\2\2\u00dc\u059e\3\2\2\2\u00de\u05ab\3\2\2\2\u00e0\u05ad")
        buf.write("\3\2\2\2\u00e2\u05b8\3\2\2\2\u00e4\u05bd\3\2\2\2\u00e6")
        buf.write("\u05c5\3\2\2\2\u00e8\u05ca\3\2\2\2\u00ea\u05e3\3\2\2\2")
        buf.write("\u00ec\u05e5\3\2\2\2\u00ee\u05e8\3\2\2\2\u00f0\u05f1\3")
        buf.write("\2\2\2\u00f2\u05ff\3\2\2\2\u00f4\u0604\3\2\2\2\u00f6\u060f")
        buf.write("\3\2\2\2\u00f8\u0614\3\2\2\2\u00fa\u0621\3\2\2\2\u00fc")
        buf.write("\u0626\3\2\2\2\u00fe\u062e\3\2\2\2\u0100\u063c\3\2\2\2")
        buf.write("\u0102\u0641\3\2\2\2\u0104\u0653\3\2\2\2\u0106\u0655\3")
        buf.write("\2\2\2\u0108\u065b\3\2\2\2\u010a\u065d\3\2\2\2\u010c\u0665")
        buf.write("\3\2\2\2\u010e\u066d\3\2\2\2\u0110\u0674\3\2\2\2\u0112")
        buf.write("\u0676\3\2\2\2\u0114\u067f\3\2\2\2\u0116\u0687\3\2\2\2")
        buf.write("\u0118\u068a\3\2\2\2\u011a\u0690\3\2\2\2\u011c\u0699\3")
        buf.write("\2\2\2\u011e\u06a1\3\2\2\2\u0120\u06a7\3\2\2\2\u0122\u06b1")
        buf.write("\3\2\2\2\u0124\u06b5\3\2\2\2\u0126\u06ba\3\2\2\2\u0128")
        buf.write("\u06c2\3\2\2\2\u012a\u06c4\3\2\2\2\u012c\u06cd\3\2\2\2")
        buf.write("\u012e\u06d4\3\2\2\2\u0130\u06e3\3\2\2\2\u0132\u06e5\3")
        buf.write("\2\2\2\u0134\u06e7\3\2\2\2\u0136\u06eb\3\2\2\2\u0138\u06ef")
        buf.write("\3\2\2\2\u013a\u06f9\3\2\2\2\u013c\u06fb\3\2\2\2\u013e")
        buf.write("\u0701\3\2\2\2\u0140\u0709\3\2\2\2\u0142\u0711\3\2\2\2")
        buf.write("\u0144\u0719\3\2\2\2\u0146\u0739\3\2\2\2\u0148\u073b\3")
        buf.write("\2\2\2\u014a\u0744\3\2\2\2\u014c\u075a\3\2\2\2\u014e\u075c")
        buf.write("\3\2\2\2\u0150\u075e\3\2\2\2\u0152\u0764\3\2\2\2\u0154")
        buf.write("\u076a\3\2\2\2\u0156\u0774\3\2\2\2\u0158\u0778\3\2\2\2")
        buf.write("\u015a\u077a\3\2\2\2\u015c\u078a\3\2\2\2\u015e\u079c\3")
        buf.write("\2\2\2\u0160\u079e\3\2\2\2\u0162\u07a0\3\2\2\2\u0164\u07a8")
        buf.write("\3\2\2\2\u0166\u07b0\3\2\2\2\u0168\u07b8\3\2\2\2\u016a")
        buf.write("\u07be\3\2\2\2\u016c\u07c4\3\2\2\2\u016e\u07ca\3\2\2\2")
        buf.write("\u0170\u07ce\3\2\2\2\u0172\u07e4\3\2\2\2\u0174\u07e6\3")
        buf.write("\2\2\2\u0176\u07ed\3\2\2\2\u0178\u07f6\3\2\2\2\u017a\u07fc")
        buf.write("\3\2\2\2\u017c\u0804\3\2\2\2\u017e\u0807\3\2\2\2\u0180")
        buf.write("\u0810\3\2\2\2\u0182\u0817\3\2\2\2\u0184\u0821\3\2\2\2")
        buf.write("\u0186\u0825\3\2\2\2\u0188\u0827\3\2\2\2\u018a\u082b\3")
        buf.write("\2\2\2\u018c\u082d\3\2\2\2\u018e\u0831\3\2\2\2\u0190\u0835")
        buf.write("\3\2\2\2\u0192\u0910\3\2\2\2\u0194\u0937\3\2\2\2\u0196")
        buf.write("\u095c\3\2\2\2\u0198\u0967\3\2\2\2\u019a\u0969\3\2\2\2")
        buf.write("\u019c\u0979\3\2\2\2\u019e\u098f\3\2\2\2\u01a0\u0993\3")
        buf.write("\2\2\2\u01a2\u09a1\3\2\2\2\u01a4\u09ad\3\2\2\2\u01a6\u09af")
        buf.write("\3\2\2\2\u01a8\u09b9\3\2\2\2\u01aa\u09cf\3\2\2\2\u01ac")
        buf.write("\u09de\3\2\2\2\u01ae\u0a25\3\2\2\2\u01b0\u0a27\3\2\2\2")
        buf.write("\u01b2\u0a5e\3\2\2\2\u01b4\u0a68\3\2\2\2\u01b6\u0a72\3")
        buf.write("\2\2\2\u01b8\u0a74\3\2\2\2\u01ba\u0a77\3\2\2\2\u01bc\u0a81")
        buf.write("\3\2\2\2\u01be\u0a83\3\2\2\2\u01c0\u0a86\3\2\2\2\u01c2")
        buf.write("\u0a90\3\2\2\2\u01c4\u0aad\3\2\2\2\u01c6\u0aaf\3\2\2\2")
        buf.write("\u01c8\u0ac0\3\2\2\2\u01ca\u0ace\3\2\2\2\u01cc\u0ae3\3")
        buf.write("\2\2\2\u01ce\u0afd\3\2\2\2\u01d0\u0b0b\3\2\2\2\u01d2\u0b16")
        buf.write("\3\2\2\2\u01d4\u0b21\3\2\2\2\u01d6\u0b2c\3\2\2\2\u01d8")
        buf.write("\u0b37\3\2\2\2\u01da\u0b4f\3\2\2\2\u01dc\u0b53\3\2\2\2")
        buf.write("\u01de\u0b55\3\2\2\2\u01e0\u0b5c\3\2\2\2\u01e2\u0b5e\3")
        buf.write("\2\2\2\u01e4\u0b60\3\2\2\2\u01e6\u0b6a\3\2\2\2\u01e8\u0b7c")
        buf.write("\3\2\2\2\u01ea\u0b88\3\2\2\2\u01ec\u0b8c\3\2\2\2\u01ee")
        buf.write("\u0b90\3\2\2\2\u01f0\u0b92\3\2\2\2\u01f2\u0b98\3\2\2\2")
        buf.write("\u01f4\u01f5\5J&\2\u01f5\u01f6\7\2\2\3\u01f6\3\3\2\2\2")
        buf.write("\u01f7\u01fa\7}\2\2\u01f8\u01fa\5\n\6\2\u01f9\u01f7\3")
        buf.write("\2\2\2\u01f9\u01f8\3\2\2\2\u01fa\5\3\2\2\2\u01fb\u01fe")
        buf.write("\7}\2\2\u01fc\u01fe\5\f\7\2\u01fd\u01fb\3\2\2\2\u01fd")
        buf.write("\u01fc\3\2\2\2\u01fe\7\3\2\2\2\u01ff\u0202\7}\2\2\u0200")
        buf.write("\u0202\5\16\b\2\u0201\u01ff\3\2\2\2\u0201\u0200\3\2\2")
        buf.write("\2\u0202\t\3\2\2\2\u0203\u0204\t\2\2\2\u0204\13\3\2\2")
        buf.write("\2\u0205\u0206\t\3\2\2\u0206\r\3\2\2\2\u0207\u0208\t\4")
        buf.write("\2\2\u0208\17\3\2\2\2\u0209\u020a\t\5\2\2\u020a\21\3\2")
        buf.write("\2\2\u020b\u020d\5\u0108\u0085\2\u020c\u020b\3\2\2\2\u020d")
        buf.write("\u0210\3\2\2\2\u020e\u020c\3\2\2\2\u020e\u020f\3\2\2\2")
        buf.write("\u020f\u0213\3\2\2\2\u0210\u020e\3\2\2\2\u0211\u0214\5")
        buf.write("\24\13\2\u0212\u0214\7\26\2\2\u0213\u0211\3\2\2\2\u0213")
        buf.write("\u0212\3\2\2\2\u0214\23\3\2\2\2\u0215\u0218\5\26\f\2\u0216")
        buf.write("\u0218\5\30\r\2\u0217\u0215\3\2\2\2\u0217\u0216\3\2\2")
        buf.write("\2\u0218\25\3\2\2\2\u0219\u021a\t\6\2\2\u021a\27\3\2\2")
        buf.write("\2\u021b\u021c\t\7\2\2\u021c\31\3\2\2\2\u021d\u0221\5")
        buf.write("\36\20\2\u021e\u0221\5$\23\2\u021f\u0221\5&\24\2\u0220")
        buf.write("\u021d\3\2\2\2\u0220\u021e\3\2\2\2\u0220\u021f\3\2\2\2")
        buf.write("\u0221\33\3\2\2\2\u0222\u0226\7V\2\2\u0223\u0225\5\u0108")
        buf.write("\u0085\2\u0224\u0223\3\2\2\2\u0225\u0228\3\2\2\2\u0226")
        buf.write("\u0224\3\2\2\2\u0226\u0227\3\2\2\2\u0227\u0229\3\2\2\2")
        buf.write("\u0228\u0226\3\2\2\2\u0229\u022b\5\6\4\2\u022a\u022c\5")
        buf.write("\62\32\2\u022b\u022a\3\2\2\2\u022b\u022c\3\2\2\2\u022c")
        buf.write("\u022e\3\2\2\2\u022d\u022f\5\34\17\2\u022e\u022d\3\2\2")
        buf.write("\2\u022e\u022f\3\2\2\2\u022f\35\3\2\2\2\u0230\u0231\5")
        buf.write("> \2\u0231\u0232\7V\2\2\u0232\u0234\3\2\2\2\u0233\u0230")
        buf.write("\3\2\2\2\u0233\u0234\3\2\2\2\u0234\u0238\3\2\2\2\u0235")
        buf.write("\u0237\5\u0108\u0085\2\u0236\u0235\3\2\2\2\u0237\u023a")
        buf.write("\3\2\2\2\u0238\u0236\3\2\2\2\u0238\u0239\3\2\2\2\u0239")
        buf.write("\u023b\3\2\2\2\u023a\u0238\3\2\2\2\u023b\u023d\5\6\4\2")
        buf.write("\u023c\u023e\5\62\32\2\u023d\u023c\3\2\2\2\u023d\u023e")
        buf.write("\3\2\2\2\u023e\u0240\3\2\2\2\u023f\u0241\5\34\17\2\u0240")
        buf.write("\u023f\3\2\2\2\u0240\u0241\3\2\2\2\u0241\37\3\2\2\2\u0242")
        buf.write("\u0244\5\u0108\u0085\2\u0243\u0242\3\2\2\2\u0244\u0247")
        buf.write("\3\2\2\2\u0245\u0243\3\2\2\2\u0245\u0246\3\2\2\2\u0246")
        buf.write("\u0248\3\2\2\2\u0247\u0245\3\2\2\2\u0248\u024a\5\6\4\2")
        buf.write("\u0249\u024b\5\62\32\2\u024a\u0249\3\2\2\2\u024a\u024b")
        buf.write("\3\2\2\2\u024b\u0265\3\2\2\2\u024c\u024d\5> \2\u024d\u0251")
        buf.write("\7V\2\2\u024e\u0250\5\u0108\u0085\2\u024f\u024e\3\2\2")
        buf.write("\2\u0250\u0253\3\2\2\2\u0251\u024f\3\2\2\2\u0251\u0252")
        buf.write("\3\2\2\2\u0252\u0254\3\2\2\2\u0253\u0251\3\2\2\2\u0254")
        buf.write("\u0256\5\6\4\2\u0255\u0257\5\62\32\2\u0256\u0255\3\2\2")
        buf.write("\2\u0256\u0257\3\2\2\2\u0257\u0265\3\2\2\2\u0258\u0259")
        buf.write("\5\36\20\2\u0259\u025d\7V\2\2\u025a\u025c\5\u0108\u0085")
        buf.write("\2\u025b\u025a\3\2\2\2\u025c\u025f\3\2\2\2\u025d\u025b")
        buf.write("\3\2\2\2\u025d\u025e\3\2\2\2\u025e\u0260\3\2\2\2\u025f")
        buf.write("\u025d\3\2\2\2\u0260\u0262\5\6\4\2\u0261\u0263\5\62\32")
        buf.write("\2\u0262\u0261\3\2\2\2\u0262\u0263\3\2\2\2\u0263\u0265")
        buf.write("\3\2\2\2\u0264\u0245\3\2\2\2\u0264\u024c\3\2\2\2\u0264")
        buf.write("\u0258\3\2\2\2\u0265!\3\2\2\2\u0266\u0267\5 \21\2\u0267")
        buf.write("#\3\2\2\2\u0268\u026a\5\u0108\u0085\2\u0269\u0268\3\2")
        buf.write("\2\2\u026a\u026d\3\2\2\2\u026b\u0269\3\2\2\2\u026b\u026c")
        buf.write("\3\2\2\2\u026c\u026e\3\2\2\2\u026d\u026b\3\2\2\2\u026e")
        buf.write("\u026f\5\6\4\2\u026f%\3\2\2\2\u0270\u0271\5\22\n\2\u0271")
        buf.write("\u0272\5(\25\2\u0272\u027a\3\2\2\2\u0273\u0274\5 \21\2")
        buf.write("\u0274\u0275\5(\25\2\u0275\u027a\3\2\2\2\u0276\u0277\5")
        buf.write("$\23\2\u0277\u0278\5(\25\2\u0278\u027a\3\2\2\2\u0279\u0270")
        buf.write("\3\2\2\2\u0279\u0273\3\2\2\2\u0279\u0276\3\2\2\2\u027a")
        buf.write("\'\3\2\2\2\u027b\u027d\5\u0108\u0085\2\u027c\u027b\3\2")
        buf.write("\2\2\u027d\u0280\3\2\2\2\u027e\u027c\3\2\2\2\u027e\u027f")
        buf.write("\3\2\2\2\u027f\u0281\3\2\2\2\u0280\u027e\3\2\2\2\u0281")
        buf.write("\u0282\7R\2\2\u0282\u028d\7S\2\2\u0283\u0285\5\u0108\u0085")
        buf.write("\2\u0284\u0283\3\2\2\2\u0285\u0288\3\2\2\2\u0286\u0284")
        buf.write("\3\2\2\2\u0286\u0287\3\2\2\2\u0287\u0289\3\2\2\2\u0288")
        buf.write("\u0286\3\2\2\2\u0289\u028a\7R\2\2\u028a\u028c\7S\2\2\u028b")
        buf.write("\u0286\3\2\2\2\u028c\u028f\3\2\2\2\u028d\u028b\3\2\2\2")
        buf.write("\u028d\u028e\3\2\2\2\u028e)\3\2\2\2\u028f\u028d\3\2\2")
        buf.write("\2\u0290\u0292\5,\27\2\u0291\u0290\3\2\2\2\u0292\u0295")
        buf.write("\3\2\2\2\u0293\u0291\3\2\2\2\u0293\u0294\3\2\2\2\u0294")
        buf.write("\u0296\3\2\2\2\u0295\u0293\3\2\2\2\u0296\u0298\5\6\4\2")
        buf.write("\u0297\u0299\5.\30\2\u0298\u0297\3\2\2\2\u0298\u0299\3")
        buf.write("\2\2\2\u0299+\3\2\2\2\u029a\u029b\5\u0108\u0085\2\u029b")
        buf.write("-\3\2\2\2\u029c\u02a5\7$\2\2\u029d\u02a6\5$\23\2\u029e")
        buf.write("\u02a2\5\36\20\2\u029f\u02a1\5\60\31\2\u02a0\u029f\3\2")
        buf.write("\2\2\u02a1\u02a4\3\2\2\2\u02a2\u02a0\3\2\2\2\u02a2\u02a3")
        buf.write("\3\2\2\2\u02a3\u02a6\3\2\2\2\u02a4\u02a2\3\2\2\2\u02a5")
        buf.write("\u029d\3\2\2\2\u02a5\u029e\3\2\2\2\u02a6/\3\2\2\2\u02a7")
        buf.write("\u02a8\7n\2\2\u02a8\u02a9\5\"\22\2\u02a9\61\3\2\2\2\u02aa")
        buf.write("\u02ab\7\\\2\2\u02ab\u02ac\5\64\33\2\u02ac\u02ad\7[\2")
        buf.write("\2\u02ad\63\3\2\2\2\u02ae\u02b3\5\66\34\2\u02af\u02b0")
        buf.write("\7U\2\2\u02b0\u02b2\5\66\34\2\u02b1\u02af\3\2\2\2\u02b2")
        buf.write("\u02b5\3\2\2\2\u02b3\u02b1\3\2\2\2\u02b3\u02b4\3\2\2\2")
        buf.write("\u02b4\65\3\2\2\2\u02b5\u02b3\3\2\2\2\u02b6\u02b9\5\32")
        buf.write("\16\2\u02b7\u02b9\58\35\2\u02b8\u02b6\3\2\2\2\u02b8\u02b7")
        buf.write("\3\2\2\2\u02b9\67\3\2\2\2\u02ba\u02bc\5\u0108\u0085\2")
        buf.write("\u02bb\u02ba\3\2\2\2\u02bc\u02bf\3\2\2\2\u02bd\u02bb\3")
        buf.write("\2\2\2\u02bd\u02be\3\2\2\2\u02be\u02c0\3\2\2\2\u02bf\u02bd")
        buf.write("\3\2\2\2\u02c0\u02c2\7_\2\2\u02c1\u02c3\5:\36\2\u02c2")
        buf.write("\u02c1\3\2\2\2\u02c2\u02c3\3\2\2\2\u02c39\3\2\2\2\u02c4")
        buf.write("\u02c5\7$\2\2\u02c5\u02c9\5\32\16\2\u02c6\u02c7\7;\2\2")
        buf.write("\u02c7\u02c9\5\32\16\2\u02c8\u02c4\3\2\2\2\u02c8\u02c6")
        buf.write("\3\2\2\2\u02c9;\3\2\2\2\u02ca\u02cd\5\4\3\2\u02cb\u02cc")
        buf.write("\7V\2\2\u02cc\u02ce\5<\37\2\u02cd\u02cb\3\2\2\2\u02cd")
        buf.write("\u02ce\3\2\2\2\u02ce=\3\2\2\2\u02cf\u02d2\5\4\3\2\u02d0")
        buf.write("\u02d1\7V\2\2\u02d1\u02d3\5> \2\u02d2\u02d0\3\2\2\2\u02d2")
        buf.write("\u02d3\3\2\2\2\u02d3?\3\2\2\2\u02d4\u02d7\5> \2\u02d5")
        buf.write("\u02d6\7V\2\2\u02d6\u02d8\5\6\4\2\u02d7\u02d5\3\2\2\2")
        buf.write("\u02d7\u02d8\3\2\2\2\u02d8A\3\2\2\2\u02d9\u02dc\5\4\3")
        buf.write("\2\u02da\u02db\7V\2\2\u02db\u02dd\5B\"\2\u02dc\u02da\3")
        buf.write("\2\2\2\u02dc\u02dd\3\2\2\2\u02ddC\3\2\2\2\u02de\u02df")
        buf.write("\5H%\2\u02df\u02e0\7V\2\2\u02e0\u02e2\3\2\2\2\u02e1\u02de")
        buf.write("\3\2\2\2\u02e1\u02e2\3\2\2\2\u02e2\u02e3\3\2\2\2\u02e3")
        buf.write("\u02e4\5\4\3\2\u02e4E\3\2\2\2\u02e5\u02e6\5\b\5\2\u02e6")
        buf.write("G\3\2\2\2\u02e7\u02ea\5\4\3\2\u02e8\u02e9\7V\2\2\u02e9")
        buf.write("\u02eb\5H%\2\u02ea\u02e8\3\2\2\2\u02ea\u02eb\3\2\2\2\u02eb")
        buf.write("I\3\2\2\2\u02ec\u02ef\5L\'\2\u02ed\u02ef\5N(\2\u02ee\u02ec")
        buf.write("\3\2\2\2\u02ee\u02ed\3\2\2\2\u02efK\3\2\2\2\u02f0\u02f2")
        buf.write("\5P)\2\u02f1\u02f0\3\2\2\2\u02f1\u02f2\3\2\2\2\u02f2\u02f6")
        buf.write("\3\2\2\2\u02f3\u02f5\5T+\2\u02f4\u02f3\3\2\2\2\u02f5\u02f8")
        buf.write("\3\2\2\2\u02f6\u02f4\3\2\2\2\u02f6\u02f7\3\2\2\2\u02f7")
        buf.write("\u02fc\3\2\2\2\u02f8\u02f6\3\2\2\2\u02f9\u02fb\5^\60\2")
        buf.write("\u02fa\u02f9\3\2\2\2\u02fb\u02fe\3\2\2\2\u02fc\u02fa\3")
        buf.write("\2\2\2\u02fc\u02fd\3\2\2\2\u02fdM\3\2\2\2\u02fe\u02fc")
        buf.write("\3\2\2\2\u02ff\u0301\5T+\2\u0300\u02ff\3\2\2\2\u0301\u0304")
        buf.write("\3\2\2\2\u0302\u0300\3\2\2\2\u0302\u0303\3\2\2\2\u0303")
        buf.write("\u0305\3\2\2\2\u0304\u0302\3\2\2\2\u0305\u0306\5`\61\2")
        buf.write("\u0306O\3\2\2\2\u0307\u0309\5R*\2\u0308\u0307\3\2\2\2")
        buf.write("\u0309\u030c\3\2\2\2\u030a\u0308\3\2\2\2\u030a\u030b\3")
        buf.write("\2\2\2\u030b\u030d\3\2\2\2\u030c\u030a\3\2\2\2\u030d\u030e")
        buf.write("\7\63\2\2\u030e\u0313\5\4\3\2\u030f\u0310\7V\2\2\u0310")
        buf.write("\u0312\5\4\3\2\u0311\u030f\3\2\2\2\u0312\u0315\3\2\2\2")
        buf.write("\u0313\u0311\3\2\2\2\u0313\u0314\3\2\2\2\u0314\u0316\3")
        buf.write("\2\2\2\u0315\u0313\3\2\2\2\u0316\u0317\7T\2\2\u0317Q\3")
        buf.write("\2\2\2\u0318\u0319\5\u0108\u0085\2\u0319S\3\2\2\2\u031a")
        buf.write("\u031f\5V,\2\u031b\u031f\5X-\2\u031c\u031f\5Z.\2\u031d")
        buf.write("\u031f\5\\/\2\u031e\u031a\3\2\2\2\u031e\u031b\3\2\2\2")
        buf.write("\u031e\u031c\3\2\2\2\u031e\u031d\3\2\2\2\u031fU\3\2\2")
        buf.write("\2\u0320\u0321\7,\2\2\u0321\u0322\5@!\2\u0322\u0323\7")
        buf.write("T\2\2\u0323W\3\2\2\2\u0324\u0325\7,\2\2\u0325\u0326\5")
        buf.write("B\"\2\u0326\u0327\7V\2\2\u0327\u0328\7l\2\2\u0328\u0329")
        buf.write("\7T\2\2\u0329Y\3\2\2\2\u032a\u032b\7,\2\2\u032b\u032c")
        buf.write("\79\2\2\u032c\u032d\5@!\2\u032d\u032e\7V\2\2\u032e\u032f")
        buf.write("\5\4\3\2\u032f\u0330\7T\2\2\u0330[\3\2\2\2\u0331\u0332")
        buf.write("\7,\2\2\u0332\u0333\79\2\2\u0333\u0334\5@!\2\u0334\u0335")
        buf.write("\7V\2\2\u0335\u0336\7l\2\2\u0336\u0337\7T\2\2\u0337]\3")
        buf.write("\2\2\2\u0338\u033c\5f\64\2\u0339\u033c\5\u00e6t\2\u033a")
        buf.write("\u033c\7T\2\2\u033b\u0338\3\2\2\2\u033b\u0339\3\2\2\2")
        buf.write("\u033b\u033a\3\2\2\2\u033c_\3\2\2\2\u033d\u033f\5\u0108")
        buf.write("\u0085\2\u033e\u033d\3\2\2\2\u033f\u0342\3\2\2\2\u0340")
        buf.write("\u033e\3\2\2\2\u0340\u0341\3\2\2\2\u0341\u0344\3\2\2\2")
        buf.write("\u0342\u0340\3\2\2\2\u0343\u0345\7\7\2\2\u0344\u0343\3")
        buf.write("\2\2\2\u0344\u0345\3\2\2\2\u0345\u0346\3\2\2\2\u0346\u0347")
        buf.write("\7\4\2\2\u0347\u034c\5\4\3\2\u0348\u0349\7V\2\2\u0349")
        buf.write("\u034b\5\4\3\2\u034a\u0348\3\2\2\2\u034b\u034e\3\2\2\2")
        buf.write("\u034c\u034a\3\2\2\2\u034c\u034d\3\2\2\2\u034d\u034f\3")
        buf.write("\2\2\2\u034e\u034c\3\2\2\2\u034f\u0353\7P\2\2\u0350\u0352")
        buf.write("\5b\62\2\u0351\u0350\3\2\2\2\u0352\u0355\3\2\2\2\u0353")
        buf.write("\u0351\3\2\2\2\u0353\u0354\3\2\2\2\u0354\u0356\3\2\2\2")
        buf.write("\u0355\u0353\3\2\2\2\u0356\u0357\7Q\2\2\u0357a\3\2\2\2")
        buf.write("\u0358\u035c\7\f\2\2\u0359\u035b\5d\63\2\u035a\u0359\3")
        buf.write("\2\2\2\u035b\u035e\3\2\2\2\u035c\u035a\3\2\2\2\u035c\u035d")
        buf.write("\3\2\2\2\u035d\u035f\3\2\2\2\u035e\u035c\3\2\2\2\u035f")
        buf.write("\u0360\5<\37\2\u0360\u0361\7T\2\2\u0361\u0392\3\2\2\2")
        buf.write("\u0362\u0363\7\3\2\2\u0363\u036d\5> \2\u0364\u0365\7\16")
        buf.write("\2\2\u0365\u036a\5<\37\2\u0366\u0367\7U\2\2\u0367\u0369")
        buf.write("\5<\37\2\u0368\u0366\3\2\2\2\u0369\u036c\3\2\2\2\u036a")
        buf.write("\u0368\3\2\2\2\u036a\u036b\3\2\2\2\u036b\u036e\3\2\2\2")
        buf.write("\u036c\u036a\3\2\2\2\u036d\u0364\3\2\2\2\u036d\u036e\3")
        buf.write("\2\2\2\u036e\u036f\3\2\2\2\u036f\u0370\7T\2\2\u0370\u0392")
        buf.write("\3\2\2\2\u0371\u0372\7\b\2\2\u0372\u037c\5> \2\u0373\u0374")
        buf.write("\7\16\2\2\u0374\u0379\5<\37\2\u0375\u0376\7U\2\2\u0376")
        buf.write("\u0378\5<\37\2\u0377\u0375\3\2\2\2\u0378\u037b\3\2\2\2")
        buf.write("\u0379\u0377\3\2\2\2\u0379\u037a\3\2\2\2\u037a\u037d\3")
        buf.write("\2\2\2\u037b\u0379\3\2\2\2\u037c\u0373\3\2\2\2\u037c\u037d")
        buf.write("\3\2\2\2\u037d\u037e\3\2\2\2\u037e\u037f\7T\2\2\u037f")
        buf.write("\u0392\3\2\2\2\u0380\u0381\7\20\2\2\u0381\u0382\5@!\2")
        buf.write("\u0382\u0383\7T\2\2\u0383\u0392\3\2\2\2\u0384\u0385\7")
        buf.write("\n\2\2\u0385\u0386\5@!\2\u0386\u0387\7\22\2\2\u0387\u038c")
        buf.write("\5@!\2\u0388\u0389\7U\2\2\u0389\u038b\5@!\2\u038a\u0388")
        buf.write("\3\2\2\2\u038b\u038e\3\2\2\2\u038c\u038a\3\2\2\2\u038c")
        buf.write("\u038d\3\2\2\2\u038d\u038f\3\2\2\2\u038e\u038c\3\2\2\2")
        buf.write("\u038f\u0390\7T\2\2\u0390\u0392\3\2\2\2\u0391\u0358\3")
        buf.write("\2\2\2\u0391\u0362\3\2\2\2\u0391\u0371\3\2\2\2\u0391\u0380")
        buf.write("\3\2\2\2\u0391\u0384\3\2\2\2\u0392c\3\2\2\2\u0393\u0394")
        buf.write("\t\b\2\2\u0394e\3\2\2\2\u0395\u0399\5h\65\2\u0396\u0399")
        buf.write("\5\u00c8e\2\u0397\u0399\5\u00d4k\2\u0398\u0395\3\2\2\2")
        buf.write("\u0398\u0396\3\2\2\2\u0398\u0397\3\2\2\2\u0399g\3\2\2")
        buf.write("\2\u039a\u039c\5j\66\2\u039b\u039a\3\2\2\2\u039c\u039f")
        buf.write("\3\2\2\2\u039d\u039b\3\2\2\2\u039d\u039e\3\2\2\2\u039e")
        buf.write("\u03a0\3\2\2\2\u039f\u039d\3\2\2\2\u03a0\u03a1\7\34\2")
        buf.write("\2\u03a1\u03a3\5\6\4\2\u03a2\u03a4\5l\67\2\u03a3\u03a2")
        buf.write("\3\2\2\2\u03a3\u03a4\3\2\2\2\u03a4\u03a6\3\2\2\2\u03a5")
        buf.write("\u03a7\5p9\2\u03a6\u03a5\3\2\2\2\u03a6\u03a7\3\2\2\2\u03a7")
        buf.write("\u03a9\3\2\2\2\u03a8\u03aa\5r:\2\u03a9\u03a8\3\2\2\2\u03a9")
        buf.write("\u03aa\3\2\2\2\u03aa\u03ac\3\2\2\2\u03ab\u03ad\5v<\2\u03ac")
        buf.write("\u03ab\3\2\2\2\u03ac\u03ad\3\2\2\2\u03ad\u03ae\3\2\2\2")
        buf.write("\u03ae\u03af\5x=\2\u03afi\3\2\2\2\u03b0\u03bb\5\u0108")
        buf.write("\u0085\2\u03b1\u03bb\7\66\2\2\u03b2\u03bb\7\65\2\2\u03b3")
        buf.write("\u03bb\7\64\2\2\u03b4\u03bb\7\24\2\2\u03b5\u03bb\79\2")
        buf.write("\2\u03b6\u03bb\7%\2\2\u03b7\u03bb\7\r\2\2\u03b8\u03bb")
        buf.write("\7\5\2\2\u03b9\u03bb\7:\2\2\u03ba\u03b0\3\2\2\2\u03ba")
        buf.write("\u03b1\3\2\2\2\u03ba\u03b2\3\2\2\2\u03ba\u03b3\3\2\2\2")
        buf.write("\u03ba\u03b4\3\2\2\2\u03ba\u03b5\3\2\2\2\u03ba\u03b6\3")
        buf.write("\2\2\2\u03ba\u03b7\3\2\2\2\u03ba\u03b8\3\2\2\2\u03ba\u03b9")
        buf.write("\3\2\2\2\u03bbk\3\2\2\2\u03bc\u03bd\7\\\2\2\u03bd\u03be")
        buf.write("\5n8\2\u03be\u03bf\7[\2\2\u03bfm\3\2\2\2\u03c0\u03c5\5")
        buf.write("*\26\2\u03c1\u03c2\7U\2\2\u03c2\u03c4\5*\26\2\u03c3\u03c1")
        buf.write("\3\2\2\2\u03c4\u03c7\3\2\2\2\u03c5\u03c3\3\2\2\2\u03c5")
        buf.write("\u03c6\3\2\2\2\u03c6o\3\2\2\2\u03c7\u03c5\3\2\2\2\u03c8")
        buf.write("\u03c9\7$\2\2\u03c9\u03ca\5 \21\2\u03caq\3\2\2\2\u03cb")
        buf.write("\u03cc\7+\2\2\u03cc\u03cd\5t;\2\u03cds\3\2\2\2\u03ce\u03d3")
        buf.write("\5\"\22\2\u03cf\u03d0\7U\2\2\u03d0\u03d2\5\"\22\2\u03d1")
        buf.write("\u03cf\3\2\2\2\u03d2\u03d5\3\2\2\2\u03d3\u03d1\3\2\2\2")
        buf.write("\u03d3\u03d4\3\2\2\2\u03d4u\3\2\2\2\u03d5\u03d3\3\2\2")
        buf.write("\2\u03d6\u03d7\7\t\2\2\u03d7\u03dc\5@!\2\u03d8\u03d9\7")
        buf.write("U\2\2\u03d9\u03db\5@!\2\u03da\u03d8\3\2\2\2\u03db\u03de")
        buf.write("\3\2\2\2\u03dc\u03da\3\2\2\2\u03dc\u03dd\3\2\2\2\u03dd")
        buf.write("w\3\2\2\2\u03de\u03dc\3\2\2\2\u03df\u03e3\7P\2\2\u03e0")
        buf.write("\u03e2\5z>\2\u03e1\u03e0\3\2\2\2\u03e2\u03e5\3\2\2\2\u03e3")
        buf.write("\u03e1\3\2\2\2\u03e3\u03e4\3\2\2\2\u03e4\u03e6\3\2\2\2")
        buf.write("\u03e5\u03e3\3\2\2\2\u03e6\u03e7\7Q\2\2\u03e7y\3\2\2\2")
        buf.write("\u03e8\u03ed\5|?\2\u03e9\u03ed\5\u00b8]\2\u03ea\u03ed")
        buf.write("\5\u00ba^\2\u03eb\u03ed\5\u00bc_\2\u03ec\u03e8\3\2\2\2")
        buf.write("\u03ec\u03e9\3\2\2\2\u03ec\u03ea\3\2\2\2\u03ec\u03eb\3")
        buf.write("\2\2\2\u03ed{\3\2\2\2\u03ee\u03f4\5~@\2\u03ef\u03f4\5")
        buf.write("\u009cO\2\u03f0\u03f4\5f\64\2\u03f1\u03f4\5\u00e6t\2\u03f2")
        buf.write("\u03f4\7T\2\2\u03f3\u03ee\3\2\2\2\u03f3\u03ef\3\2\2\2")
        buf.write("\u03f3\u03f0\3\2\2\2\u03f3\u03f1\3\2\2\2\u03f3\u03f2\3")
        buf.write("\2\2\2\u03f4}\3\2\2\2\u03f5\u03f7\5\u0080A\2\u03f6\u03f5")
        buf.write("\3\2\2\2\u03f7\u03fa\3\2\2\2\u03f8\u03f6\3\2\2\2\u03f8")
        buf.write("\u03f9\3\2\2\2\u03f9\u03fb\3\2\2\2\u03fa\u03f8\3\2\2\2")
        buf.write("\u03fb\u03fc\5\u008aF\2\u03fc\u03fd\5\u0082B\2\u03fd\u03fe")
        buf.write("\7T\2\2\u03fe\177\3\2\2\2\u03ff\u0408\5\u0108\u0085\2")
        buf.write("\u0400\u0408\7\66\2\2\u0401\u0408\7\65\2\2\u0402\u0408")
        buf.write("\7\64\2\2\u0403\u0408\79\2\2\u0404\u0408\7%\2\2\u0405")
        buf.write("\u0408\7A\2\2\u0406\u0408\7D\2\2\u0407\u03ff\3\2\2\2\u0407")
        buf.write("\u0400\3\2\2\2\u0407\u0401\3\2\2\2\u0407\u0402\3\2\2\2")
        buf.write("\u0407\u0403\3\2\2\2\u0407\u0404\3\2\2\2\u0407\u0405\3")
        buf.write("\2\2\2\u0407\u0406\3\2\2\2\u0408\u0081\3\2\2\2\u0409\u040e")
        buf.write("\5\u0084C\2\u040a\u040b\7U\2\2\u040b\u040d\5\u0084C\2")
        buf.write("\u040c\u040a\3\2\2\2\u040d\u0410\3\2\2\2\u040e\u040c\3")
        buf.write("\2\2\2\u040e\u040f\3\2\2\2\u040f\u0083\3\2\2\2\u0410\u040e")
        buf.write("\3\2\2\2\u0411\u0414\5\u0086D\2\u0412\u0413\7Z\2\2\u0413")
        buf.write("\u0415\5\u0088E\2\u0414\u0412\3\2\2\2\u0414\u0415\3\2")
        buf.write("\2\2\u0415\u0085\3\2\2\2\u0416\u0418\5\4\3\2\u0417\u0419")
        buf.write("\5(\25\2\u0418\u0417\3\2\2\2\u0418\u0419\3\2\2\2\u0419")
        buf.write("\u0087\3\2\2\2\u041a\u041d\5\u018e\u00c8\2\u041b\u041d")
        buf.write("\5\u011a\u008e\2\u041c\u041a\3\2\2\2\u041c\u041b\3\2\2")
        buf.write("\2\u041d\u0089\3\2\2\2\u041e\u0421\5\u008cG\2\u041f\u0421")
        buf.write("\5\u008eH\2\u0420\u041e\3\2\2\2\u0420\u041f\3\2\2\2\u0421")
        buf.write("\u008b\3\2\2\2\u0422\u0425\5\24\13\2\u0423\u0425\7\26")
        buf.write("\2\2\u0424\u0422\3\2\2\2\u0424\u0423\3\2\2\2\u0425\u008d")
        buf.write("\3\2\2\2\u0426\u042a\5\u0090I\2\u0427\u042a\5\u0098M\2")
        buf.write("\u0428\u042a\5\u009aN\2\u0429\u0426\3\2\2\2\u0429\u0427")
        buf.write("\3\2\2\2\u0429\u0428\3\2\2\2\u042a\u008f\3\2\2\2\u042b")
        buf.write("\u042c\5> \2\u042c\u0430\7V\2\2\u042d\u042f\5\u0108\u0085")
        buf.write("\2\u042e\u042d\3\2\2\2\u042f\u0432\3\2\2\2\u0430\u042e")
        buf.write("\3\2\2\2\u0430\u0431\3\2\2\2\u0431\u0434\3\2\2\2\u0432")
        buf.write("\u0430\3\2\2\2\u0433\u042b\3\2\2\2\u0433\u0434\3\2\2\2")
        buf.write("\u0434\u0435\3\2\2\2\u0435\u0437\5\6\4\2\u0436\u0438\5")
        buf.write("\62\32\2\u0437\u0436\3\2\2\2\u0437\u0438\3\2\2\2\u0438")
        buf.write("\u043a\3\2\2\2\u0439\u043b\5\u0092J\2\u043a\u0439\3\2")
        buf.write("\2\2\u043a\u043b\3\2\2\2\u043b\u0091\3\2\2\2\u043c\u0440")
        buf.write("\7V\2\2\u043d\u043f\5\u0108\u0085\2\u043e\u043d\3\2\2")
        buf.write("\2\u043f\u0442\3\2\2\2\u0440\u043e\3\2\2\2\u0440\u0441")
        buf.write("\3\2\2\2\u0441\u0443\3\2\2\2\u0442\u0440\3\2\2\2\u0443")
        buf.write("\u0445\5\6\4\2\u0444\u0446\5\62\32\2\u0445\u0444\3\2\2")
        buf.write("\2\u0445\u0446\3\2\2\2\u0446\u0448\3\2\2\2\u0447\u0449")
        buf.write("\5\u0092J\2\u0448\u0447\3\2\2\2\u0448\u0449\3\2\2\2\u0449")
        buf.write("\u0093\3\2\2\2\u044a\u044c\5\6\4\2\u044b\u044d\5\62\32")
        buf.write("\2\u044c\u044b\3\2\2\2\u044c\u044d\3\2\2\2\u044d\u045e")
        buf.write("\3\2\2\2\u044e\u0451\5> \2\u044f\u0451\5\u0090I\2\u0450")
        buf.write("\u044e\3\2\2\2\u0450\u044f\3\2\2\2\u0451\u0452\3\2\2\2")
        buf.write("\u0452\u0456\7V\2\2\u0453\u0455\5\u0108\u0085\2\u0454")
        buf.write("\u0453\3\2\2\2\u0455\u0458\3\2\2\2\u0456\u0454\3\2\2\2")
        buf.write("\u0456\u0457\3\2\2\2\u0457\u0459\3\2\2\2\u0458\u0456\3")
        buf.write("\2\2\2\u0459\u045b\5\6\4\2\u045a\u045c\5\62\32\2\u045b")
        buf.write("\u045a\3\2\2\2\u045b\u045c\3\2\2\2\u045c\u045e\3\2\2\2")
        buf.write("\u045d\u044a\3\2\2\2\u045d\u0450\3\2\2\2\u045e\u0095\3")
        buf.write("\2\2\2\u045f\u0460\5\u0094K\2\u0460\u0097\3\2\2\2\u0461")
        buf.write("\u0462\5\6\4\2\u0462\u0099\3\2\2\2\u0463\u0467\5\u008c")
        buf.write("G\2\u0464\u0467\5\u0090I\2\u0465\u0467\5\u0098M\2\u0466")
        buf.write("\u0463\3\2\2\2\u0466\u0464\3\2\2\2\u0466\u0465\3\2\2\2")
        buf.write("\u0467\u0468\3\2\2\2\u0468\u0469\5(\25\2\u0469\u009b\3")
        buf.write("\2\2\2\u046a\u046c\5\u009eP\2\u046b\u046a\3\2\2\2\u046c")
        buf.write("\u046f\3\2\2\2\u046d\u046b\3\2\2\2\u046d\u046e\3\2\2\2")
        buf.write("\u046e\u0470\3\2\2\2\u046f\u046d\3\2\2\2\u0470\u0471\5")
        buf.write("\u00a0Q\2\u0471\u0472\5\u00b6\\\2\u0472\u009d\3\2\2\2")
        buf.write("\u0473\u047e\5\u0108\u0085\2\u0474\u047e\7\66\2\2\u0475")
        buf.write("\u047e\7\65\2\2\u0476\u047e\7\64\2\2\u0477\u047e\7\24")
        buf.write("\2\2\u0478\u047e\79\2\2\u0479\u047e\7%\2\2\u047a\u047e")
        buf.write("\7=\2\2\u047b\u047e\7\61\2\2\u047c\u047e\7:\2\2\u047d")
        buf.write("\u0473\3\2\2\2\u047d\u0474\3\2\2\2\u047d\u0475\3\2\2\2")
        buf.write("\u047d\u0476\3\2\2\2\u047d\u0477\3\2\2\2\u047d\u0478\3")
        buf.write("\2\2\2\u047d\u0479\3\2\2\2\u047d\u047a\3\2\2\2\u047d\u047b")
        buf.write("\3\2\2\2\u047d\u047c\3\2\2\2\u047e\u009f\3\2\2\2\u047f")
        buf.write("\u0483\5l\67\2\u0480\u0482\5\u0108\u0085\2\u0481\u0480")
        buf.write("\3\2\2\2\u0482\u0485\3\2\2\2\u0483\u0481\3\2\2\2\u0483")
        buf.write("\u0484\3\2\2\2\u0484\u0487\3\2\2\2\u0485\u0483\3\2\2\2")
        buf.write("\u0486\u047f\3\2\2\2\u0486\u0487\3\2\2\2\u0487\u0488\3")
        buf.write("\2\2\2\u0488\u0489\5\u00a2R\2\u0489\u048b\5\u00a4S\2\u048a")
        buf.write("\u048c\5\u00b0Y\2\u048b\u048a\3\2\2\2\u048b\u048c\3\2")
        buf.write("\2\2\u048c\u00a1\3\2\2\2\u048d\u0490\5\u008aF\2\u048e")
        buf.write("\u0490\7C\2\2\u048f\u048d\3\2\2\2\u048f\u048e\3\2\2\2")
        buf.write("\u0490\u00a3\3\2\2\2\u0491\u0492\5\4\3\2\u0492\u0496\7")
        buf.write("N\2\2\u0493\u0494\5\u00a6T\2\u0494\u0495\7U\2\2\u0495")
        buf.write("\u0497\3\2\2\2\u0496\u0493\3\2\2\2\u0496\u0497\3\2\2\2")
        buf.write("\u0497\u0499\3\2\2\2\u0498\u049a\5\u00a8U\2\u0499\u0498")
        buf.write("\3\2\2\2\u0499\u049a\3\2\2\2\u049a\u049b\3\2\2\2\u049b")
        buf.write("\u049d\7O\2\2\u049c\u049e\5(\25\2\u049d\u049c\3\2\2\2")
        buf.write("\u049d\u049e\3\2\2\2\u049e\u00a5\3\2\2\2\u049f\u04a1\5")
        buf.write("\u0108\u0085\2\u04a0\u049f\3\2\2\2\u04a1\u04a4\3\2\2\2")
        buf.write("\u04a2\u04a0\3\2\2\2\u04a2\u04a3\3\2\2\2\u04a3\u04a5\3")
        buf.write("\2\2\2\u04a4\u04a2\3\2\2\2\u04a5\u04a9\5\u008aF\2\u04a6")
        buf.write("\u04a7\5\4\3\2\u04a7\u04a8\7V\2\2\u04a8\u04aa\3\2\2\2")
        buf.write("\u04a9\u04a6\3\2\2\2\u04a9\u04aa\3\2\2\2\u04aa\u04ab\3")
        buf.write("\2\2\2\u04ab\u04ac\7>\2\2\u04ac\u00a7\3\2\2\2\u04ad\u04b2")
        buf.write("\5\u00aaV\2\u04ae\u04af\7U\2\2\u04af\u04b1\5\u00aaV\2")
        buf.write("\u04b0\u04ae\3\2\2\2\u04b1\u04b4\3\2\2\2\u04b2\u04b0\3")
        buf.write("\2\2\2\u04b2\u04b3\3\2\2\2\u04b3\u00a9\3\2\2\2\u04b4\u04b2")
        buf.write("\3\2\2\2\u04b5\u04b7\5\u00aeX\2\u04b6\u04b5\3\2\2\2\u04b7")
        buf.write("\u04ba\3\2\2\2\u04b8\u04b6\3\2\2\2\u04b8\u04b9\3\2\2\2")
        buf.write("\u04b9\u04bb\3\2\2\2\u04ba\u04b8\3\2\2\2\u04bb\u04bc\5")
        buf.write("\u008aF\2\u04bc\u04bd\5\u0086D\2\u04bd\u04c0\3\2\2\2\u04be")
        buf.write("\u04c0\5\u00acW\2\u04bf\u04b8\3\2\2\2\u04bf\u04be\3\2")
        buf.write("\2\2\u04c0\u00ab\3\2\2\2\u04c1\u04c3\5\u00aeX\2\u04c2")
        buf.write("\u04c1\3\2\2\2\u04c3\u04c6\3\2\2\2\u04c4\u04c2\3\2\2\2")
        buf.write("\u04c4\u04c5\3\2\2\2\u04c5\u04c7\3\2\2\2\u04c6\u04c4\3")
        buf.write("\2\2\2\u04c7\u04cb\5\u008aF\2\u04c8\u04ca\5\u0108\u0085")
        buf.write("\2\u04c9\u04c8\3\2\2\2\u04ca\u04cd\3\2\2\2\u04cb\u04c9")
        buf.write("\3\2\2\2\u04cb\u04cc\3\2\2\2\u04cc\u04ce\3\2\2\2\u04cd")
        buf.write("\u04cb\3\2\2\2\u04ce\u04cf\7W\2\2\u04cf\u04d0\5\4\3\2")
        buf.write("\u04d0\u00ad\3\2\2\2\u04d1\u04d4\5\u0108\u0085\2\u04d2")
        buf.write("\u04d4\7%\2\2\u04d3\u04d1\3\2\2\2\u04d3\u04d2\3\2\2\2")
        buf.write("\u04d4\u00af\3\2\2\2\u04d5\u04d6\7@\2\2\u04d6\u04d7\5")
        buf.write("\u00b2Z\2\u04d7\u00b1\3\2\2\2\u04d8\u04dd\5\u00b4[\2\u04d9")
        buf.write("\u04da\7U\2\2\u04da\u04dc\5\u00b4[\2\u04db\u04d9\3\2\2")
        buf.write("\2\u04dc\u04df\3\2\2\2\u04dd\u04db\3\2\2\2\u04dd\u04de")
        buf.write("\3\2\2\2\u04de\u00b3\3\2\2\2\u04df\u04dd\3\2\2\2\u04e0")
        buf.write("\u04e3\5 \21\2\u04e1\u04e3\5$\23\2\u04e2\u04e0\3\2\2\2")
        buf.write("\u04e2\u04e1\3\2\2\2\u04e3\u00b5\3\2\2\2\u04e4\u04e7\5")
        buf.write("\u011e\u0090\2\u04e5\u04e7\7T\2\2\u04e6\u04e4\3\2\2\2")
        buf.write("\u04e6\u04e5\3\2\2\2\u04e7\u00b7\3\2\2\2\u04e8\u04e9\5")
        buf.write("\u011e\u0090\2\u04e9\u00b9\3\2\2\2\u04ea\u04eb\79\2\2")
        buf.write("\u04eb\u04ec\5\u011e\u0090\2\u04ec\u00bb\3\2\2\2\u04ed")
        buf.write("\u04ef\5\u00be`\2\u04ee\u04ed\3\2\2\2\u04ef\u04f2\3\2")
        buf.write("\2\2\u04f0\u04ee\3\2\2\2\u04f0\u04f1\3\2\2\2\u04f1\u04f3")
        buf.write("\3\2\2\2\u04f2\u04f0\3\2\2\2\u04f3\u04f5\5\u00c0a\2\u04f4")
        buf.write("\u04f6\5\u00b0Y\2\u04f5\u04f4\3\2\2\2\u04f5\u04f6\3\2")
        buf.write("\2\2\u04f6\u04f7\3\2\2\2\u04f7\u04f8\5\u00c4c\2\u04f8")
        buf.write("\u00bd\3\2\2\2\u04f9\u04fe\5\u0108\u0085\2\u04fa\u04fe")
        buf.write("\7\66\2\2\u04fb\u04fe\7\65\2\2\u04fc\u04fe\7\64\2\2\u04fd")
        buf.write("\u04f9\3\2\2\2\u04fd\u04fa\3\2\2\2\u04fd\u04fb\3\2\2\2")
        buf.write("\u04fd\u04fc\3\2\2\2\u04fe\u00bf\3\2\2\2\u04ff\u0501\5")
        buf.write("l\67\2\u0500\u04ff\3\2\2\2\u0500\u0501\3\2\2\2\u0501\u0502")
        buf.write("\3\2\2\2\u0502\u0503\5\u00c2b\2\u0503\u0507\7N\2\2\u0504")
        buf.write("\u0505\5\u00a6T\2\u0505\u0506\7U\2\2\u0506\u0508\3\2\2")
        buf.write("\2\u0507\u0504\3\2\2\2\u0507\u0508\3\2\2\2\u0508\u050a")
        buf.write("\3\2\2\2\u0509\u050b\5\u00a8U\2\u050a\u0509\3\2\2\2\u050a")
        buf.write("\u050b\3\2\2\2\u050b\u050c\3\2\2\2\u050c\u050d\7O\2\2")
        buf.write("\u050d\u00c1\3\2\2\2\u050e\u050f\5\6\4\2\u050f\u00c3\3")
        buf.write("\2\2\2\u0510\u0512\7P\2\2\u0511\u0513\5\u00c6d\2\u0512")
        buf.write("\u0511\3\2\2\2\u0512\u0513\3\2\2\2\u0513\u0515\3\2\2\2")
        buf.write("\u0514\u0516\5\u0120\u0091\2\u0515\u0514\3\2\2\2\u0515")
        buf.write("\u0516\3\2\2\2\u0516\u0517\3\2\2\2\u0517\u0518\7Q\2\2")
        buf.write("\u0518\u00c5\3\2\2\2\u0519\u051b\5\62\32\2\u051a\u0519")
        buf.write("\3\2\2\2\u051a\u051b\3\2\2\2\u051b\u051c\3\2\2\2\u051c")
        buf.write("\u051d\t\t\2\2\u051d\u051f\7N\2\2\u051e\u0520\5\u01b0")
        buf.write("\u00d9\2\u051f\u051e\3\2\2\2\u051f\u0520\3\2\2\2\u0520")
        buf.write("\u0521\3\2\2\2\u0521\u0522\7O\2\2\u0522\u0534\7T\2\2\u0523")
        buf.write("\u0526\5D#\2\u0524\u0526\5\u0190\u00c9\2\u0525\u0523\3")
        buf.write("\2\2\2\u0525\u0524\3\2\2\2\u0526\u0527\3\2\2\2\u0527\u0529")
        buf.write("\7V\2\2\u0528\u052a\5\62\32\2\u0529\u0528\3\2\2\2\u0529")
        buf.write("\u052a\3\2\2\2\u052a\u052b\3\2\2\2\u052b\u052c\7;\2\2")
        buf.write("\u052c\u052e\7N\2\2\u052d\u052f\5\u01b0\u00d9\2\u052e")
        buf.write("\u052d\3\2\2\2\u052e\u052f\3\2\2\2\u052f\u0530\3\2\2\2")
        buf.write("\u0530\u0531\7O\2\2\u0531\u0532\7T\2\2\u0532\u0534\3\2")
        buf.write("\2\2\u0533\u051a\3\2\2\2\u0533\u0525\3\2\2\2\u0534\u00c7")
        buf.write("\3\2\2\2\u0535\u0537\5j\66\2\u0536\u0535\3\2\2\2\u0537")
        buf.write("\u053a\3\2\2\2\u0538\u0536\3\2\2\2\u0538\u0539\3\2\2\2")
        buf.write("\u0539\u053b\3\2\2\2\u053a\u0538\3\2\2\2\u053b\u053c\7")
        buf.write("#\2\2\u053c\u053e\5\6\4\2\u053d\u053f\5r:\2\u053e\u053d")
        buf.write("\3\2\2\2\u053e\u053f\3\2\2\2\u053f\u0540\3\2\2\2\u0540")
        buf.write("\u0541\5\u00caf\2\u0541\u00c9\3\2\2\2\u0542\u0544\7P\2")
        buf.write("\2\u0543\u0545\5\u00ccg\2\u0544\u0543\3\2\2\2\u0544\u0545")
        buf.write("\3\2\2\2\u0545\u0547\3\2\2\2\u0546\u0548\7U\2\2\u0547")
        buf.write("\u0546\3\2\2\2\u0547\u0548\3\2\2\2\u0548\u054a\3\2\2\2")
        buf.write("\u0549\u054b\5\u00d2j\2\u054a\u0549\3\2\2\2\u054a\u054b")
        buf.write("\3\2\2\2\u054b\u054c\3\2\2\2\u054c\u054d\7Q\2\2\u054d")
        buf.write("\u00cb\3\2\2\2\u054e\u0553\5\u00ceh\2\u054f\u0550\7U\2")
        buf.write("\2\u0550\u0552\5\u00ceh\2\u0551\u054f\3\2\2\2\u0552\u0555")
        buf.write("\3\2\2\2\u0553\u0551\3\2\2\2\u0553\u0554\3\2\2\2\u0554")
        buf.write("\u00cd\3\2\2\2\u0555\u0553\3\2\2\2\u0556\u0558\5\u00d0")
        buf.write("i\2\u0557\u0556\3\2\2\2\u0558\u055b\3\2\2\2\u0559\u0557")
        buf.write("\3\2\2\2\u0559\u055a\3\2\2\2\u055a\u055c\3\2\2\2\u055b")
        buf.write("\u0559\3\2\2\2\u055c\u0562\5\4\3\2\u055d\u055f\7N\2\2")
        buf.write("\u055e\u0560\5\u01b0\u00d9\2\u055f\u055e\3\2\2\2\u055f")
        buf.write("\u0560\3\2\2\2\u0560\u0561\3\2\2\2\u0561\u0563\7O\2\2")
        buf.write("\u0562\u055d\3\2\2\2\u0562\u0563\3\2\2\2\u0563\u0565\3")
        buf.write("\2\2\2\u0564\u0566\5x=\2\u0565\u0564\3\2\2\2\u0565\u0566")
        buf.write("\3\2\2\2\u0566\u00cf\3\2\2\2\u0567\u0568\5\u0108\u0085")
        buf.write("\2\u0568\u00d1\3\2\2\2\u0569\u056d\7T\2\2\u056a\u056c")
        buf.write("\5z>\2\u056b\u056a\3\2\2\2\u056c\u056f\3\2\2\2\u056d\u056b")
        buf.write("\3\2\2\2\u056d\u056e\3\2\2\2\u056e\u00d3\3\2\2\2\u056f")
        buf.write("\u056d\3\2\2\2\u0570\u0572\5j\66\2\u0571\u0570\3\2\2\2")
        buf.write("\u0572\u0575\3\2\2\2\u0573\u0571\3\2\2\2\u0573\u0574\3")
        buf.write("\2\2\2\u0574\u0576\3\2\2\2\u0575\u0573\3\2\2\2\u0576\u0577")
        buf.write("\7\13\2\2\u0577\u0579\5\6\4\2\u0578\u057a\5l\67\2\u0579")
        buf.write("\u0578\3\2\2\2\u0579\u057a\3\2\2\2\u057a\u057b\3\2\2\2")
        buf.write("\u057b\u057d\5\u00d6l\2\u057c\u057e\5r:\2\u057d\u057c")
        buf.write("\3\2\2\2\u057d\u057e\3\2\2\2\u057e\u057f\3\2\2\2\u057f")
        buf.write("\u0580\5\u00e0q\2\u0580\u00d5\3\2\2\2\u0581\u0583\7N\2")
        buf.write("\2\u0582\u0584\5\u00d8m\2\u0583\u0582\3\2\2\2\u0583\u0584")
        buf.write("\3\2\2\2\u0584\u0585\3\2\2\2\u0585\u0586\7O\2\2\u0586")
        buf.write("\u00d7\3\2\2\2\u0587\u058c\5\u00dan\2\u0588\u0589\7U\2")
        buf.write("\2\u0589\u058b\5\u00dan\2\u058a\u0588\3\2\2\2\u058b\u058e")
        buf.write("\3\2\2\2\u058c\u058a\3\2\2\2\u058c\u058d\3\2\2\2\u058d")
        buf.write("\u00d9\3\2\2\2\u058e\u058c\3\2\2\2\u058f\u0591\5\u00de")
        buf.write("p\2\u0590\u058f\3\2\2\2\u0591\u0594\3\2\2\2\u0592\u0590")
        buf.write("\3\2\2\2\u0592\u0593\3\2\2\2\u0593\u0595\3\2\2\2\u0594")
        buf.write("\u0592\3\2\2\2\u0595\u0596\5\u008aF\2\u0596\u0597\5\4")
        buf.write("\3\2\u0597\u059a\3\2\2\2\u0598\u059a\5\u00dco\2\u0599")
        buf.write("\u0592\3\2\2\2\u0599\u0598\3\2\2\2\u059a\u00db\3\2\2\2")
        buf.write("\u059b\u059d\5\u00dep\2\u059c\u059b\3\2\2\2\u059d\u05a0")
        buf.write("\3\2\2\2\u059e\u059c\3\2\2\2\u059e\u059f\3\2\2\2\u059f")
        buf.write("\u05a1\3\2\2\2\u05a0\u059e\3\2\2\2\u05a1\u05a5\5\u008a")
        buf.write("F\2\u05a2\u05a4\5\u0108\u0085\2\u05a3\u05a2\3\2\2\2\u05a4")
        buf.write("\u05a7\3\2\2\2\u05a5\u05a3\3\2\2\2\u05a5\u05a6\3\2\2\2")
        buf.write("\u05a6\u05a8\3\2\2\2\u05a7\u05a5\3\2\2\2\u05a8\u05a9\7")
        buf.write("W\2\2\u05a9\u05aa\5\4\3\2\u05aa\u00dd\3\2\2\2\u05ab\u05ac")
        buf.write("\5\u0108\u0085\2\u05ac\u00df\3\2\2\2\u05ad\u05b1\7P\2")
        buf.write("\2\u05ae\u05b0\5\u00e2r\2\u05af\u05ae\3\2\2\2\u05b0\u05b3")
        buf.write("\3\2\2\2\u05b1\u05af\3\2\2\2\u05b1\u05b2\3\2\2\2\u05b2")
        buf.write("\u05b4\3\2\2\2\u05b3\u05b1\3\2\2\2\u05b4\u05b5\7Q\2\2")
        buf.write("\u05b5\u00e1\3\2\2\2\u05b6\u05b9\5z>\2\u05b7\u05b9\5\u00e4")
        buf.write("s\2\u05b8\u05b6\3\2\2\2\u05b8\u05b7\3\2\2\2\u05b9\u00e3")
        buf.write("\3\2\2\2\u05ba\u05bc\5\u00be`\2\u05bb\u05ba\3\2\2\2\u05bc")
        buf.write("\u05bf\3\2\2\2\u05bd\u05bb\3\2\2\2\u05bd\u05be\3\2\2\2")
        buf.write("\u05be\u05c0\3\2\2\2\u05bf\u05bd\3\2\2\2\u05c0\u05c1\5")
        buf.write("\u00c2b\2\u05c1\u05c2\5\u00c4c\2\u05c2\u00e5\3\2\2\2\u05c3")
        buf.write("\u05c6\5\u00e8u\2\u05c4\u05c6\5\u00fc\177\2\u05c5\u05c3")
        buf.write("\3\2\2\2\u05c5\u05c4\3\2\2\2\u05c6\u00e7\3\2\2\2\u05c7")
        buf.write("\u05c9\5\u00eav\2\u05c8\u05c7\3\2\2\2\u05c9\u05cc\3\2")
        buf.write("\2\2\u05ca\u05c8\3\2\2\2\u05ca\u05cb\3\2\2\2\u05cb\u05cd")
        buf.write("\3\2\2\2\u05cc\u05ca\3\2\2\2\u05cd\u05ce\7/\2\2\u05ce")
        buf.write("\u05d0\5\6\4\2\u05cf\u05d1\5l\67\2\u05d0\u05cf\3\2\2\2")
        buf.write("\u05d0\u05d1\3\2\2\2\u05d1\u05d3\3\2\2\2\u05d2\u05d4\5")
        buf.write("\u00ecw\2\u05d3\u05d2\3\2\2\2\u05d3\u05d4\3\2\2\2\u05d4")
        buf.write("\u05d6\3\2\2\2\u05d5\u05d7\5\u00eex\2\u05d6\u05d5\3\2")
        buf.write("\2\2\u05d6\u05d7\3\2\2\2\u05d7\u05d8\3\2\2\2\u05d8\u05d9")
        buf.write("\5\u00f0y\2\u05d9\u00e9\3\2\2\2\u05da\u05e4\5\u0108\u0085")
        buf.write("\2\u05db\u05e4\7\66\2\2\u05dc\u05e4\7\65\2\2\u05dd\u05e4")
        buf.write("\7\64\2\2\u05de\u05e4\7\24\2\2\u05df\u05e4\79\2\2\u05e0")
        buf.write("\u05e4\7\r\2\2\u05e1\u05e4\7\5\2\2\u05e2\u05e4\7:\2\2")
        buf.write("\u05e3\u05da\3\2\2\2\u05e3\u05db\3\2\2\2\u05e3\u05dc\3")
        buf.write("\2\2\2\u05e3\u05dd\3\2\2\2\u05e3\u05de\3\2\2\2\u05e3\u05df")
        buf.write("\3\2\2\2\u05e3\u05e0\3\2\2\2\u05e3\u05e1\3\2\2\2\u05e3")
        buf.write("\u05e2\3\2\2\2\u05e4\u00eb\3\2\2\2\u05e5\u05e6\7$\2\2")
        buf.write("\u05e6\u05e7\5t;\2\u05e7\u00ed\3\2\2\2\u05e8\u05e9\7\t")
        buf.write("\2\2\u05e9\u05ee\5@!\2\u05ea\u05eb\7U\2\2\u05eb\u05ed")
        buf.write("\5@!\2\u05ec\u05ea\3\2\2\2\u05ed\u05f0\3\2\2\2\u05ee\u05ec")
        buf.write("\3\2\2\2\u05ee\u05ef\3\2\2\2\u05ef\u00ef\3\2\2\2\u05f0")
        buf.write("\u05ee\3\2\2\2\u05f1\u05f5\7P\2\2\u05f2\u05f4\5\u00f2")
        buf.write("z\2\u05f3\u05f2\3\2\2\2\u05f4\u05f7\3\2\2\2\u05f5\u05f3")
        buf.write("\3\2\2\2\u05f5\u05f6\3\2\2\2\u05f6\u05f8\3\2\2\2\u05f7")
        buf.write("\u05f5\3\2\2\2\u05f8\u05f9\7Q\2\2\u05f9\u00f1\3\2\2\2")
        buf.write("\u05fa\u0600\5\u00f4{\2\u05fb\u0600\5\u00f8}\2\u05fc\u0600")
        buf.write("\5f\64\2\u05fd\u0600\5\u00e6t\2\u05fe\u0600\7T\2\2\u05ff")
        buf.write("\u05fa\3\2\2\2\u05ff\u05fb\3\2\2\2\u05ff\u05fc\3\2\2\2")
        buf.write("\u05ff\u05fd\3\2\2\2\u05ff\u05fe\3\2\2\2\u0600\u00f3\3")
        buf.write("\2\2\2\u0601\u0603\5\u00f6|\2\u0602\u0601\3\2\2\2\u0603")
        buf.write("\u0606\3\2\2\2\u0604\u0602\3\2\2\2\u0604\u0605\3\2\2\2")
        buf.write("\u0605\u0607\3\2\2\2\u0606\u0604\3\2\2\2\u0607\u0608\5")
        buf.write("\u008aF\2\u0608\u0609\5\u0082B\2\u0609\u060a\7T\2\2\u060a")
        buf.write("\u00f5\3\2\2\2\u060b\u0610\5\u0108\u0085\2\u060c\u0610")
        buf.write("\7\66\2\2\u060d\u0610\79\2\2\u060e\u0610\7%\2\2\u060f")
        buf.write("\u060b\3\2\2\2\u060f\u060c\3\2\2\2\u060f\u060d\3\2\2\2")
        buf.write("\u060f\u060e\3\2\2\2\u0610\u00f7\3\2\2\2\u0611\u0613\5")
        buf.write("\u00fa~\2\u0612\u0611\3\2\2\2\u0613\u0616\3\2\2\2\u0614")
        buf.write("\u0612\3\2\2\2\u0614\u0615\3\2\2\2\u0615\u0617\3\2\2\2")
        buf.write("\u0616\u0614\3\2\2\2\u0617\u0618\5\u00a0Q\2\u0618\u0619")
        buf.write("\5\u00b6\\\2\u0619\u00f9\3\2\2\2\u061a\u0622\5\u0108\u0085")
        buf.write("\2\u061b\u0622\7\66\2\2\u061c\u0622\7\64\2\2\u061d\u0622")
        buf.write("\7\24\2\2\u061e\u0622\7\37\2\2\u061f\u0622\79\2\2\u0620")
        buf.write("\u0622\7:\2\2\u0621\u061a\3\2\2\2\u0621\u061b\3\2\2\2")
        buf.write("\u0621\u061c\3\2\2\2\u0621\u061d\3\2\2\2\u0621\u061e\3")
        buf.write("\2\2\2\u0621\u061f\3\2\2\2\u0621\u0620\3\2\2\2\u0622\u00fb")
        buf.write("\3\2\2\2\u0623\u0625\5\u00eav\2\u0624\u0623\3\2\2\2\u0625")
        buf.write("\u0628\3\2\2\2\u0626\u0624\3\2\2\2\u0626\u0627\3\2\2\2")
        buf.write("\u0627\u0629\3\2\2\2\u0628\u0626\3\2\2\2\u0629\u062a\7")
        buf.write("X\2\2\u062a\u062b\7/\2\2\u062b\u062c\5\6\4\2\u062c\u062d")
        buf.write("\5\u00fe\u0080\2\u062d\u00fd\3\2\2\2\u062e\u0632\7P\2")
        buf.write("\2\u062f\u0631\5\u0100\u0081\2\u0630\u062f\3\2\2\2\u0631")
        buf.write("\u0634\3\2\2\2\u0632\u0630\3\2\2\2\u0632\u0633\3\2\2\2")
        buf.write("\u0633\u0635\3\2\2\2\u0634\u0632\3\2\2\2\u0635\u0636\7")
        buf.write("Q\2\2\u0636\u00ff\3\2\2\2\u0637\u063d\5\u0102\u0082\2")
        buf.write("\u0638\u063d\5\u00f4{\2\u0639\u063d\5f\64\2\u063a\u063d")
        buf.write("\5\u00e6t\2\u063b\u063d\7T\2\2\u063c\u0637\3\2\2\2\u063c")
        buf.write("\u0638\3\2\2\2\u063c\u0639\3\2\2\2\u063c\u063a\3\2\2\2")
        buf.write("\u063c\u063b\3\2\2\2\u063d\u0101\3\2\2\2\u063e\u0640\5")
        buf.write("\u0104\u0083\2\u063f\u063e\3\2\2\2\u0640\u0643\3\2\2\2")
        buf.write("\u0641\u063f\3\2\2\2\u0641\u0642\3\2\2\2\u0642\u0644\3")
        buf.write("\2\2\2\u0643\u0641\3\2\2\2\u0644\u0645\5\u008aF\2\u0645")
        buf.write("\u0646\5\4\3\2\u0646\u0647\7N\2\2\u0647\u0649\7O\2\2\u0648")
        buf.write("\u064a\5(\25\2\u0649\u0648\3\2\2\2\u0649\u064a\3\2\2\2")
        buf.write("\u064a\u064c\3\2\2\2\u064b\u064d\5\u0106\u0084\2\u064c")
        buf.write("\u064b\3\2\2\2\u064c\u064d\3\2\2\2\u064d\u064e\3\2\2\2")
        buf.write("\u064e\u064f\7T\2\2\u064f\u0103\3\2\2\2\u0650\u0654\5")
        buf.write("\u0108\u0085\2\u0651\u0654\7\66\2\2\u0652\u0654\7\24\2")
        buf.write("\2\u0653\u0650\3\2\2\2\u0653\u0651\3\2\2\2\u0653\u0652")
        buf.write("\3\2\2\2\u0654\u0105\3\2\2\2\u0655\u0656\7\37\2\2\u0656")
        buf.write("\u0657\5\u0110\u0089\2\u0657\u0107\3\2\2\2\u0658\u065c")
        buf.write("\5\u010a\u0086\2\u0659\u065c\5\u0116\u008c\2\u065a\u065c")
        buf.write("\5\u0118\u008d\2\u065b\u0658\3\2\2\2\u065b\u0659\3\2\2")
        buf.write("\2\u065b\u065a\3\2\2\2\u065c\u0109\3\2\2\2\u065d\u065e")
        buf.write("\7X\2\2\u065e\u065f\5@!\2\u065f\u0661\7N\2\2\u0660\u0662")
        buf.write("\5\u010c\u0087\2\u0661\u0660\3\2\2\2\u0661\u0662\3\2\2")
        buf.write("\2\u0662\u0663\3\2\2\2\u0663\u0664\7O\2\2\u0664\u010b")
        buf.write("\3\2\2\2\u0665\u066a\5\u010e\u0088\2\u0666\u0667\7U\2")
        buf.write("\2\u0667\u0669\5\u010e\u0088\2\u0668\u0666\3\2\2\2\u0669")
        buf.write("\u066c\3\2\2\2\u066a\u0668\3\2\2\2\u066a\u066b\3\2\2\2")
        buf.write("\u066b\u010d\3\2\2\2\u066c\u066a\3\2\2\2\u066d\u066e\5")
        buf.write("\4\3\2\u066e\u066f\7Z\2\2\u066f\u0670\5\u0110\u0089\2")
        buf.write("\u0670\u010f\3\2\2\2\u0671\u0675\5\u01da\u00ee\2\u0672")
        buf.write("\u0675\5\u0112\u008a\2\u0673\u0675\5\u0108\u0085\2\u0674")
        buf.write("\u0671\3\2\2\2\u0674\u0672\3\2\2\2\u0674\u0673\3\2\2\2")
        buf.write("\u0675\u0111\3\2\2\2\u0676\u0678\7P\2\2\u0677\u0679\5")
        buf.write("\u0114\u008b\2\u0678\u0677\3\2\2\2\u0678\u0679\3\2\2\2")
        buf.write("\u0679\u067b\3\2\2\2\u067a\u067c\7U\2\2\u067b\u067a\3")
        buf.write("\2\2\2\u067b\u067c\3\2\2\2\u067c\u067d\3\2\2\2\u067d\u067e")
        buf.write("\7Q\2\2\u067e\u0113\3\2\2\2\u067f\u0684\5\u0110\u0089")
        buf.write("\2\u0680\u0681\7U\2\2\u0681\u0683\5\u0110\u0089\2\u0682")
        buf.write("\u0680\3\2\2\2\u0683\u0686\3\2\2\2\u0684\u0682\3\2\2\2")
        buf.write("\u0684\u0685\3\2\2\2\u0685\u0115\3\2\2\2\u0686\u0684\3")
        buf.write("\2\2\2\u0687\u0688\7X\2\2\u0688\u0689\5@!\2\u0689\u0117")
        buf.write("\3\2\2\2\u068a\u068b\7X\2\2\u068b\u068c\5@!\2\u068c\u068d")
        buf.write("\7N\2\2\u068d\u068e\5\u0110\u0089\2\u068e\u068f\7O\2\2")
        buf.write("\u068f\u0119\3\2\2\2\u0690\u0692\7P\2\2\u0691\u0693\5")
        buf.write("\u011c\u008f\2\u0692\u0691\3\2\2\2\u0692\u0693\3\2\2\2")
        buf.write("\u0693\u0695\3\2\2\2\u0694\u0696\7U\2\2\u0695\u0694\3")
        buf.write("\2\2\2\u0695\u0696\3\2\2\2\u0696\u0697\3\2\2\2\u0697\u0698")
        buf.write("\7Q\2\2\u0698\u011b\3\2\2\2\u0699\u069e\5\u0088E\2\u069a")
        buf.write("\u069b\7U\2\2\u069b\u069d\5\u0088E\2\u069c\u069a\3\2\2")
        buf.write("\2\u069d\u06a0\3\2\2\2\u069e\u069c\3\2\2\2\u069e\u069f")
        buf.write("\3\2\2\2\u069f\u011d\3\2\2\2\u06a0\u069e\3\2\2\2\u06a1")
        buf.write("\u06a3\7P\2\2\u06a2\u06a4\5\u0120\u0091\2\u06a3\u06a2")
        buf.write("\3\2\2\2\u06a3\u06a4\3\2\2\2\u06a4\u06a5\3\2\2\2\u06a5")
        buf.write("\u06a6\7Q\2\2\u06a6\u011f\3\2\2\2\u06a7\u06ab\5\u0122")
        buf.write("\u0092\2\u06a8\u06aa\5\u0122\u0092\2\u06a9\u06a8\3\2\2")
        buf.write("\2\u06aa\u06ad\3\2\2\2\u06ab\u06a9\3\2\2\2\u06ab\u06ac")
        buf.write("\3\2\2\2\u06ac\u0121\3\2\2\2\u06ad\u06ab\3\2\2\2\u06ae")
        buf.write("\u06b2\5\u0124\u0093\2\u06af\u06b2\5\u012a\u0096\2\u06b0")
        buf.write("\u06b2\5\u012c\u0097\2\u06b1\u06ae\3\2\2\2\u06b1\u06af")
        buf.write("\3\2\2\2\u06b1\u06b0\3\2\2\2\u06b2\u0123\3\2\2\2\u06b3")
        buf.write("\u06b6\5f\64\2\u06b4\u06b6\5\u00e8u\2\u06b5\u06b3\3\2")
        buf.write("\2\2\u06b5\u06b4\3\2\2\2\u06b6\u0125\3\2\2\2\u06b7\u06b9")
        buf.write("\5\u00aeX\2\u06b8\u06b7\3\2\2\2\u06b9\u06bc\3\2\2\2\u06ba")
        buf.write("\u06b8\3\2\2\2\u06ba\u06bb\3\2\2\2\u06bb\u06bd\3\2\2\2")
        buf.write("\u06bc\u06ba\3\2\2\2\u06bd\u06be\5\u0128\u0095\2\u06be")
        buf.write("\u06bf\5\u0082B\2\u06bf\u0127\3\2\2\2\u06c0\u06c3\5\u008a")
        buf.write("F\2\u06c1\u06c3\7\21\2\2\u06c2\u06c0\3\2\2\2\u06c2\u06c1")
        buf.write("\3\2\2\2\u06c3\u0129\3\2\2\2\u06c4\u06c5\5\u0126\u0094")
        buf.write("\2\u06c5\u06c6\7T\2\2\u06c6\u012b\3\2\2\2\u06c7\u06ce")
        buf.write("\5\u0130\u0099\2\u06c8\u06ce\5\u0134\u009b\2\u06c9\u06ce")
        buf.write("\5\u013c\u009f\2\u06ca\u06ce\5\u013e\u00a0\2\u06cb\u06ce")
        buf.write("\5\u0150\u00a9\2\u06cc\u06ce\5\u0156\u00ac\2\u06cd\u06c7")
        buf.write("\3\2\2\2\u06cd\u06c8\3\2\2\2\u06cd\u06c9\3\2\2\2\u06cd")
        buf.write("\u06ca\3\2\2\2\u06cd\u06cb\3\2\2\2\u06cd\u06cc\3\2\2\2")
        buf.write("\u06ce\u012d\3\2\2\2\u06cf\u06d5\5\u0130\u0099\2\u06d0")
        buf.write("\u06d5\5\u0136\u009c\2\u06d1\u06d5\5\u0140\u00a1\2\u06d2")
        buf.write("\u06d5\5\u0152\u00aa\2\u06d3\u06d5\5\u0158\u00ad\2\u06d4")
        buf.write("\u06cf\3\2\2\2\u06d4\u06d0\3\2\2\2\u06d4\u06d1\3\2\2\2")
        buf.write("\u06d4\u06d2\3\2\2\2\u06d4\u06d3\3\2\2\2\u06d5\u012f\3")
        buf.write("\2\2\2\u06d6\u06e4\5\u011e\u0090\2\u06d7\u06e4\5\u0132")
        buf.write("\u009a\2\u06d8\u06e4\5\u0138\u009d\2\u06d9\u06e4\5\u0142")
        buf.write("\u00a2\2\u06da\u06e4\5\u0144\u00a3\2\u06db\u06e4\5\u0154")
        buf.write("\u00ab\2\u06dc\u06e4\5\u0168\u00b5\2\u06dd\u06e4\5\u016a")
        buf.write("\u00b6\2\u06de\u06e4\5\u016c\u00b7\2\u06df\u06e4\5\u0170")
        buf.write("\u00b9\2\u06e0\u06e4\5\u016e\u00b8\2\u06e1\u06e4\5\u0172")
        buf.write("\u00ba\2\u06e2\u06e4\5\u0188\u00c5\2\u06e3\u06d6\3\2\2")
        buf.write("\2\u06e3\u06d7\3\2\2\2\u06e3\u06d8\3\2\2\2\u06e3\u06d9")
        buf.write("\3\2\2\2\u06e3\u06da\3\2\2\2\u06e3\u06db\3\2\2\2\u06e3")
        buf.write("\u06dc\3\2\2\2\u06e3\u06dd\3\2\2\2\u06e3\u06de\3\2\2\2")
        buf.write("\u06e3\u06df\3\2\2\2\u06e3\u06e0\3\2\2\2\u06e3\u06e1\3")
        buf.write("\2\2\2\u06e3\u06e2\3\2\2\2\u06e4\u0131\3\2\2\2\u06e5\u06e6")
        buf.write("\7T\2\2\u06e6\u0133\3\2\2\2\u06e7\u06e8\5\4\3\2\u06e8")
        buf.write("\u06e9\7`\2\2\u06e9\u06ea\5\u012c\u0097\2\u06ea\u0135")
        buf.write("\3\2\2\2\u06eb\u06ec\5\4\3\2\u06ec\u06ed\7`\2\2\u06ed")
        buf.write("\u06ee\5\u012e\u0098\2\u06ee\u0137\3\2\2\2\u06ef\u06f0")
        buf.write("\5\u013a\u009e\2\u06f0\u06f1\7T\2\2\u06f1\u0139\3\2\2")
        buf.write("\2\u06f2\u06fa\5\u01de\u00f0\2\u06f3\u06fa\5\u01be\u00e0")
        buf.write("\2\u06f4\u06fa\5\u01c0\u00e1\2\u06f5\u06fa\5\u01b8\u00dd")
        buf.write("\2\u06f6\u06fa\5\u01ba\u00de\2\u06f7\u06fa\5\u01ae\u00d8")
        buf.write("\2\u06f8\u06fa\5\u0198\u00cd\2\u06f9\u06f2\3\2\2\2\u06f9")
        buf.write("\u06f3\3\2\2\2\u06f9\u06f4\3\2\2\2\u06f9\u06f5\3\2\2\2")
        buf.write("\u06f9\u06f6\3\2\2\2\u06f9\u06f7\3\2\2\2\u06f9\u06f8\3")
        buf.write("\2\2\2\u06fa\u013b\3\2\2\2\u06fb\u06fc\7)\2\2\u06fc\u06fd")
        buf.write("\7N\2\2\u06fd\u06fe\5\u018e\u00c8\2\u06fe\u06ff\7O\2\2")
        buf.write("\u06ff\u0700\5\u012c\u0097\2\u0700\u013d\3\2\2\2\u0701")
        buf.write("\u0702\7)\2\2\u0702\u0703\7N\2\2\u0703\u0704\5\u018e\u00c8")
        buf.write("\2\u0704\u0705\7O\2\2\u0705\u0706\5\u012e\u0098\2\u0706")
        buf.write("\u0707\7\"\2\2\u0707\u0708\5\u012c\u0097\2\u0708\u013f")
        buf.write("\3\2\2\2\u0709\u070a\7)\2\2\u070a\u070b\7N\2\2\u070b\u070c")
        buf.write("\5\u018e\u00c8\2\u070c\u070d\7O\2\2\u070d\u070e\5\u012e")
        buf.write("\u0098\2\u070e\u070f\7\"\2\2\u070f\u0710\5\u012e\u0098")
        buf.write("\2\u0710\u0141\3\2\2\2\u0711\u0712\7\25\2\2\u0712\u0715")
        buf.write("\5\u018e\u00c8\2\u0713\u0714\7`\2\2\u0714\u0716\5\u018e")
        buf.write("\u00c8\2\u0715\u0713\3\2\2\2\u0715\u0716\3\2\2\2\u0716")
        buf.write("\u0717\3\2\2\2\u0717\u0718\7T\2\2\u0718\u0143\3\2\2\2")
        buf.write("\u0719\u071a\7<\2\2\u071a\u071b\7N\2\2\u071b\u071c\5\u018e")
        buf.write("\u00c8\2\u071c\u071d\7O\2\2\u071d\u071e\5\u0146\u00a4")
        buf.write("\2\u071e\u0145\3\2\2\2\u071f\u0720\7P\2\2\u0720\u0724")
        buf.write("\5\u0148\u00a5\2\u0721\u0723\5\u0148\u00a5\2\u0722\u0721")
        buf.write("\3\2\2\2\u0723\u0726\3\2\2\2\u0724\u0722\3\2\2\2\u0724")
        buf.write("\u0725\3\2\2\2\u0725\u0727\3\2\2\2\u0726\u0724\3\2\2\2")
        buf.write("\u0727\u0728\7Q\2\2\u0728\u073a\3\2\2\2\u0729\u072d\7")
        buf.write("P\2\2\u072a\u072c\5\u014a\u00a6\2\u072b\u072a\3\2\2\2")
        buf.write("\u072c\u072f\3\2\2\2\u072d\u072b\3\2\2\2\u072d\u072e\3")
        buf.write("\2\2\2\u072e\u0735\3\2\2\2\u072f\u072d\3\2\2\2\u0730\u0731")
        buf.write("\5\u014c\u00a7\2\u0731\u0732\7`\2\2\u0732\u0734\3\2\2")
        buf.write("\2\u0733\u0730\3\2\2\2\u0734\u0737\3\2\2\2\u0735\u0733")
        buf.write("\3\2\2\2\u0735\u0736\3\2\2\2\u0736\u0738\3\2\2\2\u0737")
        buf.write("\u0735\3\2\2\2\u0738\u073a\7Q\2\2\u0739\u071f\3\2\2\2")
        buf.write("\u0739\u0729\3\2\2\2\u073a\u0147\3\2\2\2\u073b\u073c\5")
        buf.write("\u014c\u00a7\2\u073c\u0742\7a\2\2\u073d\u073e\5\u018e")
        buf.write("\u00c8\2\u073e\u073f\7T\2\2\u073f\u0743\3\2\2\2\u0740")
        buf.write("\u0743\5\u011e\u0090\2\u0741\u0743\5\u016e\u00b8\2\u0742")
        buf.write("\u073d\3\2\2\2\u0742\u0740\3\2\2\2\u0742\u0741\3\2\2\2")
        buf.write("\u0743\u0149\3\2\2\2\u0744\u0745\5\u014c\u00a7\2\u0745")
        buf.write("\u074b\7`\2\2\u0746\u0747\5\u014c\u00a7\2\u0747\u0748")
        buf.write("\7`\2\2\u0748\u074a\3\2\2\2\u0749\u0746\3\2\2\2\u074a")
        buf.write("\u074d\3\2\2\2\u074b\u0749\3\2\2\2\u074b\u074c\3\2\2\2")
        buf.write("\u074c\u074e\3\2\2\2\u074d\u074b\3\2\2\2\u074e\u074f\5")
        buf.write("\u0120\u0091\2\u074f\u014b\3\2\2\2\u0750\u0751\7\31\2")
        buf.write("\2\u0751\u0756\5\u014e\u00a8\2\u0752\u0753\7U\2\2\u0753")
        buf.write("\u0755\5\u014e\u00a8\2\u0754\u0752\3\2\2\2\u0755\u0758")
        buf.write("\3\2\2\2\u0756\u0754\3\2\2\2\u0756\u0757\3\2\2\2\u0757")
        buf.write("\u075b\3\2\2\2\u0758\u0756\3\2\2\2\u0759\u075b\7\37\2")
        buf.write("\2\u075a\u0750\3\2\2\2\u075a\u0759\3\2\2\2\u075b\u014d")
        buf.write("\3\2\2\2\u075c\u075d\5\u01da\u00ee\2\u075d\u014f\3\2\2")
        buf.write("\2\u075e\u075f\7E\2\2\u075f\u0760\7N\2\2\u0760\u0761\5")
        buf.write("\u018e\u00c8\2\u0761\u0762\7O\2\2\u0762\u0763\5\u012c")
        buf.write("\u0097\2\u0763\u0151\3\2\2\2\u0764\u0765\7E\2\2\u0765")
        buf.write("\u0766\7N\2\2\u0766\u0767\5\u018e\u00c8\2\u0767\u0768")
        buf.write("\7O\2\2\u0768\u0769\5\u012e\u0098\2\u0769\u0153\3\2\2")
        buf.write("\2\u076a\u076b\7 \2\2\u076b\u076c\5\u012c\u0097\2\u076c")
        buf.write("\u076d\7E\2\2\u076d\u076e\7N\2\2\u076e\u076f\5\u018e\u00c8")
        buf.write("\2\u076f\u0770\7O\2\2\u0770\u0771\7T\2\2\u0771\u0155\3")
        buf.write("\2\2\2\u0772\u0775\5\u015a\u00ae\2\u0773\u0775\5\u0164")
        buf.write("\u00b3\2\u0774\u0772\3\2\2\2\u0774\u0773\3\2\2\2\u0775")
        buf.write("\u0157\3\2\2\2\u0776\u0779\5\u015c\u00af\2\u0777\u0779")
        buf.write("\5\u0166\u00b4\2\u0778\u0776\3\2\2\2\u0778\u0777\3\2\2")
        buf.write("\2\u0779\u0159\3\2\2\2\u077a\u077b\7(\2\2\u077b\u077d")
        buf.write("\7N\2\2\u077c\u077e\5\u015e\u00b0\2\u077d\u077c\3\2\2")
        buf.write("\2\u077d\u077e\3\2\2\2\u077e\u077f\3\2\2\2\u077f\u0781")
        buf.write("\7T\2\2\u0780\u0782\5\u018e\u00c8\2\u0781\u0780\3\2\2")
        buf.write("\2\u0781\u0782\3\2\2\2\u0782\u0783\3\2\2\2\u0783\u0785")
        buf.write("\7T\2\2\u0784\u0786\5\u0160\u00b1\2\u0785\u0784\3\2\2")
        buf.write("\2\u0785\u0786\3\2\2\2\u0786\u0787\3\2\2\2\u0787\u0788")
        buf.write("\7O\2\2\u0788\u0789\5\u012c\u0097\2\u0789\u015b\3\2\2")
        buf.write("\2\u078a\u078b\7(\2\2\u078b\u078d\7N\2\2\u078c\u078e\5")
        buf.write("\u015e\u00b0\2\u078d\u078c\3\2\2\2\u078d\u078e\3\2\2\2")
        buf.write("\u078e\u078f\3\2\2\2\u078f\u0791\7T\2\2\u0790\u0792\5")
        buf.write("\u018e\u00c8\2\u0791\u0790\3\2\2\2\u0791\u0792\3\2\2\2")
        buf.write("\u0792\u0793\3\2\2\2\u0793\u0795\7T\2\2\u0794\u0796\5")
        buf.write("\u0160\u00b1\2\u0795\u0794\3\2\2\2\u0795\u0796\3\2\2\2")
        buf.write("\u0796\u0797\3\2\2\2\u0797\u0798\7O\2\2\u0798\u0799\5")
        buf.write("\u012e\u0098\2\u0799\u015d\3\2\2\2\u079a\u079d\5\u0162")
        buf.write("\u00b2\2\u079b\u079d\5\u0126\u0094\2\u079c\u079a\3\2\2")
        buf.write("\2\u079c\u079b\3\2\2\2\u079d\u015f\3\2\2\2\u079e\u079f")
        buf.write("\5\u0162\u00b2\2\u079f\u0161\3\2\2\2\u07a0\u07a5\5\u013a")
        buf.write("\u009e\2\u07a1\u07a2\7U\2\2\u07a2\u07a4\5\u013a\u009e")
        buf.write("\2\u07a3\u07a1\3\2\2\2\u07a4\u07a7\3\2\2\2\u07a5\u07a3")
        buf.write("\3\2\2\2\u07a5\u07a6\3\2\2\2\u07a6\u0163\3\2\2\2\u07a7")
        buf.write("\u07a5\3\2\2\2\u07a8\u07a9\7(\2\2\u07a9\u07aa\7N\2\2\u07aa")
        buf.write("\u07ab\5\u0126\u0094\2\u07ab\u07ac\7`\2\2\u07ac\u07ad")
        buf.write("\5\u018e\u00c8\2\u07ad\u07ae\7O\2\2\u07ae\u07af\5\u012c")
        buf.write("\u0097\2\u07af\u0165\3\2\2\2\u07b0\u07b1\7(\2\2\u07b1")
        buf.write("\u07b2\7N\2\2\u07b2\u07b3\5\u0126\u0094\2\u07b3\u07b4")
        buf.write("\7`\2\2\u07b4\u07b5\5\u018e\u00c8\2\u07b5\u07b6\7O\2\2")
        buf.write("\u07b6\u07b7\5\u012e\u0098\2\u07b7\u0167\3\2\2\2\u07b8")
        buf.write("\u07ba\7\27\2\2\u07b9\u07bb\5\4\3\2\u07ba\u07b9\3\2\2")
        buf.write("\2\u07ba\u07bb\3\2\2\2\u07bb\u07bc\3\2\2\2\u07bc\u07bd")
        buf.write("\7T\2\2\u07bd\u0169\3\2\2\2\u07be\u07c0\7\36\2\2\u07bf")
        buf.write("\u07c1\5\4\3\2\u07c0\u07bf\3\2\2\2\u07c0\u07c1\3\2\2\2")
        buf.write("\u07c1\u07c2\3\2\2\2\u07c2\u07c3\7T\2\2\u07c3\u016b\3")
        buf.write("\2\2\2\u07c4\u07c6\7\67\2\2\u07c5\u07c7\5\u018e\u00c8")
        buf.write("\2\u07c6\u07c5\3\2\2\2\u07c6\u07c7\3\2\2\2\u07c7\u07c8")
        buf.write("\3\2\2\2\u07c8\u07c9\7T\2\2\u07c9\u016d\3\2\2\2\u07ca")
        buf.write("\u07cb\7?\2\2\u07cb\u07cc\5\u018e\u00c8\2\u07cc\u07cd")
        buf.write("\7T\2\2\u07cd\u016f\3\2\2\2\u07ce\u07cf\7=\2\2\u07cf\u07d0")
        buf.write("\7N\2\2\u07d0\u07d1\5\u018e\u00c8\2\u07d1\u07d2\7O\2\2")
        buf.write("\u07d2\u07d3\5\u011e\u0090\2\u07d3\u0171\3\2\2\2\u07d4")
        buf.write("\u07d5\7B\2\2\u07d5\u07d6\5\u011e\u0090\2\u07d6\u07d7")
        buf.write("\5\u0174\u00bb\2\u07d7\u07e5\3\2\2\2\u07d8\u07d9\7B\2")
        buf.write("\2\u07d9\u07da\5\u011e\u0090\2\u07da\u07db\5\u017c\u00bf")
        buf.write("\2\u07db\u07e5\3\2\2\2\u07dc\u07dd\7B\2\2\u07dd\u07df")
        buf.write("\5\u011e\u0090\2\u07de\u07e0\5\u0174\u00bb\2\u07df\u07de")
        buf.write("\3\2\2\2\u07df\u07e0\3\2\2\2\u07e0\u07e1\3\2\2\2\u07e1")
        buf.write("\u07e2\5\u017c\u00bf\2\u07e2\u07e5\3\2\2\2\u07e3\u07e5")
        buf.write("\5\u017e\u00c0\2\u07e4\u07d4\3\2\2\2\u07e4\u07d8\3\2\2")
        buf.write("\2\u07e4\u07dc\3\2\2\2\u07e4\u07e3\3\2\2\2\u07e5\u0173")
        buf.write("\3\2\2\2\u07e6\u07ea\5\u0176\u00bc\2\u07e7\u07e9\5\u0176")
        buf.write("\u00bc\2\u07e8\u07e7\3\2\2\2\u07e9\u07ec\3\2\2\2\u07ea")
        buf.write("\u07e8\3\2\2\2\u07ea\u07eb\3\2\2\2\u07eb\u0175\3\2\2\2")
        buf.write("\u07ec\u07ea\3\2\2\2\u07ed\u07ee\7\32\2\2\u07ee\u07ef")
        buf.write("\7N\2\2\u07ef\u07f0\5\u0178\u00bd\2\u07f0\u07f1\7O\2\2")
        buf.write("\u07f1\u07f2\5\u011e\u0090\2\u07f2\u0177\3\2\2\2\u07f3")
        buf.write("\u07f5\5\u00aeX\2\u07f4\u07f3\3\2\2\2\u07f5\u07f8\3\2")
        buf.write("\2\2\u07f6\u07f4\3\2\2\2\u07f6\u07f7\3\2\2\2\u07f7\u07f9")
        buf.write("\3\2\2\2\u07f8\u07f6\3\2\2\2\u07f9\u07fa\5\u017a\u00be")
        buf.write("\2\u07fa\u07fb\5\u0086D\2\u07fb\u0179\3\2\2\2\u07fc\u0801")
        buf.write("\5\u0094K\2\u07fd\u07fe\7o\2\2\u07fe\u0800\5 \21\2\u07ff")
        buf.write("\u07fd\3\2\2\2\u0800\u0803\3\2\2\2\u0801\u07ff\3\2\2\2")
        buf.write("\u0801\u0802\3\2\2\2\u0802\u017b\3\2\2\2\u0803\u0801\3")
        buf.write("\2\2\2\u0804\u0805\7&\2\2\u0805\u0806\5\u011e\u0090\2")
        buf.write("\u0806\u017d\3\2\2\2\u0807\u0808\7B\2\2\u0808\u0809\5")
        buf.write("\u0180\u00c1\2\u0809\u080b\5\u011e\u0090\2\u080a\u080c")
        buf.write("\5\u0174\u00bb\2\u080b\u080a\3\2\2\2\u080b\u080c\3\2\2")
        buf.write("\2\u080c\u080e\3\2\2\2\u080d\u080f\5\u017c\u00bf\2\u080e")
        buf.write("\u080d\3\2\2\2\u080e\u080f\3\2\2\2\u080f\u017f\3\2\2\2")
        buf.write("\u0810\u0811\7N\2\2\u0811\u0813\5\u0182\u00c2\2\u0812")
        buf.write("\u0814\7T\2\2\u0813\u0812\3\2\2\2\u0813\u0814\3\2\2\2")
        buf.write("\u0814\u0815\3\2\2\2\u0815\u0816\7O\2\2\u0816\u0181\3")
        buf.write("\2\2\2\u0817\u081c\5\u0184\u00c3\2\u0818\u0819\7T\2\2")
        buf.write("\u0819\u081b\5\u0184\u00c3\2\u081a\u0818\3\2\2\2\u081b")
        buf.write("\u081e\3\2\2\2\u081c\u081a\3\2\2\2\u081c\u081d\3\2\2\2")
        buf.write("\u081d\u0183\3\2\2\2\u081e\u081c\3\2\2\2\u081f\u0822\5")
        buf.write("\u0126\u0094\2\u0820\u0822\5\u0186\u00c4\2\u0821\u081f")
        buf.write("\3\2\2\2\u0821\u0820\3\2\2\2\u0822\u0185\3\2\2\2\u0823")
        buf.write("\u0826\5D#\2\u0824\u0826\5\u01ac\u00d7\2\u0825\u0823\3")
        buf.write("\2\2\2\u0825\u0824\3\2\2\2\u0826\u0187\3\2\2\2\u0827\u0828")
        buf.write("\7\23\2\2\u0828\u0829\5\u018e\u00c8\2\u0829\u082a\7T\2")
        buf.write("\2\u082a\u0189\3\2\2\2\u082b\u082c\5\u018c\u00c7\2\u082c")
        buf.write("\u018b\3\2\2\2\u082d\u082e\5\u0126\u0094\2\u082e\u018d")
        buf.write("\3\2\2\2\u082f\u0832\5\u01e4\u00f3\2\u0830\u0832\5\u01dc")
        buf.write("\u00ef\2\u0831\u082f\3\2\2\2\u0831\u0830\3\2\2\2\u0832")
        buf.write("\u018f\3\2\2\2\u0833\u0836\5\u0192\u00ca\2\u0834\u0836")
        buf.write("\5\u01a0\u00d1\2\u0835\u0833\3\2\2\2\u0835\u0834\3\2\2")
        buf.write("\2\u0836\u0191\3\2\2\2\u0837\u0839\5\20\t\2\u0838\u083a")
        buf.write("\5\u0194\u00cb\2\u0839\u0838\3\2\2\2\u0839\u083a\3\2\2")
        buf.write("\2\u083a\u0911\3\2\2\2\u083b\u083d\5\u0196\u00cc\2\u083c")
        buf.write("\u083e\5\u0194\u00cb\2\u083d\u083c\3\2\2\2\u083d\u083e")
        buf.write("\3\2\2\2\u083e\u0911\3\2\2\2\u083f\u0841\7>\2\2\u0840")
        buf.write("\u0842\5\u0194\u00cb\2\u0841\u0840\3\2\2\2\u0841\u0842")
        buf.write("\3\2\2\2\u0842\u0911\3\2\2\2\u0843\u0844\5@!\2\u0844\u0845")
        buf.write("\7V\2\2\u0845\u0847\7>\2\2\u0846\u0848\5\u0194\u00cb\2")
        buf.write("\u0847\u0846\3\2\2\2\u0847\u0848\3\2\2\2\u0848\u0911\3")
        buf.write("\2\2\2\u0849\u084a\7N\2\2\u084a\u084b\5\u018e\u00c8\2")
        buf.write("\u084b\u084d\7O\2\2\u084c\u084e\5\u0194\u00cb\2\u084d")
        buf.write("\u084c\3\2\2\2\u084d\u084e\3\2\2\2\u084e\u0911\3\2\2\2")
        buf.write("\u084f\u0851\5\u019a\u00ce\2\u0850\u0852\5\u0194\u00cb")
        buf.write("\2\u0851\u0850\3\2\2\2\u0851\u0852\3\2\2\2\u0852\u0911")
        buf.write("\3\2\2\2\u0853\u0854\5D#\2\u0854\u0855\7V\2\2\u0855\u0857")
        buf.write("\5\u019a\u00ce\2\u0856\u0858\5\u0194\u00cb\2\u0857\u0856")
        buf.write("\3\2\2\2\u0857\u0858\3\2\2\2\u0858\u0911\3\2\2\2\u0859")
        buf.write("\u085a\5\u01a0\u00d1\2\u085a\u085b\7V\2\2\u085b\u085d")
        buf.write("\5\u019a\u00ce\2\u085c\u085e\5\u0194\u00cb\2\u085d\u085c")
        buf.write("\3\2\2\2\u085d\u085e\3\2\2\2\u085e\u0911\3\2\2\2\u085f")
        buf.write("\u0860\5\u01a0\u00d1\2\u0860\u0861\7V\2\2\u0861\u0863")
        buf.write("\5\4\3\2\u0862\u0864\5\u0194\u00cb\2\u0863\u0862\3\2\2")
        buf.write("\2\u0863\u0864\3\2\2\2\u0864\u0911\3\2\2\2\u0865\u0866")
        buf.write("\7;\2\2\u0866\u0867\7V\2\2\u0867\u0869\5\4\3\2\u0868\u086a")
        buf.write("\5\u0194\u00cb\2\u0869\u0868\3\2\2\2\u0869\u086a\3\2\2")
        buf.write("\2\u086a\u0911\3\2\2\2\u086b\u086c\5@!\2\u086c\u086d\7")
        buf.write("V\2\2\u086d\u086e\7;\2\2\u086e\u086f\7V\2\2\u086f\u0871")
        buf.write("\5\4\3\2\u0870\u0872\5\u0194\u00cb\2\u0871\u0870\3\2\2")
        buf.write("\2\u0871\u0872\3\2\2\2\u0872\u0911\3\2\2\2\u0873\u0874")
        buf.write("\5D#\2\u0874\u0875\7R\2\2\u0875\u0876\5\u018e\u00c8\2")
        buf.write("\u0876\u0878\7S\2\2\u0877\u0879\5\u0194\u00cb\2\u0878")
        buf.write("\u0877\3\2\2\2\u0878\u0879\3\2\2\2\u0879\u0911\3\2\2\2")
        buf.write("\u087a\u087b\5\u01a4\u00d3\2\u087b\u087c\7R\2\2\u087c")
        buf.write("\u087d\5\u018e\u00c8\2\u087d\u087f\7S\2\2\u087e\u0880")
        buf.write("\5\u0194\u00cb\2\u087f\u087e\3\2\2\2\u087f\u0880\3\2\2")
        buf.write("\2\u0880\u0911\3\2\2\2\u0881\u0882\5F$\2\u0882\u0884\7")
        buf.write("N\2\2\u0883\u0885\5\u01b0\u00d9\2\u0884\u0883\3\2\2\2")
        buf.write("\u0884\u0885\3\2\2\2\u0885\u0886\3\2\2\2\u0886\u0888\7")
        buf.write("O\2\2\u0887\u0889\5\u0194\u00cb\2\u0888\u0887\3\2\2\2")
        buf.write("\u0888\u0889\3\2\2\2\u0889\u0911\3\2\2\2\u088a\u088b\5")
        buf.write("@!\2\u088b\u088d\7V\2\2\u088c\u088e\5\62\32\2\u088d\u088c")
        buf.write("\3\2\2\2\u088d\u088e\3\2\2\2\u088e\u088f\3\2\2\2\u088f")
        buf.write("\u0890\5\4\3\2\u0890\u0892\7N\2\2\u0891\u0893\5\u01b0")
        buf.write("\u00d9\2\u0892\u0891\3\2\2\2\u0892\u0893\3\2\2\2\u0893")
        buf.write("\u0894\3\2\2\2\u0894\u0896\7O\2\2\u0895\u0897\5\u0194")
        buf.write("\u00cb\2\u0896\u0895\3\2\2\2\u0896\u0897\3\2\2\2\u0897")
        buf.write("\u0911\3\2\2\2\u0898\u0899\5D#\2\u0899\u089b\7V\2\2\u089a")
        buf.write("\u089c\5\62\32\2\u089b\u089a\3\2\2\2\u089b\u089c\3\2\2")
        buf.write("\2\u089c\u089d\3\2\2\2\u089d\u089e\5\4\3\2\u089e\u08a0")
        buf.write("\7N\2\2\u089f\u08a1\5\u01b0\u00d9\2\u08a0\u089f\3\2\2")
        buf.write("\2\u08a0\u08a1\3\2\2\2\u08a1\u08a2\3\2\2\2\u08a2\u08a4")
        buf.write("\7O\2\2\u08a3\u08a5\5\u0194\u00cb\2\u08a4\u08a3\3\2\2")
        buf.write("\2\u08a4\u08a5\3\2\2\2\u08a5\u0911\3\2\2\2\u08a6\u08a7")
        buf.write("\5\u01a0\u00d1\2\u08a7\u08a9\7V\2\2\u08a8\u08aa\5\62\32")
        buf.write("\2\u08a9\u08a8\3\2\2\2\u08a9\u08aa\3\2\2\2\u08aa\u08ab")
        buf.write("\3\2\2\2\u08ab\u08ac\5\4\3\2\u08ac\u08ae\7N\2\2\u08ad")
        buf.write("\u08af\5\u01b0\u00d9\2\u08ae\u08ad\3\2\2\2\u08ae\u08af")
        buf.write("\3\2\2\2\u08af\u08b0\3\2\2\2\u08b0\u08b2\7O\2\2\u08b1")
        buf.write("\u08b3\5\u0194\u00cb\2\u08b2\u08b1\3\2\2\2\u08b2\u08b3")
        buf.write("\3\2\2\2\u08b3\u0911\3\2\2\2\u08b4\u08b5\7;\2\2\u08b5")
        buf.write("\u08b7\7V\2\2\u08b6\u08b8\5\62\32\2\u08b7\u08b6\3\2\2")
        buf.write("\2\u08b7\u08b8\3\2\2\2\u08b8\u08b9\3\2\2\2\u08b9\u08ba")
        buf.write("\5\4\3\2\u08ba\u08bc\7N\2\2\u08bb\u08bd\5\u01b0\u00d9")
        buf.write("\2\u08bc\u08bb\3\2\2\2\u08bc\u08bd\3\2\2\2\u08bd\u08be")
        buf.write("\3\2\2\2\u08be\u08c0\7O\2\2\u08bf\u08c1\5\u0194\u00cb")
        buf.write("\2\u08c0\u08bf\3\2\2\2\u08c0\u08c1\3\2\2\2\u08c1\u0911")
        buf.write("\3\2\2\2\u08c2\u08c3\5@!\2\u08c3\u08c4\7V\2\2\u08c4\u08c5")
        buf.write("\7;\2\2\u08c5\u08c7\7V\2\2\u08c6\u08c8\5\62\32\2\u08c7")
        buf.write("\u08c6\3\2\2\2\u08c7\u08c8\3\2\2\2\u08c8\u08c9\3\2\2\2")
        buf.write("\u08c9\u08ca\5\4\3\2\u08ca\u08cc\7N\2\2\u08cb\u08cd\5")
        buf.write("\u01b0\u00d9\2\u08cc\u08cb\3\2\2\2\u08cc\u08cd\3\2\2\2")
        buf.write("\u08cd\u08ce\3\2\2\2\u08ce\u08d0\7O\2\2\u08cf\u08d1\5")
        buf.write("\u0194\u00cb\2\u08d0\u08cf\3\2\2\2\u08d0\u08d1\3\2\2\2")
        buf.write("\u08d1\u0911\3\2\2\2\u08d2\u08d3\5D#\2\u08d3\u08d5\7Y")
        buf.write("\2\2\u08d4\u08d6\5\62\32\2\u08d5\u08d4\3\2\2\2\u08d5\u08d6")
        buf.write("\3\2\2\2\u08d6\u08d7\3\2\2\2\u08d7\u08d9\5\4\3\2\u08d8")
        buf.write("\u08da\5\u0194\u00cb\2\u08d9\u08d8\3\2\2\2\u08d9\u08da")
        buf.write("\3\2\2\2\u08da\u0911\3\2\2\2\u08db\u08dc\5\u01a0\u00d1")
        buf.write("\2\u08dc\u08de\7Y\2\2\u08dd\u08df\5\62\32\2\u08de\u08dd")
        buf.write("\3\2\2\2\u08de\u08df\3\2\2\2\u08df\u08e0\3\2\2\2\u08e0")
        buf.write("\u08e2\5\4\3\2\u08e1\u08e3\5\u0194\u00cb\2\u08e2\u08e1")
        buf.write("\3\2\2\2\u08e2\u08e3\3\2\2\2\u08e3\u0911\3\2\2\2\u08e4")
        buf.write("\u08e5\5\32\16\2\u08e5\u08e7\7Y\2\2\u08e6\u08e8\5\62\32")
        buf.write("\2\u08e7\u08e6\3\2\2\2\u08e7\u08e8\3\2\2\2\u08e8\u08e9")
        buf.write("\3\2\2\2\u08e9\u08eb\5\4\3\2\u08ea\u08ec\5\u0194\u00cb")
        buf.write("\2\u08eb\u08ea\3\2\2\2\u08eb\u08ec\3\2\2\2\u08ec\u0911")
        buf.write("\3\2\2\2\u08ed\u08ee\7;\2\2\u08ee\u08f0\7Y\2\2\u08ef\u08f1")
        buf.write("\5\62\32\2\u08f0\u08ef\3\2\2\2\u08f0\u08f1\3\2\2\2\u08f1")
        buf.write("\u08f2\3\2\2\2\u08f2\u08f4\5\4\3\2\u08f3\u08f5\5\u0194")
        buf.write("\u00cb\2\u08f4\u08f3\3\2\2\2\u08f4\u08f5\3\2\2\2\u08f5")
        buf.write("\u0911\3\2\2\2\u08f6\u08f7\5@!\2\u08f7\u08f8\7V\2\2\u08f8")
        buf.write("\u08f9\7;\2\2\u08f9\u08fb\7Y\2\2\u08fa\u08fc\5\62\32\2")
        buf.write("\u08fb\u08fa\3\2\2\2\u08fb\u08fc\3\2\2\2\u08fc\u08fd\3")
        buf.write("\2\2\2\u08fd\u08ff\5\4\3\2\u08fe\u0900\5\u0194\u00cb\2")
        buf.write("\u08ff\u08fe\3\2\2\2\u08ff\u0900\3\2\2\2\u0900\u0911\3")
        buf.write("\2\2\2\u0901\u0902\5 \21\2\u0902\u0904\7Y\2\2\u0903\u0905")
        buf.write("\5\62\32\2\u0904\u0903\3\2\2\2\u0904\u0905\3\2\2\2\u0905")
        buf.write("\u0906\3\2\2\2\u0906\u0908\7\62\2\2\u0907\u0909\5\u0194")
        buf.write("\u00cb\2\u0908\u0907\3\2\2\2\u0908\u0909\3\2\2\2\u0909")
        buf.write("\u0911\3\2\2\2\u090a\u090b\5&\24\2\u090b\u090c\7Y\2\2")
        buf.write("\u090c\u090e\7\62\2\2\u090d\u090f\5\u0194\u00cb\2\u090e")
        buf.write("\u090d\3\2\2\2\u090e\u090f\3\2\2\2\u090f\u0911\3\2\2\2")
        buf.write("\u0910\u0837\3\2\2\2\u0910\u083b\3\2\2\2\u0910\u083f\3")
        buf.write("\2\2\2\u0910\u0843\3\2\2\2\u0910\u0849\3\2\2\2\u0910\u084f")
        buf.write("\3\2\2\2\u0910\u0853\3\2\2\2\u0910\u0859\3\2\2\2\u0910")
        buf.write("\u085f\3\2\2\2\u0910\u0865\3\2\2\2\u0910\u086b\3\2\2\2")
        buf.write("\u0910\u0873\3\2\2\2\u0910\u087a\3\2\2\2\u0910\u0881\3")
        buf.write("\2\2\2\u0910\u088a\3\2\2\2\u0910\u0898\3\2\2\2\u0910\u08a6")
        buf.write("\3\2\2\2\u0910\u08b4\3\2\2\2\u0910\u08c2\3\2\2\2\u0910")
        buf.write("\u08d2\3\2\2\2\u0910\u08db\3\2\2\2\u0910\u08e4\3\2\2\2")
        buf.write("\u0910\u08ed\3\2\2\2\u0910\u08f6\3\2\2\2\u0910\u0901\3")
        buf.write("\2\2\2\u0910\u090a\3\2\2\2\u0911\u0193\3\2\2\2\u0912\u0913")
        buf.write("\7V\2\2\u0913\u0915\5\u019a\u00ce\2\u0914\u0916\5\u0194")
        buf.write("\u00cb\2\u0915\u0914\3\2\2\2\u0915\u0916\3\2\2\2\u0916")
        buf.write("\u0938\3\2\2\2\u0917\u0918\7V\2\2\u0918\u091a\5\4\3\2")
        buf.write("\u0919\u091b\5\u0194\u00cb\2\u091a\u0919\3\2\2\2\u091a")
        buf.write("\u091b\3\2\2\2\u091b\u0938\3\2\2\2\u091c\u091d\7R\2\2")
        buf.write("\u091d\u091e\5\u018e\u00c8\2\u091e\u0920\7S\2\2\u091f")
        buf.write("\u0921\5\u0194\u00cb\2\u0920\u091f\3\2\2\2\u0920\u0921")
        buf.write("\3\2\2\2\u0921\u0938\3\2\2\2\u0922\u0924\7V\2\2\u0923")
        buf.write("\u0925\5\62\32\2\u0924\u0923\3\2\2\2\u0924\u0925\3\2\2")
        buf.write("\2\u0925\u0926\3\2\2\2\u0926\u0927\5\4\3\2\u0927\u0929")
        buf.write("\7N\2\2\u0928\u092a\5\u01b0\u00d9\2\u0929\u0928\3\2\2")
        buf.write("\2\u0929\u092a\3\2\2\2\u092a\u092b\3\2\2\2\u092b\u092d")
        buf.write("\7O\2\2\u092c\u092e\5\u0194\u00cb\2\u092d\u092c\3\2\2")
        buf.write("\2\u092d\u092e\3\2\2\2\u092e\u0938\3\2\2\2\u092f\u0931")
        buf.write("\7Y\2\2\u0930\u0932\5\62\32\2\u0931\u0930\3\2\2\2\u0931")
        buf.write("\u0932\3\2\2\2\u0932\u0933\3\2\2\2\u0933\u0935\5\4\3\2")
        buf.write("\u0934\u0936\5\u0194\u00cb\2\u0935\u0934\3\2\2\2\u0935")
        buf.write("\u0936\3\2\2\2\u0936\u0938\3\2\2\2\u0937\u0912\3\2\2\2")
        buf.write("\u0937\u0917\3\2\2\2\u0937\u091c\3\2\2\2\u0937\u0922\3")
        buf.write("\2\2\2\u0937\u092f\3\2\2\2\u0938\u0195\3\2\2\2\u0939\u093e")
        buf.write("\5@!\2\u093a\u093b\7R\2\2\u093b\u093d\7S\2\2\u093c\u093a")
        buf.write("\3\2\2\2\u093d\u0940\3\2\2\2\u093e\u093c\3\2\2\2\u093e")
        buf.write("\u093f\3\2\2\2\u093f\u0941\3\2\2\2\u0940\u093e\3\2\2\2")
        buf.write("\u0941\u0942\7V\2\2\u0942\u0943\7\34\2\2\u0943\u095d\3")
        buf.write("\2\2\2\u0944\u0949\5\24\13\2\u0945\u0946\7R\2\2\u0946")
        buf.write("\u0948\7S\2\2\u0947\u0945\3\2\2\2\u0948\u094b\3\2\2\2")
        buf.write("\u0949\u0947\3\2\2\2\u0949\u094a\3\2\2\2\u094a\u094c\3")
        buf.write("\2\2\2\u094b\u0949\3\2\2\2\u094c\u094d\7V\2\2\u094d\u094e")
        buf.write("\7\34\2\2\u094e\u095d\3\2\2\2\u094f\u0954\7\26\2\2\u0950")
        buf.write("\u0951\7R\2\2\u0951\u0953\7S\2\2\u0952\u0950\3\2\2\2\u0953")
        buf.write("\u0956\3\2\2\2\u0954\u0952\3\2\2\2\u0954\u0955\3\2\2\2")
        buf.write("\u0955\u0957\3\2\2\2\u0956\u0954\3\2\2\2\u0957\u0958\7")
        buf.write("V\2\2\u0958\u095d\7\34\2\2\u0959\u095a\7C\2\2\u095a\u095b")
        buf.write("\7V\2\2\u095b\u095d\7\34\2\2\u095c\u0939\3\2\2\2\u095c")
        buf.write("\u0944\3\2\2\2\u095c\u094f\3\2\2\2\u095c\u0959\3\2\2\2")
        buf.write("\u095d\u0197\3\2\2\2\u095e\u0968\5\u019a\u00ce\2\u095f")
        buf.write("\u0960\5D#\2\u0960\u0961\7V\2\2\u0961\u0962\5\u019a\u00ce")
        buf.write("\2\u0962\u0968\3\2\2\2\u0963\u0964\5\u0190\u00c9\2\u0964")
        buf.write("\u0965\7V\2\2\u0965\u0966\5\u019a\u00ce\2\u0966\u0968")
        buf.write("\3\2\2\2\u0967\u095e\3\2\2\2\u0967\u095f\3\2\2\2\u0967")
        buf.write("\u0963\3\2\2\2\u0968\u0199\3\2\2\2\u0969\u096b\7\62\2")
        buf.write("\2\u096a\u096c\5\62\32\2\u096b\u096a\3\2\2\2\u096b\u096c")
        buf.write("\3\2\2\2\u096c\u096d\3\2\2\2\u096d\u096e\5\u019c\u00cf")
        buf.write("\2\u096e\u0970\7N\2\2\u096f\u0971\5\u01b0\u00d9\2\u0970")
        buf.write("\u096f\3\2\2\2\u0970\u0971\3\2\2\2\u0971\u0972\3\2\2\2")
        buf.write("\u0972\u0974\7O\2\2\u0973\u0975\5x=\2\u0974\u0973\3\2")
        buf.write("\2\2\u0974\u0975\3\2\2\2\u0975\u019b\3\2\2\2\u0976\u0978")
        buf.write("\5\u0108\u0085\2\u0977\u0976\3\2\2\2\u0978\u097b\3\2\2")
        buf.write("\2\u0979\u0977\3\2\2\2\u0979\u097a\3\2\2\2\u097a\u097c")
        buf.write("\3\2\2\2\u097b\u0979\3\2\2\2\u097c\u0987\5\4\3\2\u097d")
        buf.write("\u0981\7V\2\2\u097e\u0980\5\u0108\u0085\2\u097f\u097e")
        buf.write("\3\2\2\2\u0980\u0983\3\2\2\2\u0981\u097f\3\2\2\2\u0981")
        buf.write("\u0982\3\2\2\2\u0982\u0984\3\2\2\2\u0983\u0981\3\2\2\2")
        buf.write("\u0984\u0986\5\4\3\2\u0985\u097d\3\2\2\2\u0986\u0989\3")
        buf.write("\2\2\2\u0987\u0985\3\2\2\2\u0987\u0988\3\2\2\2\u0988\u098b")
        buf.write("\3\2\2\2\u0989\u0987\3\2\2\2\u098a\u098c\5\u019e\u00d0")
        buf.write("\2\u098b\u098a\3\2\2\2\u098b\u098c\3\2\2\2\u098c\u019d")
        buf.write("\3\2\2\2\u098d\u0990\5\62\32\2\u098e\u0990\7\6\2\2\u098f")
        buf.write("\u098d\3\2\2\2\u098f\u098e\3\2\2\2\u0990\u019f\3\2\2\2")
        buf.write("\u0991\u0994\5\u01a2\u00d2\2\u0992\u0994\5\u01a4\u00d3")
        buf.write("\2\u0993\u0991\3\2\2\2\u0993\u0992\3\2\2\2\u0994\u01a1")
        buf.write("\3\2\2\2\u0995\u0996\7\62\2\2\u0996\u0997\5\22\n\2\u0997")
        buf.write("\u0999\5\u01a6\u00d4\2\u0998\u099a\5(\25\2\u0999\u0998")
        buf.write("\3\2\2\2\u0999\u099a\3\2\2\2\u099a\u09a2\3\2\2\2\u099b")
        buf.write("\u099c\7\62\2\2\u099c\u099d\5 \21\2\u099d\u099f\5\u01a6")
        buf.write("\u00d4\2\u099e\u09a0\5(\25\2\u099f\u099e\3\2\2\2\u099f")
        buf.write("\u09a0\3\2\2\2\u09a0\u09a2\3\2\2\2\u09a1\u0995\3\2\2\2")
        buf.write("\u09a1\u099b\3\2\2\2\u09a2\u01a3\3\2\2\2\u09a3\u09a4\7")
        buf.write("\62\2\2\u09a4\u09a5\5\22\n\2\u09a5\u09a6\5(\25\2\u09a6")
        buf.write("\u09a7\5\u011a\u008e\2\u09a7\u09ae\3\2\2\2\u09a8\u09a9")
        buf.write("\7\62\2\2\u09a9\u09aa\5\36\20\2\u09aa\u09ab\5(\25\2\u09ab")
        buf.write("\u09ac\5\u011a\u008e\2\u09ac\u09ae\3\2\2\2\u09ad\u09a3")
        buf.write("\3\2\2\2\u09ad\u09a8\3\2\2\2\u09ae\u01a5\3\2\2\2\u09af")
        buf.write("\u09b3\5\u01a8\u00d5\2\u09b0\u09b2\5\u01a8\u00d5\2\u09b1")
        buf.write("\u09b0\3\2\2\2\u09b2\u09b5\3\2\2\2\u09b3\u09b1\3\2\2\2")
        buf.write("\u09b3\u09b4\3\2\2\2\u09b4\u01a7\3\2\2\2\u09b5\u09b3\3")
        buf.write("\2\2\2\u09b6\u09b8\5\u0108\u0085\2\u09b7\u09b6\3\2\2\2")
        buf.write("\u09b8\u09bb\3\2\2\2\u09b9\u09b7\3\2\2\2\u09b9\u09ba\3")
        buf.write("\2\2\2\u09ba\u09bc\3\2\2\2\u09bb\u09b9\3\2\2\2\u09bc\u09bd")
        buf.write("\7R\2\2\u09bd\u09be\5\u018e\u00c8\2\u09be\u09bf\7S\2\2")
        buf.write("\u09bf\u01a9\3\2\2\2\u09c0\u09c1\5D#\2\u09c1\u09c2\7R")
        buf.write("\2\2\u09c2\u09c3\5\u018e\u00c8\2\u09c3\u09c4\7S\2\2\u09c4")
        buf.write("\u09d0\3\2\2\2\u09c5\u09c6\5\u0192\u00ca\2\u09c6\u09c7")
        buf.write("\7R\2\2\u09c7\u09c8\5\u018e\u00c8\2\u09c8\u09c9\7S\2\2")
        buf.write("\u09c9\u09d0\3\2\2\2\u09ca\u09cb\5\u01a4\u00d3\2\u09cb")
        buf.write("\u09cc\7R\2\2\u09cc\u09cd\5\u018e\u00c8\2\u09cd\u09ce")
        buf.write("\7S\2\2\u09ce\u09d0\3\2\2\2\u09cf\u09c0\3\2\2\2\u09cf")
        buf.write("\u09c5\3\2\2\2\u09cf\u09ca\3\2\2\2\u09d0\u01ab\3\2\2\2")
        buf.write("\u09d1\u09d2\5\u0190\u00c9\2\u09d2\u09d3\7V\2\2\u09d3")
        buf.write("\u09d4\5\4\3\2\u09d4\u09df\3\2\2\2\u09d5\u09d6\7;\2\2")
        buf.write("\u09d6\u09d7\7V\2\2\u09d7\u09df\5\4\3\2\u09d8\u09d9\5")
        buf.write("@!\2\u09d9\u09da\7V\2\2\u09da\u09db\7;\2\2\u09db\u09dc")
        buf.write("\7V\2\2\u09dc\u09dd\5\4\3\2\u09dd\u09df\3\2\2\2\u09de")
        buf.write("\u09d1\3\2\2\2\u09de\u09d5\3\2\2\2\u09de\u09d8\3\2\2\2")
        buf.write("\u09df\u01ad\3\2\2\2\u09e0\u09e1\5F$\2\u09e1\u09e3\7N")
        buf.write("\2\2\u09e2\u09e4\5\u01b0\u00d9\2\u09e3\u09e2\3\2\2\2\u09e3")
        buf.write("\u09e4\3\2\2\2\u09e4\u09e5\3\2\2\2\u09e5\u09e6\7O\2\2")
        buf.write("\u09e6\u0a26\3\2\2\2\u09e7\u09e8\5@!\2\u09e8\u09ea\7V")
        buf.write("\2\2\u09e9\u09eb\5\62\32\2\u09ea\u09e9\3\2\2\2\u09ea\u09eb")
        buf.write("\3\2\2\2\u09eb\u09ec\3\2\2\2\u09ec\u09ed\5\4\3\2\u09ed")
        buf.write("\u09ef\7N\2\2\u09ee\u09f0\5\u01b0\u00d9\2\u09ef\u09ee")
        buf.write("\3\2\2\2\u09ef\u09f0\3\2\2\2\u09f0\u09f1\3\2\2\2\u09f1")
        buf.write("\u09f2\7O\2\2\u09f2\u0a26\3\2\2\2\u09f3\u09f4\5D#\2\u09f4")
        buf.write("\u09f6\7V\2\2\u09f5\u09f7\5\62\32\2\u09f6\u09f5\3\2\2")
        buf.write("\2\u09f6\u09f7\3\2\2\2\u09f7\u09f8\3\2\2\2\u09f8\u09f9")
        buf.write("\5\4\3\2\u09f9\u09fb\7N\2\2\u09fa\u09fc\5\u01b0\u00d9")
        buf.write("\2\u09fb\u09fa\3\2\2\2\u09fb\u09fc\3\2\2\2\u09fc\u09fd")
        buf.write("\3\2\2\2\u09fd\u09fe\7O\2\2\u09fe\u0a26\3\2\2\2\u09ff")
        buf.write("\u0a00\5\u0190\u00c9\2\u0a00\u0a02\7V\2\2\u0a01\u0a03")
        buf.write("\5\62\32\2\u0a02\u0a01\3\2\2\2\u0a02\u0a03\3\2\2\2\u0a03")
        buf.write("\u0a04\3\2\2\2\u0a04\u0a05\5\4\3\2\u0a05\u0a07\7N\2\2")
        buf.write("\u0a06\u0a08\5\u01b0\u00d9\2\u0a07\u0a06\3\2\2\2\u0a07")
        buf.write("\u0a08\3\2\2\2\u0a08\u0a09\3\2\2\2\u0a09\u0a0a\7O\2\2")
        buf.write("\u0a0a\u0a26\3\2\2\2\u0a0b\u0a0c\7;\2\2\u0a0c\u0a0e\7")
        buf.write("V\2\2\u0a0d\u0a0f\5\62\32\2\u0a0e\u0a0d\3\2\2\2\u0a0e")
        buf.write("\u0a0f\3\2\2\2\u0a0f\u0a10\3\2\2\2\u0a10\u0a11\5\4\3\2")
        buf.write("\u0a11\u0a13\7N\2\2\u0a12\u0a14\5\u01b0\u00d9\2\u0a13")
        buf.write("\u0a12\3\2\2\2\u0a13\u0a14\3\2\2\2\u0a14\u0a15\3\2\2\2")
        buf.write("\u0a15\u0a16\7O\2\2\u0a16\u0a26\3\2\2\2\u0a17\u0a18\5")
        buf.write("@!\2\u0a18\u0a19\7V\2\2\u0a19\u0a1a\7;\2\2\u0a1a\u0a1c")
        buf.write("\7V\2\2\u0a1b\u0a1d\5\62\32\2\u0a1c\u0a1b\3\2\2\2\u0a1c")
        buf.write("\u0a1d\3\2\2\2\u0a1d\u0a1e\3\2\2\2\u0a1e\u0a1f\5\4\3\2")
        buf.write("\u0a1f\u0a21\7N\2\2\u0a20\u0a22\5\u01b0\u00d9\2\u0a21")
        buf.write("\u0a20\3\2\2\2\u0a21\u0a22\3\2\2\2\u0a22\u0a23\3\2\2\2")
        buf.write("\u0a23\u0a24\7O\2\2\u0a24\u0a26\3\2\2\2\u0a25\u09e0\3")
        buf.write("\2\2\2\u0a25\u09e7\3\2\2\2\u0a25\u09f3\3\2\2\2\u0a25\u09ff")
        buf.write("\3\2\2\2\u0a25\u0a0b\3\2\2\2\u0a25\u0a17\3\2\2\2\u0a26")
        buf.write("\u01af\3\2\2\2\u0a27\u0a2c\5\u018e\u00c8\2\u0a28\u0a29")
        buf.write("\7U\2\2\u0a29\u0a2b\5\u018e\u00c8\2\u0a2a\u0a28\3\2\2")
        buf.write("\2\u0a2b\u0a2e\3\2\2\2\u0a2c\u0a2a\3\2\2\2\u0a2c\u0a2d")
        buf.write("\3\2\2\2\u0a2d\u01b1\3\2\2\2\u0a2e\u0a2c\3\2\2\2\u0a2f")
        buf.write("\u0a30\5D#\2\u0a30\u0a32\7Y\2\2\u0a31\u0a33\5\62\32\2")
        buf.write("\u0a32\u0a31\3\2\2\2\u0a32\u0a33\3\2\2\2\u0a33\u0a34\3")
        buf.write("\2\2\2\u0a34\u0a35\5\4\3\2\u0a35\u0a5f\3\2\2\2\u0a36\u0a37")
        buf.write("\5\u0190\u00c9\2\u0a37\u0a39\7Y\2\2\u0a38\u0a3a\5\62\32")
        buf.write("\2\u0a39\u0a38\3\2\2\2\u0a39\u0a3a\3\2\2\2\u0a3a\u0a3b")
        buf.write("\3\2\2\2\u0a3b\u0a3c\5\4\3\2\u0a3c\u0a5f\3\2\2\2\u0a3d")
        buf.write("\u0a3e\5\32\16\2\u0a3e\u0a40\7Y\2\2\u0a3f\u0a41\5\62\32")
        buf.write("\2\u0a40\u0a3f\3\2\2\2\u0a40\u0a41\3\2\2\2\u0a41\u0a42")
        buf.write("\3\2\2\2\u0a42\u0a43\5\4\3\2\u0a43\u0a5f\3\2\2\2\u0a44")
        buf.write("\u0a45\7;\2\2\u0a45\u0a47\7Y\2\2\u0a46\u0a48\5\62\32\2")
        buf.write("\u0a47\u0a46\3\2\2\2\u0a47\u0a48\3\2\2\2\u0a48\u0a49\3")
        buf.write("\2\2\2\u0a49\u0a5f\5\4\3\2\u0a4a\u0a4b\5@!\2\u0a4b\u0a4c")
        buf.write("\7V\2\2\u0a4c\u0a4d\7;\2\2\u0a4d\u0a4f\7Y\2\2\u0a4e\u0a50")
        buf.write("\5\62\32\2\u0a4f\u0a4e\3\2\2\2\u0a4f\u0a50\3\2\2\2\u0a50")
        buf.write("\u0a51\3\2\2\2\u0a51\u0a52\5\4\3\2\u0a52\u0a5f\3\2\2\2")
        buf.write("\u0a53\u0a54\5 \21\2\u0a54\u0a56\7Y\2\2\u0a55\u0a57\5")
        buf.write("\62\32\2\u0a56\u0a55\3\2\2\2\u0a56\u0a57\3\2\2\2\u0a57")
        buf.write("\u0a58\3\2\2\2\u0a58\u0a59\7\62\2\2\u0a59\u0a5f\3\2\2")
        buf.write("\2\u0a5a\u0a5b\5&\24\2\u0a5b\u0a5c\7Y\2\2\u0a5c\u0a5d")
        buf.write("\7\62\2\2\u0a5d\u0a5f\3\2\2\2\u0a5e\u0a2f\3\2\2\2\u0a5e")
        buf.write("\u0a36\3\2\2\2\u0a5e\u0a3d\3\2\2\2\u0a5e\u0a44\3\2\2\2")
        buf.write("\u0a5e\u0a4a\3\2\2\2\u0a5e\u0a53\3\2\2\2\u0a5e\u0a5a\3")
        buf.write("\2\2\2\u0a5f\u01b3\3\2\2\2\u0a60\u0a62\5\u0190\u00c9\2")
        buf.write("\u0a61\u0a63\5\u01b6\u00dc\2\u0a62\u0a61\3\2\2\2\u0a62")
        buf.write("\u0a63\3\2\2\2\u0a63\u0a69\3\2\2\2\u0a64\u0a66\5D#\2\u0a65")
        buf.write("\u0a67\5\u01b6\u00dc\2\u0a66\u0a65\3\2\2\2\u0a66\u0a67")
        buf.write("\3\2\2\2\u0a67\u0a69\3\2\2\2\u0a68\u0a60\3\2\2\2\u0a68")
        buf.write("\u0a64\3\2\2\2\u0a69\u01b5\3\2\2\2\u0a6a\u0a6c\7h\2\2")
        buf.write("\u0a6b\u0a6d\5\u01b6\u00dc\2\u0a6c\u0a6b\3\2\2\2\u0a6c")
        buf.write("\u0a6d\3\2\2\2\u0a6d\u0a73\3\2\2\2\u0a6e\u0a70\7i\2\2")
        buf.write("\u0a6f\u0a71\5\u01b6\u00dc\2\u0a70\u0a6f\3\2\2\2\u0a70")
        buf.write("\u0a71\3\2\2\2\u0a71\u0a73\3\2\2\2\u0a72\u0a6a\3\2\2\2")
        buf.write("\u0a72\u0a6e\3\2\2\2\u0a73\u01b7\3\2\2\2\u0a74\u0a75\5")
        buf.write("\u01b4\u00db\2\u0a75\u0a76\7h\2\2\u0a76\u01b9\3\2\2\2")
        buf.write("\u0a77\u0a78\5\u01b4\u00db\2\u0a78\u0a79\7i\2\2\u0a79")
        buf.write("\u01bb\3\2\2\2\u0a7a\u0a82\5\u01be\u00e0\2\u0a7b\u0a82")
        buf.write("\5\u01c0\u00e1\2\u0a7c\u0a7d\7j\2\2\u0a7d\u0a82\5\u01bc")
        buf.write("\u00df\2\u0a7e\u0a7f\7k\2\2\u0a7f\u0a82\5\u01bc\u00df")
        buf.write("\2\u0a80\u0a82\5\u01c2\u00e2\2\u0a81\u0a7a\3\2\2\2\u0a81")
        buf.write("\u0a7b\3\2\2\2\u0a81\u0a7c\3\2\2\2\u0a81\u0a7e\3\2\2\2")
        buf.write("\u0a81\u0a80\3\2\2\2\u0a82\u01bd\3\2\2\2\u0a83\u0a84\7")
        buf.write("h\2\2\u0a84\u0a85\5\u01bc\u00df\2\u0a85\u01bf\3\2\2\2")
        buf.write("\u0a86\u0a87\7i\2\2\u0a87\u0a88\5\u01bc\u00df\2\u0a88")
        buf.write("\u01c1\3\2\2\2\u0a89\u0a91\5\u01b4\u00db\2\u0a8a\u0a8b")
        buf.write("\7^\2\2\u0a8b\u0a91\5\u01bc\u00df\2\u0a8c\u0a8d\7]\2\2")
        buf.write("\u0a8d\u0a91\5\u01bc\u00df\2\u0a8e\u0a91\5\u01c4\u00e3")
        buf.write("\2\u0a8f\u0a91\5\u01f0\u00f9\2\u0a90\u0a89\3\2\2\2\u0a90")
        buf.write("\u0a8a\3\2\2\2\u0a90\u0a8c\3\2\2\2\u0a90\u0a8e\3\2\2\2")
        buf.write("\u0a90\u0a8f\3\2\2\2\u0a91\u01c3\3\2\2\2\u0a92\u0a93\7")
        buf.write("N\2\2\u0a93\u0a94\5\22\n\2\u0a94\u0a95\7O\2\2\u0a95\u0a96")
        buf.write("\5\u01bc\u00df\2\u0a96\u0aae\3\2\2\2\u0a97\u0a98\7N\2")
        buf.write("\2\u0a98\u0a9c\5\32\16\2\u0a99\u0a9b\5\60\31\2\u0a9a\u0a99")
        buf.write("\3\2\2\2\u0a9b\u0a9e\3\2\2\2\u0a9c\u0a9a\3\2\2\2\u0a9c")
        buf.write("\u0a9d\3\2\2\2\u0a9d\u0a9f\3\2\2\2\u0a9e\u0a9c\3\2\2\2")
        buf.write("\u0a9f\u0aa0\7O\2\2\u0aa0\u0aa1\5\u01c2\u00e2\2\u0aa1")
        buf.write("\u0aae\3\2\2\2\u0aa2\u0aa3\7N\2\2\u0aa3\u0aa7\5\32\16")
        buf.write("\2\u0aa4\u0aa6\5\60\31\2\u0aa5\u0aa4\3\2\2\2\u0aa6\u0aa9")
        buf.write("\3\2\2\2\u0aa7\u0aa5\3\2\2\2\u0aa7\u0aa8\3\2\2\2\u0aa8")
        buf.write("\u0aaa\3\2\2\2\u0aa9\u0aa7\3\2\2\2\u0aaa\u0aab\7O\2\2")
        buf.write("\u0aab\u0aac\5\u01e4\u00f3\2\u0aac\u0aae\3\2\2\2\u0aad")
        buf.write("\u0a92\3\2\2\2\u0aad\u0a97\3\2\2\2\u0aad\u0aa2\3\2\2\2")
        buf.write("\u0aae\u01c5\3\2\2\2\u0aaf\u0ab0\b\u00e4\1\2\u0ab0\u0ab1")
        buf.write("\5\u01bc\u00df\2\u0ab1\u0abd\3\2\2\2\u0ab2\u0ab3\f\5\2")
        buf.write("\2\u0ab3\u0ab4\7l\2\2\u0ab4\u0abc\5\u01bc\u00df\2\u0ab5")
        buf.write("\u0ab6\f\4\2\2\u0ab6\u0ab7\7m\2\2\u0ab7\u0abc\5\u01bc")
        buf.write("\u00df\2\u0ab8\u0ab9\f\3\2\2\u0ab9\u0aba\7q\2\2\u0aba")
        buf.write("\u0abc\5\u01bc\u00df\2\u0abb\u0ab2\3\2\2\2\u0abb\u0ab5")
        buf.write("\3\2\2\2\u0abb\u0ab8\3\2\2\2\u0abc\u0abf\3\2\2\2\u0abd")
        buf.write("\u0abb\3\2\2\2\u0abd\u0abe\3\2\2\2\u0abe\u01c7\3\2\2\2")
        buf.write("\u0abf\u0abd\3\2\2\2\u0ac0\u0ac1\b\u00e5\1\2\u0ac1\u0ac2")
        buf.write("\5\u01c6\u00e4\2\u0ac2\u0acb\3\2\2\2\u0ac3\u0ac4\f\4\2")
        buf.write("\2\u0ac4\u0ac5\7j\2\2\u0ac5\u0aca\5\u01c6\u00e4\2\u0ac6")
        buf.write("\u0ac7\f\3\2\2\u0ac7\u0ac8\7k\2\2\u0ac8\u0aca\5\u01c6")
        buf.write("\u00e4\2\u0ac9\u0ac3\3\2\2\2\u0ac9\u0ac6\3\2\2\2\u0aca")
        buf.write("\u0acd\3\2\2\2\u0acb\u0ac9\3\2\2\2\u0acb\u0acc\3\2\2\2")
        buf.write("\u0acc\u01c9\3\2\2\2\u0acd\u0acb\3\2\2\2\u0ace\u0acf\b")
        buf.write("\u00e6\1\2\u0acf\u0ad0\5\u01c8\u00e5\2\u0ad0\u0ae0\3\2")
        buf.write("\2\2\u0ad1\u0ad2\f\5\2\2\u0ad2\u0ad3\7\\\2\2\u0ad3\u0ad4")
        buf.write("\7\\\2\2\u0ad4\u0adf\5\u01c8\u00e5\2\u0ad5\u0ad6\f\4\2")
        buf.write("\2\u0ad6\u0ad7\7[\2\2\u0ad7\u0ad8\7[\2\2\u0ad8\u0adf\5")
        buf.write("\u01c8\u00e5\2\u0ad9\u0ada\f\3\2\2\u0ada\u0adb\7[\2\2")
        buf.write("\u0adb\u0adc\7[\2\2\u0adc\u0add\7[\2\2\u0add\u0adf\5\u01c8")
        buf.write("\u00e5\2\u0ade\u0ad1\3\2\2\2\u0ade\u0ad5\3\2\2\2\u0ade")
        buf.write("\u0ad9\3\2\2\2\u0adf\u0ae2\3\2\2\2\u0ae0\u0ade\3\2\2\2")
        buf.write("\u0ae0\u0ae1\3\2\2\2\u0ae1\u01cb\3\2\2\2\u0ae2\u0ae0\3")
        buf.write("\2\2\2\u0ae3\u0ae4\b\u00e7\1\2\u0ae4\u0ae5\5\u01ca\u00e6")
        buf.write("\2\u0ae5\u0afa\3\2\2\2\u0ae6\u0ae7\f\7\2\2\u0ae7\u0ae8")
        buf.write("\7\\\2\2\u0ae8\u0af9\5\u01ca\u00e6\2\u0ae9\u0aea\f\6\2")
        buf.write("\2\u0aea\u0aeb\7[\2\2\u0aeb\u0af9\5\u01ca\u00e6\2\u0aec")
        buf.write("\u0aed\f\5\2\2\u0aed\u0aee\7c\2\2\u0aee\u0af9\5\u01ca")
        buf.write("\u00e6\2\u0aef\u0af0\f\4\2\2\u0af0\u0af1\7d\2\2\u0af1")
        buf.write("\u0af9\5\u01ca\u00e6\2\u0af2\u0af3\f\3\2\2\u0af3\u0af6")
        buf.write("\7-\2\2\u0af4\u0af7\5\32\16\2\u0af5\u0af7\5\u018a\u00c6")
        buf.write("\2\u0af6\u0af4\3\2\2\2\u0af6\u0af5\3\2\2\2\u0af7\u0af9")
        buf.write("\3\2\2\2\u0af8\u0ae6\3\2\2\2\u0af8\u0ae9\3\2\2\2\u0af8")
        buf.write("\u0aec\3\2\2\2\u0af8\u0aef\3\2\2\2\u0af8\u0af2\3\2\2\2")
        buf.write("\u0af9\u0afc\3\2\2\2\u0afa\u0af8\3\2\2\2\u0afa\u0afb\3")
        buf.write("\2\2\2\u0afb\u01cd\3\2\2\2\u0afc\u0afa\3\2\2\2\u0afd\u0afe")
        buf.write("\b\u00e8\1\2\u0afe\u0aff\5\u01cc\u00e7\2\u0aff\u0b08\3")
        buf.write("\2\2\2\u0b00\u0b01\f\4\2\2\u0b01\u0b02\7b\2\2\u0b02\u0b07")
        buf.write("\5\u01cc\u00e7\2\u0b03\u0b04\f\3\2\2\u0b04\u0b05\7e\2")
        buf.write("\2\u0b05\u0b07\5\u01cc\u00e7\2\u0b06\u0b00\3\2\2\2\u0b06")
        buf.write("\u0b03\3\2\2\2\u0b07\u0b0a\3\2\2\2\u0b08\u0b06\3\2\2\2")
        buf.write("\u0b08\u0b09\3\2\2\2\u0b09\u01cf\3\2\2\2\u0b0a\u0b08\3")
        buf.write("\2\2\2\u0b0b\u0b0c\b\u00e9\1\2\u0b0c\u0b0d\5\u01ce\u00e8")
        buf.write("\2\u0b0d\u0b13\3\2\2\2\u0b0e\u0b0f\f\3\2\2\u0b0f\u0b10")
        buf.write("\7n\2\2\u0b10\u0b12\5\u01ce\u00e8\2\u0b11\u0b0e\3\2\2")
        buf.write("\2\u0b12\u0b15\3\2\2\2\u0b13\u0b11\3\2\2\2\u0b13\u0b14")
        buf.write("\3\2\2\2\u0b14\u01d1\3\2\2\2\u0b15\u0b13\3\2\2\2\u0b16")
        buf.write("\u0b17\b\u00ea\1\2\u0b17\u0b18\5\u01d0\u00e9\2\u0b18\u0b1e")
        buf.write("\3\2\2\2\u0b19\u0b1a\f\3\2\2\u0b1a\u0b1b\7p\2\2\u0b1b")
        buf.write("\u0b1d\5\u01d0\u00e9\2\u0b1c\u0b19\3\2\2\2\u0b1d\u0b20")
        buf.write("\3\2\2\2\u0b1e\u0b1c\3\2\2\2\u0b1e\u0b1f\3\2\2\2\u0b1f")
        buf.write("\u01d3\3\2\2\2\u0b20\u0b1e\3\2\2\2\u0b21\u0b22\b\u00eb")
        buf.write("\1\2\u0b22\u0b23\5\u01d2\u00ea\2\u0b23\u0b29\3\2\2\2\u0b24")
        buf.write("\u0b25\f\3\2\2\u0b25\u0b26\7o\2\2\u0b26\u0b28\5\u01d2")
        buf.write("\u00ea\2\u0b27\u0b24\3\2\2\2\u0b28\u0b2b\3\2\2\2\u0b29")
        buf.write("\u0b27\3\2\2\2\u0b29\u0b2a\3\2\2\2\u0b2a\u01d5\3\2\2\2")
        buf.write("\u0b2b\u0b29\3\2\2\2\u0b2c\u0b2d\b\u00ec\1\2\u0b2d\u0b2e")
        buf.write("\5\u01d4\u00eb\2\u0b2e\u0b34\3\2\2\2\u0b2f\u0b30\f\3\2")
        buf.write("\2\u0b30\u0b31\7f\2\2\u0b31\u0b33\5\u01d4\u00eb\2\u0b32")
        buf.write("\u0b2f\3\2\2\2\u0b33\u0b36\3\2\2\2\u0b34\u0b32\3\2\2\2")
        buf.write("\u0b34\u0b35\3\2\2\2\u0b35\u01d7\3\2\2\2\u0b36\u0b34\3")
        buf.write("\2\2\2\u0b37\u0b38\b\u00ed\1\2\u0b38\u0b39\5\u01d6\u00ec")
        buf.write("\2\u0b39\u0b3f\3\2\2\2\u0b3a\u0b3b\f\3\2\2\u0b3b\u0b3c")
        buf.write("\7g\2\2\u0b3c\u0b3e\5\u01d6\u00ec\2\u0b3d\u0b3a\3\2\2")
        buf.write("\2\u0b3e\u0b41\3\2\2\2\u0b3f\u0b3d\3\2\2\2\u0b3f\u0b40")
        buf.write("\3\2\2\2\u0b40\u01d9\3\2\2\2\u0b41\u0b3f\3\2\2\2\u0b42")
        buf.write("\u0b50\5\u01d8\u00ed\2\u0b43\u0b44\5\u01d8\u00ed\2\u0b44")
        buf.write("\u0b45\7_\2\2\u0b45\u0b46\5\u018e\u00c8\2\u0b46\u0b47")
        buf.write("\7`\2\2\u0b47\u0b48\5\u01da\u00ee\2\u0b48\u0b50\3\2\2")
        buf.write("\2\u0b49\u0b4a\5\u01d8\u00ed\2\u0b4a\u0b4b\7_\2\2\u0b4b")
        buf.write("\u0b4c\5\u018e\u00c8\2\u0b4c\u0b4d\7`\2\2\u0b4d\u0b4e")
        buf.write("\5\u01e4\u00f3\2\u0b4e\u0b50\3\2\2\2\u0b4f\u0b42\3\2\2")
        buf.write("\2\u0b4f\u0b43\3\2\2\2\u0b4f\u0b49\3\2\2\2\u0b50\u01db")
        buf.write("\3\2\2\2\u0b51\u0b54\5\u01da\u00ee\2\u0b52\u0b54\5\u01de")
        buf.write("\u00f0\2\u0b53\u0b51\3\2\2\2\u0b53\u0b52\3\2\2\2\u0b54")
        buf.write("\u01dd\3\2\2\2\u0b55\u0b56\5\u01e0\u00f1\2\u0b56\u0b57")
        buf.write("\5\u01e2\u00f2\2\u0b57\u0b58\5\u018e\u00c8\2\u0b58\u01df")
        buf.write("\3\2\2\2\u0b59\u0b5d\5D#\2\u0b5a\u0b5d\5\u01ac\u00d7\2")
        buf.write("\u0b5b\u0b5d\5\u01aa\u00d6\2\u0b5c\u0b59\3\2\2\2\u0b5c")
        buf.write("\u0b5a\3\2\2\2\u0b5c\u0b5b\3\2\2\2\u0b5d\u01e1\3\2\2\2")
        buf.write("\u0b5e\u0b5f\t\n\2\2\u0b5f\u01e3\3\2\2\2\u0b60\u0b61\5")
        buf.write("\u01e6\u00f4\2\u0b61\u0b62\7a\2\2\u0b62\u0b63\5\u01ee")
        buf.write("\u00f8\2\u0b63\u01e5\3\2\2\2\u0b64\u0b66\7N\2\2\u0b65")
        buf.write("\u0b67\5\u01e8\u00f5\2\u0b66\u0b65\3\2\2\2\u0b66\u0b67")
        buf.write("\3\2\2\2\u0b67\u0b68\3\2\2\2\u0b68\u0b6b\7O\2\2\u0b69")
        buf.write("\u0b6b\5\4\3\2\u0b6a\u0b64\3\2\2\2\u0b6a\u0b69\3\2\2\2")
        buf.write("\u0b6b\u01e7\3\2\2\2\u0b6c\u0b71\5\u01ea\u00f6\2\u0b6d")
        buf.write("\u0b6e\7U\2\2\u0b6e\u0b70\5\u01ea\u00f6\2\u0b6f\u0b6d")
        buf.write("\3\2\2\2\u0b70\u0b73\3\2\2\2\u0b71\u0b6f\3\2\2\2\u0b71")
        buf.write("\u0b72\3\2\2\2\u0b72\u0b7d\3\2\2\2\u0b73\u0b71\3\2\2\2")
        buf.write("\u0b74\u0b79\5\4\3\2\u0b75\u0b76\7U\2\2\u0b76\u0b78\5")
        buf.write("\4\3\2\u0b77\u0b75\3\2\2\2\u0b78\u0b7b\3\2\2\2\u0b79\u0b77")
        buf.write("\3\2\2\2\u0b79\u0b7a\3\2\2\2\u0b7a\u0b7d\3\2\2\2\u0b7b")
        buf.write("\u0b79\3\2\2\2\u0b7c\u0b6c\3\2\2\2\u0b7c\u0b74\3\2\2\2")
        buf.write("\u0b7d\u01e9\3\2\2\2\u0b7e\u0b80\5\u00aeX\2\u0b7f\u0b7e")
        buf.write("\3\2\2\2\u0b80\u0b83\3\2\2\2\u0b81\u0b7f\3\2\2\2\u0b81")
        buf.write("\u0b82\3\2\2\2\u0b82\u0b84\3\2\2\2\u0b83\u0b81\3\2\2\2")
        buf.write("\u0b84\u0b85\5\u01ec\u00f7\2\u0b85\u0b86\5\u0086D\2\u0b86")
        buf.write("\u0b89\3\2\2\2\u0b87\u0b89\5\u00acW\2\u0b88\u0b81\3\2")
        buf.write("\2\2\u0b88\u0b87\3\2\2\2\u0b89\u01eb\3\2\2\2\u0b8a\u0b8d")
        buf.write("\5\u008aF\2\u0b8b\u0b8d\7\21\2\2\u0b8c\u0b8a\3\2\2\2\u0b8c")
        buf.write("\u0b8b\3\2\2\2\u0b8d\u01ed\3\2\2\2\u0b8e\u0b91\5\u018e")
        buf.write("\u00c8\2\u0b8f\u0b91\5\u011e\u0090\2\u0b90\u0b8e\3\2\2")
        buf.write("\2\u0b90\u0b8f\3\2\2\2\u0b91\u01ef\3\2\2\2\u0b92\u0b93")
        buf.write("\7<\2\2\u0b93\u0b94\7N\2\2\u0b94\u0b95\5\u018e\u00c8\2")
        buf.write("\u0b95\u0b96\7O\2\2\u0b96\u0b97\5\u0146\u00a4\2\u0b97")
        buf.write("\u01f1\3\2\2\2\u0b98\u0b99\5\u018e\u00c8\2\u0b99\u01f3")
        buf.write("\3\2\2\2\u016c\u01f9\u01fd\u0201\u020e\u0213\u0217\u0220")
        buf.write("\u0226\u022b\u022e\u0233\u0238\u023d\u0240\u0245\u024a")
        buf.write("\u0251\u0256\u025d\u0262\u0264\u026b\u0279\u027e\u0286")
        buf.write("\u028d\u0293\u0298\u02a2\u02a5\u02b3\u02b8\u02bd\u02c2")
        buf.write("\u02c8\u02cd\u02d2\u02d7\u02dc\u02e1\u02ea\u02ee\u02f1")
        buf.write("\u02f6\u02fc\u0302\u030a\u0313\u031e\u033b\u0340\u0344")
        buf.write("\u034c\u0353\u035c\u036a\u036d\u0379\u037c\u038c\u0391")
        buf.write("\u0398\u039d\u03a3\u03a6\u03a9\u03ac\u03ba\u03c5\u03d3")
        buf.write("\u03dc\u03e3\u03ec\u03f3\u03f8\u0407\u040e\u0414\u0418")
        buf.write("\u041c\u0420\u0424\u0429\u0430\u0433\u0437\u043a\u0440")
        buf.write("\u0445\u0448\u044c\u0450\u0456\u045b\u045d\u0466\u046d")
        buf.write("\u047d\u0483\u0486\u048b\u048f\u0496\u0499\u049d\u04a2")
        buf.write("\u04a9\u04b2\u04b8\u04bf\u04c4\u04cb\u04d3\u04dd\u04e2")
        buf.write("\u04e6\u04f0\u04f5\u04fd\u0500\u0507\u050a\u0512\u0515")
        buf.write("\u051a\u051f\u0525\u0529\u052e\u0533\u0538\u053e\u0544")
        buf.write("\u0547\u054a\u0553\u0559\u055f\u0562\u0565\u056d\u0573")
        buf.write("\u0579\u057d\u0583\u058c\u0592\u0599\u059e\u05a5\u05b1")
        buf.write("\u05b8\u05bd\u05c5\u05ca\u05d0\u05d3\u05d6\u05e3\u05ee")
        buf.write("\u05f5\u05ff\u0604\u060f\u0614\u0621\u0626\u0632\u063c")
        buf.write("\u0641\u0649\u064c\u0653\u065b\u0661\u066a\u0674\u0678")
        buf.write("\u067b\u0684\u0692\u0695\u069e\u06a3\u06ab\u06b1\u06b5")
        buf.write("\u06ba\u06c2\u06cd\u06d4\u06e3\u06f9\u0715\u0724\u072d")
        buf.write("\u0735\u0739\u0742\u074b\u0756\u075a\u0774\u0778\u077d")
        buf.write("\u0781\u0785\u078d\u0791\u0795\u079c\u07a5\u07ba\u07c0")
        buf.write("\u07c6\u07df\u07e4\u07ea\u07f6\u0801\u080b\u080e\u0813")
        buf.write("\u081c\u0821\u0825\u0831\u0835\u0839\u083d\u0841\u0847")
        buf.write("\u084d\u0851\u0857\u085d\u0863\u0869\u0871\u0878\u087f")
        buf.write("\u0884\u0888\u088d\u0892\u0896\u089b\u08a0\u08a4\u08a9")
        buf.write("\u08ae\u08b2\u08b7\u08bc\u08c0\u08c7\u08cc\u08d0\u08d5")
        buf.write("\u08d9\u08de\u08e2\u08e7\u08eb\u08f0\u08f4\u08fb\u08ff")
        buf.write("\u0904\u0908\u090e\u0910\u0915\u091a\u0920\u0924\u0929")
        buf.write("\u092d\u0931\u0935\u0937\u093e\u0949\u0954\u095c\u0967")
        buf.write("\u096b\u0970\u0974\u0979\u0981\u0987\u098b\u098f\u0993")
        buf.write("\u0999\u099f\u09a1\u09ad\u09b3\u09b9\u09cf\u09de\u09e3")
        buf.write("\u09ea\u09ef\u09f6\u09fb\u0a02\u0a07\u0a0e\u0a13\u0a1c")
        buf.write("\u0a21\u0a25\u0a2c\u0a32\u0a39\u0a40\u0a47\u0a4f\u0a56")
        buf.write("\u0a5e\u0a62\u0a66\u0a68\u0a6c\u0a70\u0a72\u0a81\u0a90")
        buf.write("\u0a9c\u0aa7\u0aad\u0abb\u0abd\u0ac9\u0acb\u0ade\u0ae0")
        buf.write("\u0af6\u0af8\u0afa\u0b06\u0b08\u0b13\u0b1e\u0b29\u0b34")
        buf.write("\u0b3f\u0b4f\u0b53\u0b5c\u0b66\u0b6a\u0b71\u0b79\u0b7c")
        buf.write("\u0b81\u0b88\u0b8c\u0b90")
        return buf.getvalue()


class Java20Parser ( Parser ):

    grammarFileName = "Java20Parser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'exports'", "'module'", "'non-sealed'", 
                     "'<>'", "'open'", "'opens'", "'permits'", "'provides'", 
                     "'record'", "'requires'", "'sealed'", "'to'", "'transitive'", 
                     "'uses'", "'var'", "'with'", "'yield'", "'abstract'", 
                     "'assert'", "'boolean'", "'break'", "'byte'", "'case'", 
                     "'catch'", "'char'", "'class'", "'const'", "'continue'", 
                     "'default'", "'do'", "'double'", "'else'", "'enum'", 
                     "'extends'", "'final'", "'finally'", "'float'", "'for'", 
                     "'if'", "'goto'", "'implements'", "'import'", "'instanceof'", 
                     "'int'", "'interface'", "'long'", "'native'", "'new'", 
                     "'package'", "'private'", "'protected'", "'public'", 
                     "'return'", "'short'", "'static'", "'strictfp'", "'super'", 
                     "'switch'", "'synchronized'", "'this'", "'throw'", 
                     "'throws'", "'transient'", "'try'", "'void'", "'volatile'", 
                     "'while'", "'_'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'null'", "'('", 
                     "')'", "'{'", "'}'", "'['", "']'", "';'", "','", "'.'", 
                     "'...'", "'@'", "'::'", "'='", "'>'", "'<'", "'!'", 
                     "'~'", "'?'", "':'", "'->'", "'=='", "'<='", "'>='", 
                     "'!='", "'&&'", "'||'", "'++'", "'--'", "'+'", "'-'", 
                     "'*'", "'/'", "'&'", "'|'", "'^'", "'%'", "'+='", "'-='", 
                     "'*='", "'/='", "'&='", "'|='", "'^='", "'%='", "'<<='", 
                     "'>>='", "'>>>='" ]

    symbolicNames = [ "<INVALID>", "EXPORTS", "MODULE", "NONSEALED", "OACA", 
                      "OPEN", "OPENS", "PERMITS", "PROVIDES", "RECORD", 
                      "REQUIRES", "SEALED", "TO", "TRANSITIVE", "USES", 
                      "VAR", "WITH", "YIELD", "ABSTRACT", "ASSERT", "BOOLEAN", 
                      "BREAK", "BYTE", "CASE", "CATCH", "CHAR", "CLASS", 
                      "CONST", "CONTINUE", "DEFAULT", "DO", "DOUBLE", "ELSE", 
                      "ENUM", "EXTENDS", "FINAL", "FINALLY", "FLOAT", "FOR", 
                      "IF", "GOTO", "IMPLEMENTS", "IMPORT", "INSTANCEOF", 
                      "INT", "INTERFACE", "LONG", "NATIVE", "NEW", "PACKAGE", 
                      "PRIVATE", "PROTECTED", "PUBLIC", "RETURN", "SHORT", 
                      "STATIC", "STRICTFP", "SUPER", "SWITCH", "SYNCHRONIZED", 
                      "THIS", "THROW", "THROWS", "TRANSIENT", "TRY", "VOID", 
                      "VOLATILE", "WHILE", "UNDER_SCORE", "IntegerLiteral", 
                      "FloatingPointLiteral", "BooleanLiteral", "CharacterLiteral", 
                      "StringLiteral", "TextBlock", "NullLiteral", "LPAREN", 
                      "RPAREN", "LBRACE", "RBRACE", "LBRACK", "RBRACK", 
                      "SEMI", "COMMA", "DOT", "ELLIPSIS", "AT", "COLONCOLON", 
                      "ASSIGN", "GT", "LT", "BANG", "TILDE", "QUESTION", 
                      "COLON", "ARROW", "EQUAL", "LE", "GE", "NOTEQUAL", 
                      "AND", "OR", "INC", "DEC", "ADD", "SUB", "MUL", "DIV", 
                      "BITAND", "BITOR", "CARET", "MOD", "ADD_ASSIGN", "SUB_ASSIGN", 
                      "MUL_ASSIGN", "DIV_ASSIGN", "AND_ASSIGN", "OR_ASSIGN", 
                      "XOR_ASSIGN", "MOD_ASSIGN", "LSHIFT_ASSIGN", "RSHIFT_ASSIGN", 
                      "URSHIFT_ASSIGN", "Identifier", "WS", "COMMENT", "LINE_COMMENT" ]

    RULE_start_ = 0
    RULE_identifier = 1
    RULE_typeIdentifier = 2
    RULE_unqualifiedMethodIdentifier = 3
    RULE_contextualKeyword = 4
    RULE_contextualKeywordMinusForTypeIdentifier = 5
    RULE_contextualKeywordMinusForUnqualifiedMethodIdentifier = 6
    RULE_literal = 7
    RULE_primitiveType = 8
    RULE_numericType = 9
    RULE_integralType = 10
    RULE_floatingPointType = 11
    RULE_referenceType = 12
    RULE_coit = 13
    RULE_classOrInterfaceType = 14
    RULE_classType = 15
    RULE_interfaceType = 16
    RULE_typeVariable = 17
    RULE_arrayType = 18
    RULE_dims = 19
    RULE_typeParameter = 20
    RULE_typeParameterModifier = 21
    RULE_typeBound = 22
    RULE_additionalBound = 23
    RULE_typeArguments = 24
    RULE_typeArgumentList = 25
    RULE_typeArgument = 26
    RULE_wildcard = 27
    RULE_wildcardBounds = 28
    RULE_moduleName = 29
    RULE_packageName = 30
    RULE_typeName = 31
    RULE_packageOrTypeName = 32
    RULE_expressionName = 33
    RULE_methodName = 34
    RULE_ambiguousName = 35
    RULE_compilationUnit = 36
    RULE_ordinaryCompilationUnit = 37
    RULE_modularCompilationUnit = 38
    RULE_packageDeclaration = 39
    RULE_packageModifier = 40
    RULE_importDeclaration = 41
    RULE_singleTypeImportDeclaration = 42
    RULE_typeImportOnDemandDeclaration = 43
    RULE_singleStaticImportDeclaration = 44
    RULE_staticImportOnDemandDeclaration = 45
    RULE_topLevelClassOrInterfaceDeclaration = 46
    RULE_moduleDeclaration = 47
    RULE_moduleDirective = 48
    RULE_requiresModifier = 49
    RULE_classDeclaration = 50
    RULE_normalClassDeclaration = 51
    RULE_classModifier = 52
    RULE_typeParameters = 53
    RULE_typeParameterList = 54
    RULE_classExtends = 55
    RULE_classImplements = 56
    RULE_interfaceTypeList = 57
    RULE_classPermits = 58
    RULE_classBody = 59
    RULE_classBodyDeclaration = 60
    RULE_classMemberDeclaration = 61
    RULE_fieldDeclaration = 62
    RULE_fieldModifier = 63
    RULE_variableDeclaratorList = 64
    RULE_variableDeclarator = 65
    RULE_variableDeclaratorId = 66
    RULE_variableInitializer = 67
    RULE_unannType = 68
    RULE_unannPrimitiveType = 69
    RULE_unannReferenceType = 70
    RULE_unannClassOrInterfaceType = 71
    RULE_uCOIT = 72
    RULE_unannClassType = 73
    RULE_unannInterfaceType = 74
    RULE_unannTypeVariable = 75
    RULE_unannArrayType = 76
    RULE_methodDeclaration = 77
    RULE_methodModifier = 78
    RULE_methodHeader = 79
    RULE_result = 80
    RULE_methodDeclarator = 81
    RULE_receiverParameter = 82
    RULE_formalParameterList = 83
    RULE_formalParameter = 84
    RULE_variableArityParameter = 85
    RULE_variableModifier = 86
    RULE_throwsT = 87
    RULE_exceptionTypeList = 88
    RULE_exceptionType = 89
    RULE_methodBody = 90
    RULE_instanceInitializer = 91
    RULE_staticInitializer = 92
    RULE_constructorDeclaration = 93
    RULE_constructorModifier = 94
    RULE_constructorDeclarator = 95
    RULE_simpleTypeName = 96
    RULE_constructorBody = 97
    RULE_explicitConstructorInvocation = 98
    RULE_enumDeclaration = 99
    RULE_enumBody = 100
    RULE_enumConstantList = 101
    RULE_enumConstant = 102
    RULE_enumConstantModifier = 103
    RULE_enumBodyDeclarations = 104
    RULE_recordDeclaration = 105
    RULE_recordHeader = 106
    RULE_recordComponentList = 107
    RULE_recordComponent = 108
    RULE_variableArityRecordComponent = 109
    RULE_recordComponentModifier = 110
    RULE_recordBody = 111
    RULE_recordBodyDeclaration = 112
    RULE_compactConstructorDeclaration = 113
    RULE_interfaceDeclaration = 114
    RULE_normalInterfaceDeclaration = 115
    RULE_interfaceModifier = 116
    RULE_interfaceExtends = 117
    RULE_interfacePermits = 118
    RULE_interfaceBody = 119
    RULE_interfaceMemberDeclaration = 120
    RULE_constantDeclaration = 121
    RULE_constantModifier = 122
    RULE_interfaceMethodDeclaration = 123
    RULE_interfaceMethodModifier = 124
    RULE_annotationInterfaceDeclaration = 125
    RULE_annotationInterfaceBody = 126
    RULE_annotationInterfaceMemberDeclaration = 127
    RULE_annotationInterfaceElementDeclaration = 128
    RULE_annotationInterfaceElementModifier = 129
    RULE_defaultValue = 130
    RULE_annotation = 131
    RULE_normalAnnotation = 132
    RULE_elementValuePairList = 133
    RULE_elementValuePair = 134
    RULE_elementValue = 135
    RULE_elementValueArrayInitializer = 136
    RULE_elementValueList = 137
    RULE_markerAnnotation = 138
    RULE_singleElementAnnotation = 139
    RULE_arrayInitializer = 140
    RULE_variableInitializerList = 141
    RULE_block = 142
    RULE_blockStatements = 143
    RULE_blockStatement = 144
    RULE_localClassOrInterfaceDeclaration = 145
    RULE_localVariableDeclaration = 146
    RULE_localVariableType = 147
    RULE_localVariableDeclarationStatement = 148
    RULE_statement = 149
    RULE_statementNoShortIf = 150
    RULE_statementWithoutTrailingSubstatement = 151
    RULE_emptyStatement_ = 152
    RULE_labeledStatement = 153
    RULE_labeledStatementNoShortIf = 154
    RULE_expressionStatement = 155
    RULE_statementExpression = 156
    RULE_ifThenStatement = 157
    RULE_ifThenElseStatement = 158
    RULE_ifThenElseStatementNoShortIf = 159
    RULE_assertStatement = 160
    RULE_switchStatement = 161
    RULE_switchBlock = 162
    RULE_switchRule = 163
    RULE_switchBlockStatementGroup = 164
    RULE_switchLabel = 165
    RULE_caseConstant = 166
    RULE_whileStatement = 167
    RULE_whileStatementNoShortIf = 168
    RULE_doStatement = 169
    RULE_forStatement = 170
    RULE_forStatementNoShortIf = 171
    RULE_basicForStatement = 172
    RULE_basicForStatementNoShortIf = 173
    RULE_forInit = 174
    RULE_forUpdate = 175
    RULE_statementExpressionList = 176
    RULE_enhancedForStatement = 177
    RULE_enhancedForStatementNoShortIf = 178
    RULE_breakStatement = 179
    RULE_continueStatement = 180
    RULE_returnStatement = 181
    RULE_throwStatement = 182
    RULE_synchronizedStatement = 183
    RULE_tryStatement = 184
    RULE_catches = 185
    RULE_catchClause = 186
    RULE_catchFormalParameter = 187
    RULE_catchType = 188
    RULE_finallyBlock = 189
    RULE_tryWithResourcesStatement = 190
    RULE_resourceSpecification = 191
    RULE_resourceList = 192
    RULE_resource = 193
    RULE_variableAccess = 194
    RULE_yieldStatement = 195
    RULE_pattern = 196
    RULE_typePattern = 197
    RULE_expression = 198
    RULE_primary = 199
    RULE_primaryNoNewArray = 200
    RULE_pNNA = 201
    RULE_classLiteral = 202
    RULE_classInstanceCreationExpression = 203
    RULE_unqualifiedClassInstanceCreationExpression = 204
    RULE_classOrInterfaceTypeToInstantiate = 205
    RULE_typeArgumentsOrDiamond = 206
    RULE_arrayCreationExpression = 207
    RULE_arrayCreationExpressionWithoutInitializer = 208
    RULE_arrayCreationExpressionWithInitializer = 209
    RULE_dimExprs = 210
    RULE_dimExpr = 211
    RULE_arrayAccess = 212
    RULE_fieldAccess = 213
    RULE_methodInvocation = 214
    RULE_argumentList = 215
    RULE_methodReference = 216
    RULE_postfixExpression = 217
    RULE_pfE = 218
    RULE_postIncrementExpression = 219
    RULE_postDecrementExpression = 220
    RULE_unaryExpression = 221
    RULE_preIncrementExpression = 222
    RULE_preDecrementExpression = 223
    RULE_unaryExpressionNotPlusMinus = 224
    RULE_castExpression = 225
    RULE_multiplicativeExpression = 226
    RULE_additiveExpression = 227
    RULE_shiftExpression = 228
    RULE_relationalExpression = 229
    RULE_equalityExpression = 230
    RULE_andExpression = 231
    RULE_exclusiveOrExpression = 232
    RULE_inclusiveOrExpression = 233
    RULE_conditionalAndExpression = 234
    RULE_conditionalOrExpression = 235
    RULE_conditionalExpression = 236
    RULE_assignmentExpression = 237
    RULE_assignment = 238
    RULE_leftHandSide = 239
    RULE_assignmentOperator = 240
    RULE_lambdaExpression = 241
    RULE_lambdaParameters = 242
    RULE_lambdaParameterList = 243
    RULE_lambdaParameter = 244
    RULE_lambdaParameterType = 245
    RULE_lambdaBody = 246
    RULE_switchExpression = 247
    RULE_constantExpression = 248

    ruleNames =  [ "start_", "identifier", "typeIdentifier", "unqualifiedMethodIdentifier", 
                   "contextualKeyword", "contextualKeywordMinusForTypeIdentifier", 
                   "contextualKeywordMinusForUnqualifiedMethodIdentifier", 
                   "literal", "primitiveType", "numericType", "integralType", 
                   "floatingPointType", "referenceType", "coit", "classOrInterfaceType", 
                   "classType", "interfaceType", "typeVariable", "arrayType", 
                   "dims", "typeParameter", "typeParameterModifier", "typeBound", 
                   "additionalBound", "typeArguments", "typeArgumentList", 
                   "typeArgument", "wildcard", "wildcardBounds", "moduleName", 
                   "packageName", "typeName", "packageOrTypeName", "expressionName", 
                   "methodName", "ambiguousName", "compilationUnit", "ordinaryCompilationUnit", 
                   "modularCompilationUnit", "packageDeclaration", "packageModifier", 
                   "importDeclaration", "singleTypeImportDeclaration", "typeImportOnDemandDeclaration", 
                   "singleStaticImportDeclaration", "staticImportOnDemandDeclaration", 
                   "topLevelClassOrInterfaceDeclaration", "moduleDeclaration", 
                   "moduleDirective", "requiresModifier", "classDeclaration", 
                   "normalClassDeclaration", "classModifier", "typeParameters", 
                   "typeParameterList", "classExtends", "classImplements", 
                   "interfaceTypeList", "classPermits", "classBody", "classBodyDeclaration", 
                   "classMemberDeclaration", "fieldDeclaration", "fieldModifier", 
                   "variableDeclaratorList", "variableDeclarator", "variableDeclaratorId", 
                   "variableInitializer", "unannType", "unannPrimitiveType", 
                   "unannReferenceType", "unannClassOrInterfaceType", "uCOIT", 
                   "unannClassType", "unannInterfaceType", "unannTypeVariable", 
                   "unannArrayType", "methodDeclaration", "methodModifier", 
                   "methodHeader", "result", "methodDeclarator", "receiverParameter", 
                   "formalParameterList", "formalParameter", "variableArityParameter", 
                   "variableModifier", "throwsT", "exceptionTypeList", "exceptionType", 
                   "methodBody", "instanceInitializer", "staticInitializer", 
                   "constructorDeclaration", "constructorModifier", "constructorDeclarator", 
                   "simpleTypeName", "constructorBody", "explicitConstructorInvocation", 
                   "enumDeclaration", "enumBody", "enumConstantList", "enumConstant", 
                   "enumConstantModifier", "enumBodyDeclarations", "recordDeclaration", 
                   "recordHeader", "recordComponentList", "recordComponent", 
                   "variableArityRecordComponent", "recordComponentModifier", 
                   "recordBody", "recordBodyDeclaration", "compactConstructorDeclaration", 
                   "interfaceDeclaration", "normalInterfaceDeclaration", 
                   "interfaceModifier", "interfaceExtends", "interfacePermits", 
                   "interfaceBody", "interfaceMemberDeclaration", "constantDeclaration", 
                   "constantModifier", "interfaceMethodDeclaration", "interfaceMethodModifier", 
                   "annotationInterfaceDeclaration", "annotationInterfaceBody", 
                   "annotationInterfaceMemberDeclaration", "annotationInterfaceElementDeclaration", 
                   "annotationInterfaceElementModifier", "defaultValue", 
                   "annotation", "normalAnnotation", "elementValuePairList", 
                   "elementValuePair", "elementValue", "elementValueArrayInitializer", 
                   "elementValueList", "markerAnnotation", "singleElementAnnotation", 
                   "arrayInitializer", "variableInitializerList", "block", 
                   "blockStatements", "blockStatement", "localClassOrInterfaceDeclaration", 
                   "localVariableDeclaration", "localVariableType", "localVariableDeclarationStatement", 
                   "statement", "statementNoShortIf", "statementWithoutTrailingSubstatement", 
                   "emptyStatement_", "labeledStatement", "labeledStatementNoShortIf", 
                   "expressionStatement", "statementExpression", "ifThenStatement", 
                   "ifThenElseStatement", "ifThenElseStatementNoShortIf", 
                   "assertStatement", "switchStatement", "switchBlock", 
                   "switchRule", "switchBlockStatementGroup", "switchLabel", 
                   "caseConstant", "whileStatement", "whileStatementNoShortIf", 
                   "doStatement", "forStatement", "forStatementNoShortIf", 
                   "basicForStatement", "basicForStatementNoShortIf", "forInit", 
                   "forUpdate", "statementExpressionList", "enhancedForStatement", 
                   "enhancedForStatementNoShortIf", "breakStatement", "continueStatement", 
                   "returnStatement", "throwStatement", "synchronizedStatement", 
                   "tryStatement", "catches", "catchClause", "catchFormalParameter", 
                   "catchType", "finallyBlock", "tryWithResourcesStatement", 
                   "resourceSpecification", "resourceList", "resource", 
                   "variableAccess", "yieldStatement", "pattern", "typePattern", 
                   "expression", "primary", "primaryNoNewArray", "pNNA", 
                   "classLiteral", "classInstanceCreationExpression", "unqualifiedClassInstanceCreationExpression", 
                   "classOrInterfaceTypeToInstantiate", "typeArgumentsOrDiamond", 
                   "arrayCreationExpression", "arrayCreationExpressionWithoutInitializer", 
                   "arrayCreationExpressionWithInitializer", "dimExprs", 
                   "dimExpr", "arrayAccess", "fieldAccess", "methodInvocation", 
                   "argumentList", "methodReference", "postfixExpression", 
                   "pfE", "postIncrementExpression", "postDecrementExpression", 
                   "unaryExpression", "preIncrementExpression", "preDecrementExpression", 
                   "unaryExpressionNotPlusMinus", "castExpression", "multiplicativeExpression", 
                   "additiveExpression", "shiftExpression", "relationalExpression", 
                   "equalityExpression", "andExpression", "exclusiveOrExpression", 
                   "inclusiveOrExpression", "conditionalAndExpression", 
                   "conditionalOrExpression", "conditionalExpression", "assignmentExpression", 
                   "assignment", "leftHandSide", "assignmentOperator", "lambdaExpression", 
                   "lambdaParameters", "lambdaParameterList", "lambdaParameter", 
                   "lambdaParameterType", "lambdaBody", "switchExpression", 
                   "constantExpression" ]

    EOF = Token.EOF
    EXPORTS=1
    MODULE=2
    NONSEALED=3
    OACA=4
    OPEN=5
    OPENS=6
    PERMITS=7
    PROVIDES=8
    RECORD=9
    REQUIRES=10
    SEALED=11
    TO=12
    TRANSITIVE=13
    USES=14
    VAR=15
    WITH=16
    YIELD=17
    ABSTRACT=18
    ASSERT=19
    BOOLEAN=20
    BREAK=21
    BYTE=22
    CASE=23
    CATCH=24
    CHAR=25
    CLASS=26
    CONST=27
    CONTINUE=28
    DEFAULT=29
    DO=30
    DOUBLE=31
    ELSE=32
    ENUM=33
    EXTENDS=34
    FINAL=35
    FINALLY=36
    FLOAT=37
    FOR=38
    IF=39
    GOTO=40
    IMPLEMENTS=41
    IMPORT=42
    INSTANCEOF=43
    INT=44
    INTERFACE=45
    LONG=46
    NATIVE=47
    NEW=48
    PACKAGE=49
    PRIVATE=50
    PROTECTED=51
    PUBLIC=52
    RETURN=53
    SHORT=54
    STATIC=55
    STRICTFP=56
    SUPER=57
    SWITCH=58
    SYNCHRONIZED=59
    THIS=60
    THROW=61
    THROWS=62
    TRANSIENT=63
    TRY=64
    VOID=65
    VOLATILE=66
    WHILE=67
    UNDER_SCORE=68
    IntegerLiteral=69
    FloatingPointLiteral=70
    BooleanLiteral=71
    CharacterLiteral=72
    StringLiteral=73
    TextBlock=74
    NullLiteral=75
    LPAREN=76
    RPAREN=77
    LBRACE=78
    RBRACE=79
    LBRACK=80
    RBRACK=81
    SEMI=82
    COMMA=83
    DOT=84
    ELLIPSIS=85
    AT=86
    COLONCOLON=87
    ASSIGN=88
    GT=89
    LT=90
    BANG=91
    TILDE=92
    QUESTION=93
    COLON=94
    ARROW=95
    EQUAL=96
    LE=97
    GE=98
    NOTEQUAL=99
    AND=100
    OR=101
    INC=102
    DEC=103
    ADD=104
    SUB=105
    MUL=106
    DIV=107
    BITAND=108
    BITOR=109
    CARET=110
    MOD=111
    ADD_ASSIGN=112
    SUB_ASSIGN=113
    MUL_ASSIGN=114
    DIV_ASSIGN=115
    AND_ASSIGN=116
    OR_ASSIGN=117
    XOR_ASSIGN=118
    MOD_ASSIGN=119
    LSHIFT_ASSIGN=120
    RSHIFT_ASSIGN=121
    URSHIFT_ASSIGN=122
    Identifier=123
    WS=124
    COMMENT=125
    LINE_COMMENT=126

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Start_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def compilationUnit(self):
            return self.getTypedRuleContext(Java20Parser.CompilationUnitContext,0)


        def EOF(self):
            return self.getToken(Java20Parser.EOF, 0)

        def getRuleIndex(self):
            return Java20Parser.RULE_start_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart_" ):
                listener.enterStart_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart_" ):
                listener.exitStart_(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart_" ):
                return visitor.visitStart_(self)
            else:
                return visitor.visitChildren(self)




    def start_(self):

        localctx = Java20Parser.Start_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 498
            self.compilationUnit()
            self.state = 499
            self.match(Java20Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(Java20Parser.Identifier, 0)

        def contextualKeyword(self):
            return self.getTypedRuleContext(Java20Parser.ContextualKeywordContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_identifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifier" ):
                listener.enterIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifier" ):
                listener.exitIdentifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier" ):
                return visitor.visitIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def identifier(self):

        localctx = Java20Parser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_identifier)
        try:
            self.state = 503
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Java20Parser.Identifier]:
                self.enterOuterAlt(localctx, 1)
                self.state = 501
                self.match(Java20Parser.Identifier)
                pass
            elif token in [Java20Parser.EXPORTS, Java20Parser.MODULE, Java20Parser.NONSEALED, Java20Parser.OPEN, Java20Parser.OPENS, Java20Parser.PERMITS, Java20Parser.PROVIDES, Java20Parser.RECORD, Java20Parser.REQUIRES, Java20Parser.SEALED, Java20Parser.TO, Java20Parser.TRANSITIVE, Java20Parser.USES, Java20Parser.VAR, Java20Parser.WITH, Java20Parser.YIELD]:
                self.enterOuterAlt(localctx, 2)
                self.state = 502
                self.contextualKeyword()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeIdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(Java20Parser.Identifier, 0)

        def contextualKeywordMinusForTypeIdentifier(self):
            return self.getTypedRuleContext(Java20Parser.ContextualKeywordMinusForTypeIdentifierContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_typeIdentifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeIdentifier" ):
                listener.enterTypeIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeIdentifier" ):
                listener.exitTypeIdentifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeIdentifier" ):
                return visitor.visitTypeIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def typeIdentifier(self):

        localctx = Java20Parser.TypeIdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_typeIdentifier)
        try:
            self.state = 507
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Java20Parser.Identifier]:
                self.enterOuterAlt(localctx, 1)
                self.state = 505
                self.match(Java20Parser.Identifier)
                pass
            elif token in [Java20Parser.EXPORTS, Java20Parser.MODULE, Java20Parser.NONSEALED, Java20Parser.OPEN, Java20Parser.OPENS, Java20Parser.PROVIDES, Java20Parser.REQUIRES, Java20Parser.TO, Java20Parser.TRANSITIVE, Java20Parser.USES, Java20Parser.WITH]:
                self.enterOuterAlt(localctx, 2)
                self.state = 506
                self.contextualKeywordMinusForTypeIdentifier()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnqualifiedMethodIdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(Java20Parser.Identifier, 0)

        def contextualKeywordMinusForUnqualifiedMethodIdentifier(self):
            return self.getTypedRuleContext(Java20Parser.ContextualKeywordMinusForUnqualifiedMethodIdentifierContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_unqualifiedMethodIdentifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnqualifiedMethodIdentifier" ):
                listener.enterUnqualifiedMethodIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnqualifiedMethodIdentifier" ):
                listener.exitUnqualifiedMethodIdentifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnqualifiedMethodIdentifier" ):
                return visitor.visitUnqualifiedMethodIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def unqualifiedMethodIdentifier(self):

        localctx = Java20Parser.UnqualifiedMethodIdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_unqualifiedMethodIdentifier)
        try:
            self.state = 511
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Java20Parser.Identifier]:
                self.enterOuterAlt(localctx, 1)
                self.state = 509
                self.match(Java20Parser.Identifier)
                pass
            elif token in [Java20Parser.EXPORTS, Java20Parser.MODULE, Java20Parser.NONSEALED, Java20Parser.OPEN, Java20Parser.OPENS, Java20Parser.PERMITS, Java20Parser.PROVIDES, Java20Parser.RECORD, Java20Parser.REQUIRES, Java20Parser.SEALED, Java20Parser.TO, Java20Parser.TRANSITIVE, Java20Parser.USES, Java20Parser.VAR, Java20Parser.WITH]:
                self.enterOuterAlt(localctx, 2)
                self.state = 510
                self.contextualKeywordMinusForUnqualifiedMethodIdentifier()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContextualKeywordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EXPORTS(self):
            return self.getToken(Java20Parser.EXPORTS, 0)

        def MODULE(self):
            return self.getToken(Java20Parser.MODULE, 0)

        def NONSEALED(self):
            return self.getToken(Java20Parser.NONSEALED, 0)

        def OPEN(self):
            return self.getToken(Java20Parser.OPEN, 0)

        def OPENS(self):
            return self.getToken(Java20Parser.OPENS, 0)

        def PERMITS(self):
            return self.getToken(Java20Parser.PERMITS, 0)

        def PROVIDES(self):
            return self.getToken(Java20Parser.PROVIDES, 0)

        def RECORD(self):
            return self.getToken(Java20Parser.RECORD, 0)

        def REQUIRES(self):
            return self.getToken(Java20Parser.REQUIRES, 0)

        def SEALED(self):
            return self.getToken(Java20Parser.SEALED, 0)

        def TO(self):
            return self.getToken(Java20Parser.TO, 0)

        def TRANSITIVE(self):
            return self.getToken(Java20Parser.TRANSITIVE, 0)

        def USES(self):
            return self.getToken(Java20Parser.USES, 0)

        def VAR(self):
            return self.getToken(Java20Parser.VAR, 0)

        def WITH(self):
            return self.getToken(Java20Parser.WITH, 0)

        def YIELD(self):
            return self.getToken(Java20Parser.YIELD, 0)

        def getRuleIndex(self):
            return Java20Parser.RULE_contextualKeyword

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContextualKeyword" ):
                listener.enterContextualKeyword(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContextualKeyword" ):
                listener.exitContextualKeyword(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContextualKeyword" ):
                return visitor.visitContextualKeyword(self)
            else:
                return visitor.visitChildren(self)




    def contextualKeyword(self):

        localctx = Java20Parser.ContextualKeywordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_contextualKeyword)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 513
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java20Parser.EXPORTS) | (1 << Java20Parser.MODULE) | (1 << Java20Parser.NONSEALED) | (1 << Java20Parser.OPEN) | (1 << Java20Parser.OPENS) | (1 << Java20Parser.PERMITS) | (1 << Java20Parser.PROVIDES) | (1 << Java20Parser.RECORD) | (1 << Java20Parser.REQUIRES) | (1 << Java20Parser.SEALED) | (1 << Java20Parser.TO) | (1 << Java20Parser.TRANSITIVE) | (1 << Java20Parser.USES) | (1 << Java20Parser.VAR) | (1 << Java20Parser.WITH) | (1 << Java20Parser.YIELD))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContextualKeywordMinusForTypeIdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EXPORTS(self):
            return self.getToken(Java20Parser.EXPORTS, 0)

        def MODULE(self):
            return self.getToken(Java20Parser.MODULE, 0)

        def NONSEALED(self):
            return self.getToken(Java20Parser.NONSEALED, 0)

        def OPEN(self):
            return self.getToken(Java20Parser.OPEN, 0)

        def OPENS(self):
            return self.getToken(Java20Parser.OPENS, 0)

        def PROVIDES(self):
            return self.getToken(Java20Parser.PROVIDES, 0)

        def REQUIRES(self):
            return self.getToken(Java20Parser.REQUIRES, 0)

        def TO(self):
            return self.getToken(Java20Parser.TO, 0)

        def TRANSITIVE(self):
            return self.getToken(Java20Parser.TRANSITIVE, 0)

        def USES(self):
            return self.getToken(Java20Parser.USES, 0)

        def WITH(self):
            return self.getToken(Java20Parser.WITH, 0)

        def getRuleIndex(self):
            return Java20Parser.RULE_contextualKeywordMinusForTypeIdentifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContextualKeywordMinusForTypeIdentifier" ):
                listener.enterContextualKeywordMinusForTypeIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContextualKeywordMinusForTypeIdentifier" ):
                listener.exitContextualKeywordMinusForTypeIdentifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContextualKeywordMinusForTypeIdentifier" ):
                return visitor.visitContextualKeywordMinusForTypeIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def contextualKeywordMinusForTypeIdentifier(self):

        localctx = Java20Parser.ContextualKeywordMinusForTypeIdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_contextualKeywordMinusForTypeIdentifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 515
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java20Parser.EXPORTS) | (1 << Java20Parser.MODULE) | (1 << Java20Parser.NONSEALED) | (1 << Java20Parser.OPEN) | (1 << Java20Parser.OPENS) | (1 << Java20Parser.PROVIDES) | (1 << Java20Parser.REQUIRES) | (1 << Java20Parser.TO) | (1 << Java20Parser.TRANSITIVE) | (1 << Java20Parser.USES) | (1 << Java20Parser.WITH))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContextualKeywordMinusForUnqualifiedMethodIdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EXPORTS(self):
            return self.getToken(Java20Parser.EXPORTS, 0)

        def MODULE(self):
            return self.getToken(Java20Parser.MODULE, 0)

        def NONSEALED(self):
            return self.getToken(Java20Parser.NONSEALED, 0)

        def OPEN(self):
            return self.getToken(Java20Parser.OPEN, 0)

        def OPENS(self):
            return self.getToken(Java20Parser.OPENS, 0)

        def PERMITS(self):
            return self.getToken(Java20Parser.PERMITS, 0)

        def PROVIDES(self):
            return self.getToken(Java20Parser.PROVIDES, 0)

        def RECORD(self):
            return self.getToken(Java20Parser.RECORD, 0)

        def REQUIRES(self):
            return self.getToken(Java20Parser.REQUIRES, 0)

        def SEALED(self):
            return self.getToken(Java20Parser.SEALED, 0)

        def TO(self):
            return self.getToken(Java20Parser.TO, 0)

        def TRANSITIVE(self):
            return self.getToken(Java20Parser.TRANSITIVE, 0)

        def USES(self):
            return self.getToken(Java20Parser.USES, 0)

        def VAR(self):
            return self.getToken(Java20Parser.VAR, 0)

        def WITH(self):
            return self.getToken(Java20Parser.WITH, 0)

        def getRuleIndex(self):
            return Java20Parser.RULE_contextualKeywordMinusForUnqualifiedMethodIdentifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContextualKeywordMinusForUnqualifiedMethodIdentifier" ):
                listener.enterContextualKeywordMinusForUnqualifiedMethodIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContextualKeywordMinusForUnqualifiedMethodIdentifier" ):
                listener.exitContextualKeywordMinusForUnqualifiedMethodIdentifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContextualKeywordMinusForUnqualifiedMethodIdentifier" ):
                return visitor.visitContextualKeywordMinusForUnqualifiedMethodIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def contextualKeywordMinusForUnqualifiedMethodIdentifier(self):

        localctx = Java20Parser.ContextualKeywordMinusForUnqualifiedMethodIdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_contextualKeywordMinusForUnqualifiedMethodIdentifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 517
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java20Parser.EXPORTS) | (1 << Java20Parser.MODULE) | (1 << Java20Parser.NONSEALED) | (1 << Java20Parser.OPEN) | (1 << Java20Parser.OPENS) | (1 << Java20Parser.PERMITS) | (1 << Java20Parser.PROVIDES) | (1 << Java20Parser.RECORD) | (1 << Java20Parser.REQUIRES) | (1 << Java20Parser.SEALED) | (1 << Java20Parser.TO) | (1 << Java20Parser.TRANSITIVE) | (1 << Java20Parser.USES) | (1 << Java20Parser.VAR) | (1 << Java20Parser.WITH))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IntegerLiteral(self):
            return self.getToken(Java20Parser.IntegerLiteral, 0)

        def FloatingPointLiteral(self):
            return self.getToken(Java20Parser.FloatingPointLiteral, 0)

        def BooleanLiteral(self):
            return self.getToken(Java20Parser.BooleanLiteral, 0)

        def CharacterLiteral(self):
            return self.getToken(Java20Parser.CharacterLiteral, 0)

        def StringLiteral(self):
            return self.getToken(Java20Parser.StringLiteral, 0)

        def TextBlock(self):
            return self.getToken(Java20Parser.TextBlock, 0)

        def NullLiteral(self):
            return self.getToken(Java20Parser.NullLiteral, 0)

        def getRuleIndex(self):
            return Java20Parser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = Java20Parser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 519
            _la = self._input.LA(1)
            if not(((((_la - 69)) & ~0x3f) == 0 and ((1 << (_la - 69)) & ((1 << (Java20Parser.IntegerLiteral - 69)) | (1 << (Java20Parser.FloatingPointLiteral - 69)) | (1 << (Java20Parser.BooleanLiteral - 69)) | (1 << (Java20Parser.CharacterLiteral - 69)) | (1 << (Java20Parser.StringLiteral - 69)) | (1 << (Java20Parser.TextBlock - 69)) | (1 << (Java20Parser.NullLiteral - 69)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimitiveTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def numericType(self):
            return self.getTypedRuleContext(Java20Parser.NumericTypeContext,0)


        def BOOLEAN(self):
            return self.getToken(Java20Parser.BOOLEAN, 0)

        def annotation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.AnnotationContext)
            else:
                return self.getTypedRuleContext(Java20Parser.AnnotationContext,i)


        def getRuleIndex(self):
            return Java20Parser.RULE_primitiveType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimitiveType" ):
                listener.enterPrimitiveType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimitiveType" ):
                listener.exitPrimitiveType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitiveType" ):
                return visitor.visitPrimitiveType(self)
            else:
                return visitor.visitChildren(self)




    def primitiveType(self):

        localctx = Java20Parser.PrimitiveTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_primitiveType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 524
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Java20Parser.AT:
                self.state = 521
                self.annotation()
                self.state = 526
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 529
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Java20Parser.BYTE, Java20Parser.CHAR, Java20Parser.DOUBLE, Java20Parser.FLOAT, Java20Parser.INT, Java20Parser.LONG, Java20Parser.SHORT]:
                self.state = 527
                self.numericType()
                pass
            elif token in [Java20Parser.BOOLEAN]:
                self.state = 528
                self.match(Java20Parser.BOOLEAN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumericTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def integralType(self):
            return self.getTypedRuleContext(Java20Parser.IntegralTypeContext,0)


        def floatingPointType(self):
            return self.getTypedRuleContext(Java20Parser.FloatingPointTypeContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_numericType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumericType" ):
                listener.enterNumericType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumericType" ):
                listener.exitNumericType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumericType" ):
                return visitor.visitNumericType(self)
            else:
                return visitor.visitChildren(self)




    def numericType(self):

        localctx = Java20Parser.NumericTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_numericType)
        try:
            self.state = 533
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Java20Parser.BYTE, Java20Parser.CHAR, Java20Parser.INT, Java20Parser.LONG, Java20Parser.SHORT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 531
                self.integralType()
                pass
            elif token in [Java20Parser.DOUBLE, Java20Parser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 532
                self.floatingPointType()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntegralTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BYTE(self):
            return self.getToken(Java20Parser.BYTE, 0)

        def SHORT(self):
            return self.getToken(Java20Parser.SHORT, 0)

        def INT(self):
            return self.getToken(Java20Parser.INT, 0)

        def LONG(self):
            return self.getToken(Java20Parser.LONG, 0)

        def CHAR(self):
            return self.getToken(Java20Parser.CHAR, 0)

        def getRuleIndex(self):
            return Java20Parser.RULE_integralType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntegralType" ):
                listener.enterIntegralType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntegralType" ):
                listener.exitIntegralType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntegralType" ):
                return visitor.visitIntegralType(self)
            else:
                return visitor.visitChildren(self)




    def integralType(self):

        localctx = Java20Parser.IntegralTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_integralType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 535
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java20Parser.BYTE) | (1 << Java20Parser.CHAR) | (1 << Java20Parser.INT) | (1 << Java20Parser.LONG) | (1 << Java20Parser.SHORT))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FloatingPointTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOAT(self):
            return self.getToken(Java20Parser.FLOAT, 0)

        def DOUBLE(self):
            return self.getToken(Java20Parser.DOUBLE, 0)

        def getRuleIndex(self):
            return Java20Parser.RULE_floatingPointType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloatingPointType" ):
                listener.enterFloatingPointType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloatingPointType" ):
                listener.exitFloatingPointType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloatingPointType" ):
                return visitor.visitFloatingPointType(self)
            else:
                return visitor.visitChildren(self)




    def floatingPointType(self):

        localctx = Java20Parser.FloatingPointTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_floatingPointType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 537
            _la = self._input.LA(1)
            if not(_la==Java20Parser.DOUBLE or _la==Java20Parser.FLOAT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReferenceTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classOrInterfaceType(self):
            return self.getTypedRuleContext(Java20Parser.ClassOrInterfaceTypeContext,0)


        def typeVariable(self):
            return self.getTypedRuleContext(Java20Parser.TypeVariableContext,0)


        def arrayType(self):
            return self.getTypedRuleContext(Java20Parser.ArrayTypeContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_referenceType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReferenceType" ):
                listener.enterReferenceType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReferenceType" ):
                listener.exitReferenceType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReferenceType" ):
                return visitor.visitReferenceType(self)
            else:
                return visitor.visitChildren(self)




    def referenceType(self):

        localctx = Java20Parser.ReferenceTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_referenceType)
        try:
            self.state = 542
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 539
                self.classOrInterfaceType()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 540
                self.typeVariable()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 541
                self.arrayType()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CoitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self):
            return self.getToken(Java20Parser.DOT, 0)

        def typeIdentifier(self):
            return self.getTypedRuleContext(Java20Parser.TypeIdentifierContext,0)


        def annotation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.AnnotationContext)
            else:
                return self.getTypedRuleContext(Java20Parser.AnnotationContext,i)


        def typeArguments(self):
            return self.getTypedRuleContext(Java20Parser.TypeArgumentsContext,0)


        def coit(self):
            return self.getTypedRuleContext(Java20Parser.CoitContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_coit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCoit" ):
                listener.enterCoit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCoit" ):
                listener.exitCoit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCoit" ):
                return visitor.visitCoit(self)
            else:
                return visitor.visitChildren(self)




    def coit(self):

        localctx = Java20Parser.CoitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_coit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 544
            self.match(Java20Parser.DOT)
            self.state = 548
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Java20Parser.AT:
                self.state = 545
                self.annotation()
                self.state = 550
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 551
            self.typeIdentifier()
            self.state = 553
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 552
                self.typeArguments()


            self.state = 556
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 555
                self.coit()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassOrInterfaceTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeIdentifier(self):
            return self.getTypedRuleContext(Java20Parser.TypeIdentifierContext,0)


        def packageName(self):
            return self.getTypedRuleContext(Java20Parser.PackageNameContext,0)


        def DOT(self):
            return self.getToken(Java20Parser.DOT, 0)

        def annotation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.AnnotationContext)
            else:
                return self.getTypedRuleContext(Java20Parser.AnnotationContext,i)


        def typeArguments(self):
            return self.getTypedRuleContext(Java20Parser.TypeArgumentsContext,0)


        def coit(self):
            return self.getTypedRuleContext(Java20Parser.CoitContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_classOrInterfaceType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassOrInterfaceType" ):
                listener.enterClassOrInterfaceType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassOrInterfaceType" ):
                listener.exitClassOrInterfaceType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassOrInterfaceType" ):
                return visitor.visitClassOrInterfaceType(self)
            else:
                return visitor.visitChildren(self)




    def classOrInterfaceType(self):

        localctx = Java20Parser.ClassOrInterfaceTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_classOrInterfaceType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 561
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 558
                self.packageName()
                self.state = 559
                self.match(Java20Parser.DOT)


            self.state = 566
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Java20Parser.AT:
                self.state = 563
                self.annotation()
                self.state = 568
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 569
            self.typeIdentifier()
            self.state = 571
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 570
                self.typeArguments()


            self.state = 574
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 573
                self.coit()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeIdentifier(self):
            return self.getTypedRuleContext(Java20Parser.TypeIdentifierContext,0)


        def annotation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.AnnotationContext)
            else:
                return self.getTypedRuleContext(Java20Parser.AnnotationContext,i)


        def typeArguments(self):
            return self.getTypedRuleContext(Java20Parser.TypeArgumentsContext,0)


        def packageName(self):
            return self.getTypedRuleContext(Java20Parser.PackageNameContext,0)


        def DOT(self):
            return self.getToken(Java20Parser.DOT, 0)

        def classOrInterfaceType(self):
            return self.getTypedRuleContext(Java20Parser.ClassOrInterfaceTypeContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_classType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassType" ):
                listener.enterClassType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassType" ):
                listener.exitClassType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassType" ):
                return visitor.visitClassType(self)
            else:
                return visitor.visitChildren(self)




    def classType(self):

        localctx = Java20Parser.ClassTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_classType)
        self._la = 0 # Token type
        try:
            self.state = 610
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 579
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==Java20Parser.AT:
                    self.state = 576
                    self.annotation()
                    self.state = 581
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 582
                self.typeIdentifier()
                self.state = 584
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Java20Parser.LT:
                    self.state = 583
                    self.typeArguments()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 586
                self.packageName()
                self.state = 587
                self.match(Java20Parser.DOT)
                self.state = 591
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==Java20Parser.AT:
                    self.state = 588
                    self.annotation()
                    self.state = 593
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 594
                self.typeIdentifier()
                self.state = 596
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Java20Parser.LT:
                    self.state = 595
                    self.typeArguments()


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 598
                self.classOrInterfaceType()
                self.state = 599
                self.match(Java20Parser.DOT)
                self.state = 603
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==Java20Parser.AT:
                    self.state = 600
                    self.annotation()
                    self.state = 605
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 606
                self.typeIdentifier()
                self.state = 608
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Java20Parser.LT:
                    self.state = 607
                    self.typeArguments()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfaceTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classType(self):
            return self.getTypedRuleContext(Java20Parser.ClassTypeContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_interfaceType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterfaceType" ):
                listener.enterInterfaceType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterfaceType" ):
                listener.exitInterfaceType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfaceType" ):
                return visitor.visitInterfaceType(self)
            else:
                return visitor.visitChildren(self)




    def interfaceType(self):

        localctx = Java20Parser.InterfaceTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_interfaceType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 612
            self.classType()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeVariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeIdentifier(self):
            return self.getTypedRuleContext(Java20Parser.TypeIdentifierContext,0)


        def annotation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.AnnotationContext)
            else:
                return self.getTypedRuleContext(Java20Parser.AnnotationContext,i)


        def getRuleIndex(self):
            return Java20Parser.RULE_typeVariable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeVariable" ):
                listener.enterTypeVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeVariable" ):
                listener.exitTypeVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeVariable" ):
                return visitor.visitTypeVariable(self)
            else:
                return visitor.visitChildren(self)




    def typeVariable(self):

        localctx = Java20Parser.TypeVariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_typeVariable)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 617
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Java20Parser.AT:
                self.state = 614
                self.annotation()
                self.state = 619
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 620
            self.typeIdentifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitiveType(self):
            return self.getTypedRuleContext(Java20Parser.PrimitiveTypeContext,0)


        def dims(self):
            return self.getTypedRuleContext(Java20Parser.DimsContext,0)


        def classType(self):
            return self.getTypedRuleContext(Java20Parser.ClassTypeContext,0)


        def typeVariable(self):
            return self.getTypedRuleContext(Java20Parser.TypeVariableContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_arrayType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayType" ):
                listener.enterArrayType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayType" ):
                listener.exitArrayType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayType" ):
                return visitor.visitArrayType(self)
            else:
                return visitor.visitChildren(self)




    def arrayType(self):

        localctx = Java20Parser.ArrayTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_arrayType)
        try:
            self.state = 631
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 622
                self.primitiveType()
                self.state = 623
                self.dims()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 625
                self.classType()
                self.state = 626
                self.dims()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 628
                self.typeVariable()
                self.state = 629
                self.dims()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DimsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACK(self, i:int=None):
            if i is None:
                return self.getTokens(Java20Parser.LBRACK)
            else:
                return self.getToken(Java20Parser.LBRACK, i)

        def RBRACK(self, i:int=None):
            if i is None:
                return self.getTokens(Java20Parser.RBRACK)
            else:
                return self.getToken(Java20Parser.RBRACK, i)

        def annotation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.AnnotationContext)
            else:
                return self.getTypedRuleContext(Java20Parser.AnnotationContext,i)


        def getRuleIndex(self):
            return Java20Parser.RULE_dims

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDims" ):
                listener.enterDims(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDims" ):
                listener.exitDims(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDims" ):
                return visitor.visitDims(self)
            else:
                return visitor.visitChildren(self)




    def dims(self):

        localctx = Java20Parser.DimsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_dims)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 636
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Java20Parser.AT:
                self.state = 633
                self.annotation()
                self.state = 638
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 639
            self.match(Java20Parser.LBRACK)
            self.state = 640
            self.match(Java20Parser.RBRACK)
            self.state = 651
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 644
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==Java20Parser.AT:
                        self.state = 641
                        self.annotation()
                        self.state = 646
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 647
                    self.match(Java20Parser.LBRACK)
                    self.state = 648
                    self.match(Java20Parser.RBRACK) 
                self.state = 653
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeIdentifier(self):
            return self.getTypedRuleContext(Java20Parser.TypeIdentifierContext,0)


        def typeParameterModifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.TypeParameterModifierContext)
            else:
                return self.getTypedRuleContext(Java20Parser.TypeParameterModifierContext,i)


        def typeBound(self):
            return self.getTypedRuleContext(Java20Parser.TypeBoundContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_typeParameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeParameter" ):
                listener.enterTypeParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeParameter" ):
                listener.exitTypeParameter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeParameter" ):
                return visitor.visitTypeParameter(self)
            else:
                return visitor.visitChildren(self)




    def typeParameter(self):

        localctx = Java20Parser.TypeParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_typeParameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 657
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Java20Parser.AT:
                self.state = 654
                self.typeParameterModifier()
                self.state = 659
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 660
            self.typeIdentifier()
            self.state = 662
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Java20Parser.EXTENDS:
                self.state = 661
                self.typeBound()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeParameterModifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def annotation(self):
            return self.getTypedRuleContext(Java20Parser.AnnotationContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_typeParameterModifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeParameterModifier" ):
                listener.enterTypeParameterModifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeParameterModifier" ):
                listener.exitTypeParameterModifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeParameterModifier" ):
                return visitor.visitTypeParameterModifier(self)
            else:
                return visitor.visitChildren(self)




    def typeParameterModifier(self):

        localctx = Java20Parser.TypeParameterModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_typeParameterModifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 664
            self.annotation()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeBoundContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EXTENDS(self):
            return self.getToken(Java20Parser.EXTENDS, 0)

        def typeVariable(self):
            return self.getTypedRuleContext(Java20Parser.TypeVariableContext,0)


        def classOrInterfaceType(self):
            return self.getTypedRuleContext(Java20Parser.ClassOrInterfaceTypeContext,0)


        def additionalBound(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.AdditionalBoundContext)
            else:
                return self.getTypedRuleContext(Java20Parser.AdditionalBoundContext,i)


        def getRuleIndex(self):
            return Java20Parser.RULE_typeBound

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeBound" ):
                listener.enterTypeBound(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeBound" ):
                listener.exitTypeBound(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeBound" ):
                return visitor.visitTypeBound(self)
            else:
                return visitor.visitChildren(self)




    def typeBound(self):

        localctx = Java20Parser.TypeBoundContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_typeBound)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 666
            self.match(Java20Parser.EXTENDS)
            self.state = 675
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.state = 667
                self.typeVariable()
                pass

            elif la_ == 2:
                self.state = 668
                self.classOrInterfaceType()
                self.state = 672
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==Java20Parser.BITAND:
                    self.state = 669
                    self.additionalBound()
                    self.state = 674
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditionalBoundContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BITAND(self):
            return self.getToken(Java20Parser.BITAND, 0)

        def interfaceType(self):
            return self.getTypedRuleContext(Java20Parser.InterfaceTypeContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_additionalBound

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditionalBound" ):
                listener.enterAdditionalBound(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditionalBound" ):
                listener.exitAdditionalBound(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditionalBound" ):
                return visitor.visitAdditionalBound(self)
            else:
                return visitor.visitChildren(self)




    def additionalBound(self):

        localctx = Java20Parser.AdditionalBoundContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_additionalBound)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 677
            self.match(Java20Parser.BITAND)
            self.state = 678
            self.interfaceType()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeArgumentsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LT(self):
            return self.getToken(Java20Parser.LT, 0)

        def typeArgumentList(self):
            return self.getTypedRuleContext(Java20Parser.TypeArgumentListContext,0)


        def GT(self):
            return self.getToken(Java20Parser.GT, 0)

        def getRuleIndex(self):
            return Java20Parser.RULE_typeArguments

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeArguments" ):
                listener.enterTypeArguments(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeArguments" ):
                listener.exitTypeArguments(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeArguments" ):
                return visitor.visitTypeArguments(self)
            else:
                return visitor.visitChildren(self)




    def typeArguments(self):

        localctx = Java20Parser.TypeArgumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_typeArguments)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 680
            self.match(Java20Parser.LT)
            self.state = 681
            self.typeArgumentList()
            self.state = 682
            self.match(Java20Parser.GT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeArgumentListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeArgument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.TypeArgumentContext)
            else:
                return self.getTypedRuleContext(Java20Parser.TypeArgumentContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(Java20Parser.COMMA)
            else:
                return self.getToken(Java20Parser.COMMA, i)

        def getRuleIndex(self):
            return Java20Parser.RULE_typeArgumentList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeArgumentList" ):
                listener.enterTypeArgumentList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeArgumentList" ):
                listener.exitTypeArgumentList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeArgumentList" ):
                return visitor.visitTypeArgumentList(self)
            else:
                return visitor.visitChildren(self)




    def typeArgumentList(self):

        localctx = Java20Parser.TypeArgumentListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_typeArgumentList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 684
            self.typeArgument()
            self.state = 689
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Java20Parser.COMMA:
                self.state = 685
                self.match(Java20Parser.COMMA)
                self.state = 686
                self.typeArgument()
                self.state = 691
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeArgumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def referenceType(self):
            return self.getTypedRuleContext(Java20Parser.ReferenceTypeContext,0)


        def wildcard(self):
            return self.getTypedRuleContext(Java20Parser.WildcardContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_typeArgument

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeArgument" ):
                listener.enterTypeArgument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeArgument" ):
                listener.exitTypeArgument(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeArgument" ):
                return visitor.visitTypeArgument(self)
            else:
                return visitor.visitChildren(self)




    def typeArgument(self):

        localctx = Java20Parser.TypeArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_typeArgument)
        try:
            self.state = 694
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 692
                self.referenceType()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 693
                self.wildcard()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WildcardContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def QUESTION(self):
            return self.getToken(Java20Parser.QUESTION, 0)

        def annotation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.AnnotationContext)
            else:
                return self.getTypedRuleContext(Java20Parser.AnnotationContext,i)


        def wildcardBounds(self):
            return self.getTypedRuleContext(Java20Parser.WildcardBoundsContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_wildcard

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWildcard" ):
                listener.enterWildcard(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWildcard" ):
                listener.exitWildcard(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWildcard" ):
                return visitor.visitWildcard(self)
            else:
                return visitor.visitChildren(self)




    def wildcard(self):

        localctx = Java20Parser.WildcardContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_wildcard)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 699
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Java20Parser.AT:
                self.state = 696
                self.annotation()
                self.state = 701
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 702
            self.match(Java20Parser.QUESTION)
            self.state = 704
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Java20Parser.EXTENDS or _la==Java20Parser.SUPER:
                self.state = 703
                self.wildcardBounds()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WildcardBoundsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EXTENDS(self):
            return self.getToken(Java20Parser.EXTENDS, 0)

        def referenceType(self):
            return self.getTypedRuleContext(Java20Parser.ReferenceTypeContext,0)


        def SUPER(self):
            return self.getToken(Java20Parser.SUPER, 0)

        def getRuleIndex(self):
            return Java20Parser.RULE_wildcardBounds

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWildcardBounds" ):
                listener.enterWildcardBounds(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWildcardBounds" ):
                listener.exitWildcardBounds(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWildcardBounds" ):
                return visitor.visitWildcardBounds(self)
            else:
                return visitor.visitChildren(self)




    def wildcardBounds(self):

        localctx = Java20Parser.WildcardBoundsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_wildcardBounds)
        try:
            self.state = 710
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Java20Parser.EXTENDS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 706
                self.match(Java20Parser.EXTENDS)
                self.state = 707
                self.referenceType()
                pass
            elif token in [Java20Parser.SUPER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 708
                self.match(Java20Parser.SUPER)
                self.state = 709
                self.referenceType()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ModuleNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(Java20Parser.IdentifierContext,0)


        def DOT(self):
            return self.getToken(Java20Parser.DOT, 0)

        def moduleName(self):
            return self.getTypedRuleContext(Java20Parser.ModuleNameContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_moduleName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModuleName" ):
                listener.enterModuleName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModuleName" ):
                listener.exitModuleName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModuleName" ):
                return visitor.visitModuleName(self)
            else:
                return visitor.visitChildren(self)




    def moduleName(self):

        localctx = Java20Parser.ModuleNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_moduleName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 712
            self.identifier()
            self.state = 715
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Java20Parser.DOT:
                self.state = 713
                self.match(Java20Parser.DOT)
                self.state = 714
                self.moduleName()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PackageNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(Java20Parser.IdentifierContext,0)


        def DOT(self):
            return self.getToken(Java20Parser.DOT, 0)

        def packageName(self):
            return self.getTypedRuleContext(Java20Parser.PackageNameContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_packageName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPackageName" ):
                listener.enterPackageName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPackageName" ):
                listener.exitPackageName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPackageName" ):
                return visitor.visitPackageName(self)
            else:
                return visitor.visitChildren(self)




    def packageName(self):

        localctx = Java20Parser.PackageNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_packageName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 717
            self.identifier()
            self.state = 720
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.state = 718
                self.match(Java20Parser.DOT)
                self.state = 719
                self.packageName()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def packageName(self):
            return self.getTypedRuleContext(Java20Parser.PackageNameContext,0)


        def DOT(self):
            return self.getToken(Java20Parser.DOT, 0)

        def typeIdentifier(self):
            return self.getTypedRuleContext(Java20Parser.TypeIdentifierContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_typeName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeName" ):
                listener.enterTypeName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeName" ):
                listener.exitTypeName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeName" ):
                return visitor.visitTypeName(self)
            else:
                return visitor.visitChildren(self)




    def typeName(self):

        localctx = Java20Parser.TypeNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_typeName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 722
            self.packageName()
            self.state = 725
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.state = 723
                self.match(Java20Parser.DOT)
                self.state = 724
                self.typeIdentifier()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PackageOrTypeNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(Java20Parser.IdentifierContext,0)


        def DOT(self):
            return self.getToken(Java20Parser.DOT, 0)

        def packageOrTypeName(self):
            return self.getTypedRuleContext(Java20Parser.PackageOrTypeNameContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_packageOrTypeName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPackageOrTypeName" ):
                listener.enterPackageOrTypeName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPackageOrTypeName" ):
                listener.exitPackageOrTypeName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPackageOrTypeName" ):
                return visitor.visitPackageOrTypeName(self)
            else:
                return visitor.visitChildren(self)




    def packageOrTypeName(self):

        localctx = Java20Parser.PackageOrTypeNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_packageOrTypeName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 727
            self.identifier()
            self.state = 730
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.state = 728
                self.match(Java20Parser.DOT)
                self.state = 729
                self.packageOrTypeName()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(Java20Parser.IdentifierContext,0)


        def ambiguousName(self):
            return self.getTypedRuleContext(Java20Parser.AmbiguousNameContext,0)


        def DOT(self):
            return self.getToken(Java20Parser.DOT, 0)

        def getRuleIndex(self):
            return Java20Parser.RULE_expressionName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionName" ):
                listener.enterExpressionName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionName" ):
                listener.exitExpressionName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionName" ):
                return visitor.visitExpressionName(self)
            else:
                return visitor.visitChildren(self)




    def expressionName(self):

        localctx = Java20Parser.ExpressionNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_expressionName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 735
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.state = 732
                self.ambiguousName()
                self.state = 733
                self.match(Java20Parser.DOT)


            self.state = 737
            self.identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unqualifiedMethodIdentifier(self):
            return self.getTypedRuleContext(Java20Parser.UnqualifiedMethodIdentifierContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_methodName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodName" ):
                listener.enterMethodName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodName" ):
                listener.exitMethodName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodName" ):
                return visitor.visitMethodName(self)
            else:
                return visitor.visitChildren(self)




    def methodName(self):

        localctx = Java20Parser.MethodNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_methodName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 739
            self.unqualifiedMethodIdentifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AmbiguousNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(Java20Parser.IdentifierContext,0)


        def DOT(self):
            return self.getToken(Java20Parser.DOT, 0)

        def ambiguousName(self):
            return self.getTypedRuleContext(Java20Parser.AmbiguousNameContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_ambiguousName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAmbiguousName" ):
                listener.enterAmbiguousName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAmbiguousName" ):
                listener.exitAmbiguousName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAmbiguousName" ):
                return visitor.visitAmbiguousName(self)
            else:
                return visitor.visitChildren(self)




    def ambiguousName(self):

        localctx = Java20Parser.AmbiguousNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_ambiguousName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 741
            self.identifier()
            self.state = 744
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.state = 742
                self.match(Java20Parser.DOT)
                self.state = 743
                self.ambiguousName()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompilationUnitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ordinaryCompilationUnit(self):
            return self.getTypedRuleContext(Java20Parser.OrdinaryCompilationUnitContext,0)


        def modularCompilationUnit(self):
            return self.getTypedRuleContext(Java20Parser.ModularCompilationUnitContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_compilationUnit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompilationUnit" ):
                listener.enterCompilationUnit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompilationUnit" ):
                listener.exitCompilationUnit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompilationUnit" ):
                return visitor.visitCompilationUnit(self)
            else:
                return visitor.visitChildren(self)




    def compilationUnit(self):

        localctx = Java20Parser.CompilationUnitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_compilationUnit)
        try:
            self.state = 748
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 746
                self.ordinaryCompilationUnit()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 747
                self.modularCompilationUnit()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OrdinaryCompilationUnitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def packageDeclaration(self):
            return self.getTypedRuleContext(Java20Parser.PackageDeclarationContext,0)


        def importDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.ImportDeclarationContext)
            else:
                return self.getTypedRuleContext(Java20Parser.ImportDeclarationContext,i)


        def topLevelClassOrInterfaceDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.TopLevelClassOrInterfaceDeclarationContext)
            else:
                return self.getTypedRuleContext(Java20Parser.TopLevelClassOrInterfaceDeclarationContext,i)


        def getRuleIndex(self):
            return Java20Parser.RULE_ordinaryCompilationUnit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrdinaryCompilationUnit" ):
                listener.enterOrdinaryCompilationUnit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrdinaryCompilationUnit" ):
                listener.exitOrdinaryCompilationUnit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrdinaryCompilationUnit" ):
                return visitor.visitOrdinaryCompilationUnit(self)
            else:
                return visitor.visitChildren(self)




    def ordinaryCompilationUnit(self):

        localctx = Java20Parser.OrdinaryCompilationUnitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_ordinaryCompilationUnit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 751
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.state = 750
                self.packageDeclaration()


            self.state = 756
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Java20Parser.IMPORT:
                self.state = 753
                self.importDeclaration()
                self.state = 758
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 762
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java20Parser.NONSEALED) | (1 << Java20Parser.RECORD) | (1 << Java20Parser.SEALED) | (1 << Java20Parser.ABSTRACT) | (1 << Java20Parser.CLASS) | (1 << Java20Parser.ENUM) | (1 << Java20Parser.FINAL) | (1 << Java20Parser.INTERFACE) | (1 << Java20Parser.PRIVATE) | (1 << Java20Parser.PROTECTED) | (1 << Java20Parser.PUBLIC) | (1 << Java20Parser.STATIC) | (1 << Java20Parser.STRICTFP))) != 0) or _la==Java20Parser.SEMI or _la==Java20Parser.AT:
                self.state = 759
                self.topLevelClassOrInterfaceDeclaration()
                self.state = 764
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ModularCompilationUnitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def moduleDeclaration(self):
            return self.getTypedRuleContext(Java20Parser.ModuleDeclarationContext,0)


        def importDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.ImportDeclarationContext)
            else:
                return self.getTypedRuleContext(Java20Parser.ImportDeclarationContext,i)


        def getRuleIndex(self):
            return Java20Parser.RULE_modularCompilationUnit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModularCompilationUnit" ):
                listener.enterModularCompilationUnit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModularCompilationUnit" ):
                listener.exitModularCompilationUnit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModularCompilationUnit" ):
                return visitor.visitModularCompilationUnit(self)
            else:
                return visitor.visitChildren(self)




    def modularCompilationUnit(self):

        localctx = Java20Parser.ModularCompilationUnitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_modularCompilationUnit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 768
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Java20Parser.IMPORT:
                self.state = 765
                self.importDeclaration()
                self.state = 770
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 771
            self.moduleDeclaration()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PackageDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PACKAGE(self):
            return self.getToken(Java20Parser.PACKAGE, 0)

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.IdentifierContext)
            else:
                return self.getTypedRuleContext(Java20Parser.IdentifierContext,i)


        def SEMI(self):
            return self.getToken(Java20Parser.SEMI, 0)

        def packageModifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.PackageModifierContext)
            else:
                return self.getTypedRuleContext(Java20Parser.PackageModifierContext,i)


        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(Java20Parser.DOT)
            else:
                return self.getToken(Java20Parser.DOT, i)

        def getRuleIndex(self):
            return Java20Parser.RULE_packageDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPackageDeclaration" ):
                listener.enterPackageDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPackageDeclaration" ):
                listener.exitPackageDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPackageDeclaration" ):
                return visitor.visitPackageDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def packageDeclaration(self):

        localctx = Java20Parser.PackageDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_packageDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 776
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Java20Parser.AT:
                self.state = 773
                self.packageModifier()
                self.state = 778
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 779
            self.match(Java20Parser.PACKAGE)
            self.state = 780
            self.identifier()
            self.state = 785
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Java20Parser.DOT:
                self.state = 781
                self.match(Java20Parser.DOT)
                self.state = 782
                self.identifier()
                self.state = 787
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 788
            self.match(Java20Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PackageModifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def annotation(self):
            return self.getTypedRuleContext(Java20Parser.AnnotationContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_packageModifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPackageModifier" ):
                listener.enterPackageModifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPackageModifier" ):
                listener.exitPackageModifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPackageModifier" ):
                return visitor.visitPackageModifier(self)
            else:
                return visitor.visitChildren(self)




    def packageModifier(self):

        localctx = Java20Parser.PackageModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_packageModifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 790
            self.annotation()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImportDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def singleTypeImportDeclaration(self):
            return self.getTypedRuleContext(Java20Parser.SingleTypeImportDeclarationContext,0)


        def typeImportOnDemandDeclaration(self):
            return self.getTypedRuleContext(Java20Parser.TypeImportOnDemandDeclarationContext,0)


        def singleStaticImportDeclaration(self):
            return self.getTypedRuleContext(Java20Parser.SingleStaticImportDeclarationContext,0)


        def staticImportOnDemandDeclaration(self):
            return self.getTypedRuleContext(Java20Parser.StaticImportOnDemandDeclarationContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_importDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImportDeclaration" ):
                listener.enterImportDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImportDeclaration" ):
                listener.exitImportDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImportDeclaration" ):
                return visitor.visitImportDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def importDeclaration(self):

        localctx = Java20Parser.ImportDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_importDeclaration)
        try:
            self.state = 796
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 792
                self.singleTypeImportDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 793
                self.typeImportOnDemandDeclaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 794
                self.singleStaticImportDeclaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 795
                self.staticImportOnDemandDeclaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SingleTypeImportDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IMPORT(self):
            return self.getToken(Java20Parser.IMPORT, 0)

        def typeName(self):
            return self.getTypedRuleContext(Java20Parser.TypeNameContext,0)


        def SEMI(self):
            return self.getToken(Java20Parser.SEMI, 0)

        def getRuleIndex(self):
            return Java20Parser.RULE_singleTypeImportDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSingleTypeImportDeclaration" ):
                listener.enterSingleTypeImportDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSingleTypeImportDeclaration" ):
                listener.exitSingleTypeImportDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSingleTypeImportDeclaration" ):
                return visitor.visitSingleTypeImportDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def singleTypeImportDeclaration(self):

        localctx = Java20Parser.SingleTypeImportDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_singleTypeImportDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 798
            self.match(Java20Parser.IMPORT)
            self.state = 799
            self.typeName()
            self.state = 800
            self.match(Java20Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeImportOnDemandDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IMPORT(self):
            return self.getToken(Java20Parser.IMPORT, 0)

        def packageOrTypeName(self):
            return self.getTypedRuleContext(Java20Parser.PackageOrTypeNameContext,0)


        def DOT(self):
            return self.getToken(Java20Parser.DOT, 0)

        def MUL(self):
            return self.getToken(Java20Parser.MUL, 0)

        def SEMI(self):
            return self.getToken(Java20Parser.SEMI, 0)

        def getRuleIndex(self):
            return Java20Parser.RULE_typeImportOnDemandDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeImportOnDemandDeclaration" ):
                listener.enterTypeImportOnDemandDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeImportOnDemandDeclaration" ):
                listener.exitTypeImportOnDemandDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeImportOnDemandDeclaration" ):
                return visitor.visitTypeImportOnDemandDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def typeImportOnDemandDeclaration(self):

        localctx = Java20Parser.TypeImportOnDemandDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_typeImportOnDemandDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 802
            self.match(Java20Parser.IMPORT)
            self.state = 803
            self.packageOrTypeName()
            self.state = 804
            self.match(Java20Parser.DOT)
            self.state = 805
            self.match(Java20Parser.MUL)
            self.state = 806
            self.match(Java20Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SingleStaticImportDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IMPORT(self):
            return self.getToken(Java20Parser.IMPORT, 0)

        def STATIC(self):
            return self.getToken(Java20Parser.STATIC, 0)

        def typeName(self):
            return self.getTypedRuleContext(Java20Parser.TypeNameContext,0)


        def DOT(self):
            return self.getToken(Java20Parser.DOT, 0)

        def identifier(self):
            return self.getTypedRuleContext(Java20Parser.IdentifierContext,0)


        def SEMI(self):
            return self.getToken(Java20Parser.SEMI, 0)

        def getRuleIndex(self):
            return Java20Parser.RULE_singleStaticImportDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSingleStaticImportDeclaration" ):
                listener.enterSingleStaticImportDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSingleStaticImportDeclaration" ):
                listener.exitSingleStaticImportDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSingleStaticImportDeclaration" ):
                return visitor.visitSingleStaticImportDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def singleStaticImportDeclaration(self):

        localctx = Java20Parser.SingleStaticImportDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_singleStaticImportDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 808
            self.match(Java20Parser.IMPORT)
            self.state = 809
            self.match(Java20Parser.STATIC)
            self.state = 810
            self.typeName()
            self.state = 811
            self.match(Java20Parser.DOT)
            self.state = 812
            self.identifier()
            self.state = 813
            self.match(Java20Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StaticImportOnDemandDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IMPORT(self):
            return self.getToken(Java20Parser.IMPORT, 0)

        def STATIC(self):
            return self.getToken(Java20Parser.STATIC, 0)

        def typeName(self):
            return self.getTypedRuleContext(Java20Parser.TypeNameContext,0)


        def DOT(self):
            return self.getToken(Java20Parser.DOT, 0)

        def MUL(self):
            return self.getToken(Java20Parser.MUL, 0)

        def SEMI(self):
            return self.getToken(Java20Parser.SEMI, 0)

        def getRuleIndex(self):
            return Java20Parser.RULE_staticImportOnDemandDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStaticImportOnDemandDeclaration" ):
                listener.enterStaticImportOnDemandDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStaticImportOnDemandDeclaration" ):
                listener.exitStaticImportOnDemandDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStaticImportOnDemandDeclaration" ):
                return visitor.visitStaticImportOnDemandDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def staticImportOnDemandDeclaration(self):

        localctx = Java20Parser.StaticImportOnDemandDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_staticImportOnDemandDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 815
            self.match(Java20Parser.IMPORT)
            self.state = 816
            self.match(Java20Parser.STATIC)
            self.state = 817
            self.typeName()
            self.state = 818
            self.match(Java20Parser.DOT)
            self.state = 819
            self.match(Java20Parser.MUL)
            self.state = 820
            self.match(Java20Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TopLevelClassOrInterfaceDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classDeclaration(self):
            return self.getTypedRuleContext(Java20Parser.ClassDeclarationContext,0)


        def interfaceDeclaration(self):
            return self.getTypedRuleContext(Java20Parser.InterfaceDeclarationContext,0)


        def SEMI(self):
            return self.getToken(Java20Parser.SEMI, 0)

        def getRuleIndex(self):
            return Java20Parser.RULE_topLevelClassOrInterfaceDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTopLevelClassOrInterfaceDeclaration" ):
                listener.enterTopLevelClassOrInterfaceDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTopLevelClassOrInterfaceDeclaration" ):
                listener.exitTopLevelClassOrInterfaceDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTopLevelClassOrInterfaceDeclaration" ):
                return visitor.visitTopLevelClassOrInterfaceDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def topLevelClassOrInterfaceDeclaration(self):

        localctx = Java20Parser.TopLevelClassOrInterfaceDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_topLevelClassOrInterfaceDeclaration)
        try:
            self.state = 825
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 822
                self.classDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 823
                self.interfaceDeclaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 824
                self.match(Java20Parser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ModuleDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MODULE(self):
            return self.getToken(Java20Parser.MODULE, 0)

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.IdentifierContext)
            else:
                return self.getTypedRuleContext(Java20Parser.IdentifierContext,i)


        def LBRACE(self):
            return self.getToken(Java20Parser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(Java20Parser.RBRACE, 0)

        def annotation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.AnnotationContext)
            else:
                return self.getTypedRuleContext(Java20Parser.AnnotationContext,i)


        def OPEN(self):
            return self.getToken(Java20Parser.OPEN, 0)

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(Java20Parser.DOT)
            else:
                return self.getToken(Java20Parser.DOT, i)

        def moduleDirective(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.ModuleDirectiveContext)
            else:
                return self.getTypedRuleContext(Java20Parser.ModuleDirectiveContext,i)


        def getRuleIndex(self):
            return Java20Parser.RULE_moduleDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModuleDeclaration" ):
                listener.enterModuleDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModuleDeclaration" ):
                listener.exitModuleDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModuleDeclaration" ):
                return visitor.visitModuleDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def moduleDeclaration(self):

        localctx = Java20Parser.ModuleDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_moduleDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 830
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Java20Parser.AT:
                self.state = 827
                self.annotation()
                self.state = 832
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 834
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Java20Parser.OPEN:
                self.state = 833
                self.match(Java20Parser.OPEN)


            self.state = 836
            self.match(Java20Parser.MODULE)
            self.state = 837
            self.identifier()
            self.state = 842
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Java20Parser.DOT:
                self.state = 838
                self.match(Java20Parser.DOT)
                self.state = 839
                self.identifier()
                self.state = 844
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 845
            self.match(Java20Parser.LBRACE)
            self.state = 849
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java20Parser.EXPORTS) | (1 << Java20Parser.OPENS) | (1 << Java20Parser.PROVIDES) | (1 << Java20Parser.REQUIRES) | (1 << Java20Parser.USES))) != 0):
                self.state = 846
                self.moduleDirective()
                self.state = 851
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 852
            self.match(Java20Parser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ModuleDirectiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REQUIRES(self):
            return self.getToken(Java20Parser.REQUIRES, 0)

        def moduleName(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.ModuleNameContext)
            else:
                return self.getTypedRuleContext(Java20Parser.ModuleNameContext,i)


        def SEMI(self):
            return self.getToken(Java20Parser.SEMI, 0)

        def requiresModifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.RequiresModifierContext)
            else:
                return self.getTypedRuleContext(Java20Parser.RequiresModifierContext,i)


        def EXPORTS(self):
            return self.getToken(Java20Parser.EXPORTS, 0)

        def packageName(self):
            return self.getTypedRuleContext(Java20Parser.PackageNameContext,0)


        def TO(self):
            return self.getToken(Java20Parser.TO, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(Java20Parser.COMMA)
            else:
                return self.getToken(Java20Parser.COMMA, i)

        def OPENS(self):
            return self.getToken(Java20Parser.OPENS, 0)

        def USES(self):
            return self.getToken(Java20Parser.USES, 0)

        def typeName(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.TypeNameContext)
            else:
                return self.getTypedRuleContext(Java20Parser.TypeNameContext,i)


        def PROVIDES(self):
            return self.getToken(Java20Parser.PROVIDES, 0)

        def WITH(self):
            return self.getToken(Java20Parser.WITH, 0)

        def getRuleIndex(self):
            return Java20Parser.RULE_moduleDirective

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModuleDirective" ):
                listener.enterModuleDirective(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModuleDirective" ):
                listener.exitModuleDirective(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModuleDirective" ):
                return visitor.visitModuleDirective(self)
            else:
                return visitor.visitChildren(self)




    def moduleDirective(self):

        localctx = Java20Parser.ModuleDirectiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_moduleDirective)
        self._la = 0 # Token type
        try:
            self.state = 911
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Java20Parser.REQUIRES]:
                self.enterOuterAlt(localctx, 1)
                self.state = 854
                self.match(Java20Parser.REQUIRES)
                self.state = 858
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,54,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 855
                        self.requiresModifier() 
                    self.state = 860
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,54,self._ctx)

                self.state = 861
                self.moduleName()
                self.state = 862
                self.match(Java20Parser.SEMI)
                pass
            elif token in [Java20Parser.EXPORTS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 864
                self.match(Java20Parser.EXPORTS)
                self.state = 865
                self.packageName()
                self.state = 875
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Java20Parser.TO:
                    self.state = 866
                    self.match(Java20Parser.TO)
                    self.state = 867
                    self.moduleName()
                    self.state = 872
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==Java20Parser.COMMA:
                        self.state = 868
                        self.match(Java20Parser.COMMA)
                        self.state = 869
                        self.moduleName()
                        self.state = 874
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 877
                self.match(Java20Parser.SEMI)
                pass
            elif token in [Java20Parser.OPENS]:
                self.enterOuterAlt(localctx, 3)
                self.state = 879
                self.match(Java20Parser.OPENS)
                self.state = 880
                self.packageName()
                self.state = 890
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Java20Parser.TO:
                    self.state = 881
                    self.match(Java20Parser.TO)
                    self.state = 882
                    self.moduleName()
                    self.state = 887
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==Java20Parser.COMMA:
                        self.state = 883
                        self.match(Java20Parser.COMMA)
                        self.state = 884
                        self.moduleName()
                        self.state = 889
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 892
                self.match(Java20Parser.SEMI)
                pass
            elif token in [Java20Parser.USES]:
                self.enterOuterAlt(localctx, 4)
                self.state = 894
                self.match(Java20Parser.USES)
                self.state = 895
                self.typeName()
                self.state = 896
                self.match(Java20Parser.SEMI)
                pass
            elif token in [Java20Parser.PROVIDES]:
                self.enterOuterAlt(localctx, 5)
                self.state = 898
                self.match(Java20Parser.PROVIDES)
                self.state = 899
                self.typeName()
                self.state = 900
                self.match(Java20Parser.WITH)
                self.state = 901
                self.typeName()
                self.state = 906
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==Java20Parser.COMMA:
                    self.state = 902
                    self.match(Java20Parser.COMMA)
                    self.state = 903
                    self.typeName()
                    self.state = 908
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 909
                self.match(Java20Parser.SEMI)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RequiresModifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRANSITIVE(self):
            return self.getToken(Java20Parser.TRANSITIVE, 0)

        def STATIC(self):
            return self.getToken(Java20Parser.STATIC, 0)

        def getRuleIndex(self):
            return Java20Parser.RULE_requiresModifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRequiresModifier" ):
                listener.enterRequiresModifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRequiresModifier" ):
                listener.exitRequiresModifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRequiresModifier" ):
                return visitor.visitRequiresModifier(self)
            else:
                return visitor.visitChildren(self)




    def requiresModifier(self):

        localctx = Java20Parser.RequiresModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_requiresModifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 913
            _la = self._input.LA(1)
            if not(_la==Java20Parser.TRANSITIVE or _la==Java20Parser.STATIC):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def normalClassDeclaration(self):
            return self.getTypedRuleContext(Java20Parser.NormalClassDeclarationContext,0)


        def enumDeclaration(self):
            return self.getTypedRuleContext(Java20Parser.EnumDeclarationContext,0)


        def recordDeclaration(self):
            return self.getTypedRuleContext(Java20Parser.RecordDeclarationContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_classDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassDeclaration" ):
                listener.enterClassDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassDeclaration" ):
                listener.exitClassDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassDeclaration" ):
                return visitor.visitClassDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def classDeclaration(self):

        localctx = Java20Parser.ClassDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_classDeclaration)
        try:
            self.state = 918
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,61,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 915
                self.normalClassDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 916
                self.enumDeclaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 917
                self.recordDeclaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NormalClassDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(Java20Parser.CLASS, 0)

        def typeIdentifier(self):
            return self.getTypedRuleContext(Java20Parser.TypeIdentifierContext,0)


        def classBody(self):
            return self.getTypedRuleContext(Java20Parser.ClassBodyContext,0)


        def classModifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.ClassModifierContext)
            else:
                return self.getTypedRuleContext(Java20Parser.ClassModifierContext,i)


        def typeParameters(self):
            return self.getTypedRuleContext(Java20Parser.TypeParametersContext,0)


        def classExtends(self):
            return self.getTypedRuleContext(Java20Parser.ClassExtendsContext,0)


        def classImplements(self):
            return self.getTypedRuleContext(Java20Parser.ClassImplementsContext,0)


        def classPermits(self):
            return self.getTypedRuleContext(Java20Parser.ClassPermitsContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_normalClassDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNormalClassDeclaration" ):
                listener.enterNormalClassDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNormalClassDeclaration" ):
                listener.exitNormalClassDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNormalClassDeclaration" ):
                return visitor.visitNormalClassDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def normalClassDeclaration(self):

        localctx = Java20Parser.NormalClassDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_normalClassDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 923
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java20Parser.NONSEALED) | (1 << Java20Parser.SEALED) | (1 << Java20Parser.ABSTRACT) | (1 << Java20Parser.FINAL) | (1 << Java20Parser.PRIVATE) | (1 << Java20Parser.PROTECTED) | (1 << Java20Parser.PUBLIC) | (1 << Java20Parser.STATIC) | (1 << Java20Parser.STRICTFP))) != 0) or _la==Java20Parser.AT:
                self.state = 920
                self.classModifier()
                self.state = 925
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 926
            self.match(Java20Parser.CLASS)
            self.state = 927
            self.typeIdentifier()
            self.state = 929
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Java20Parser.LT:
                self.state = 928
                self.typeParameters()


            self.state = 932
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Java20Parser.EXTENDS:
                self.state = 931
                self.classExtends()


            self.state = 935
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Java20Parser.IMPLEMENTS:
                self.state = 934
                self.classImplements()


            self.state = 938
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Java20Parser.PERMITS:
                self.state = 937
                self.classPermits()


            self.state = 940
            self.classBody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassModifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def annotation(self):
            return self.getTypedRuleContext(Java20Parser.AnnotationContext,0)


        def PUBLIC(self):
            return self.getToken(Java20Parser.PUBLIC, 0)

        def PROTECTED(self):
            return self.getToken(Java20Parser.PROTECTED, 0)

        def PRIVATE(self):
            return self.getToken(Java20Parser.PRIVATE, 0)

        def ABSTRACT(self):
            return self.getToken(Java20Parser.ABSTRACT, 0)

        def STATIC(self):
            return self.getToken(Java20Parser.STATIC, 0)

        def FINAL(self):
            return self.getToken(Java20Parser.FINAL, 0)

        def SEALED(self):
            return self.getToken(Java20Parser.SEALED, 0)

        def NONSEALED(self):
            return self.getToken(Java20Parser.NONSEALED, 0)

        def STRICTFP(self):
            return self.getToken(Java20Parser.STRICTFP, 0)

        def getRuleIndex(self):
            return Java20Parser.RULE_classModifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassModifier" ):
                listener.enterClassModifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassModifier" ):
                listener.exitClassModifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassModifier" ):
                return visitor.visitClassModifier(self)
            else:
                return visitor.visitChildren(self)




    def classModifier(self):

        localctx = Java20Parser.ClassModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_classModifier)
        try:
            self.state = 952
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Java20Parser.AT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 942
                self.annotation()
                pass
            elif token in [Java20Parser.PUBLIC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 943
                self.match(Java20Parser.PUBLIC)
                pass
            elif token in [Java20Parser.PROTECTED]:
                self.enterOuterAlt(localctx, 3)
                self.state = 944
                self.match(Java20Parser.PROTECTED)
                pass
            elif token in [Java20Parser.PRIVATE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 945
                self.match(Java20Parser.PRIVATE)
                pass
            elif token in [Java20Parser.ABSTRACT]:
                self.enterOuterAlt(localctx, 5)
                self.state = 946
                self.match(Java20Parser.ABSTRACT)
                pass
            elif token in [Java20Parser.STATIC]:
                self.enterOuterAlt(localctx, 6)
                self.state = 947
                self.match(Java20Parser.STATIC)
                pass
            elif token in [Java20Parser.FINAL]:
                self.enterOuterAlt(localctx, 7)
                self.state = 948
                self.match(Java20Parser.FINAL)
                pass
            elif token in [Java20Parser.SEALED]:
                self.enterOuterAlt(localctx, 8)
                self.state = 949
                self.match(Java20Parser.SEALED)
                pass
            elif token in [Java20Parser.NONSEALED]:
                self.enterOuterAlt(localctx, 9)
                self.state = 950
                self.match(Java20Parser.NONSEALED)
                pass
            elif token in [Java20Parser.STRICTFP]:
                self.enterOuterAlt(localctx, 10)
                self.state = 951
                self.match(Java20Parser.STRICTFP)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeParametersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LT(self):
            return self.getToken(Java20Parser.LT, 0)

        def typeParameterList(self):
            return self.getTypedRuleContext(Java20Parser.TypeParameterListContext,0)


        def GT(self):
            return self.getToken(Java20Parser.GT, 0)

        def getRuleIndex(self):
            return Java20Parser.RULE_typeParameters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeParameters" ):
                listener.enterTypeParameters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeParameters" ):
                listener.exitTypeParameters(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeParameters" ):
                return visitor.visitTypeParameters(self)
            else:
                return visitor.visitChildren(self)




    def typeParameters(self):

        localctx = Java20Parser.TypeParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_typeParameters)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 954
            self.match(Java20Parser.LT)
            self.state = 955
            self.typeParameterList()
            self.state = 956
            self.match(Java20Parser.GT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeParameterListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeParameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.TypeParameterContext)
            else:
                return self.getTypedRuleContext(Java20Parser.TypeParameterContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(Java20Parser.COMMA)
            else:
                return self.getToken(Java20Parser.COMMA, i)

        def getRuleIndex(self):
            return Java20Parser.RULE_typeParameterList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeParameterList" ):
                listener.enterTypeParameterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeParameterList" ):
                listener.exitTypeParameterList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeParameterList" ):
                return visitor.visitTypeParameterList(self)
            else:
                return visitor.visitChildren(self)




    def typeParameterList(self):

        localctx = Java20Parser.TypeParameterListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_typeParameterList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 958
            self.typeParameter()
            self.state = 963
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Java20Parser.COMMA:
                self.state = 959
                self.match(Java20Parser.COMMA)
                self.state = 960
                self.typeParameter()
                self.state = 965
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassExtendsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EXTENDS(self):
            return self.getToken(Java20Parser.EXTENDS, 0)

        def classType(self):
            return self.getTypedRuleContext(Java20Parser.ClassTypeContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_classExtends

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassExtends" ):
                listener.enterClassExtends(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassExtends" ):
                listener.exitClassExtends(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassExtends" ):
                return visitor.visitClassExtends(self)
            else:
                return visitor.visitChildren(self)




    def classExtends(self):

        localctx = Java20Parser.ClassExtendsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_classExtends)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 966
            self.match(Java20Parser.EXTENDS)
            self.state = 967
            self.classType()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassImplementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IMPLEMENTS(self):
            return self.getToken(Java20Parser.IMPLEMENTS, 0)

        def interfaceTypeList(self):
            return self.getTypedRuleContext(Java20Parser.InterfaceTypeListContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_classImplements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassImplements" ):
                listener.enterClassImplements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassImplements" ):
                listener.exitClassImplements(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassImplements" ):
                return visitor.visitClassImplements(self)
            else:
                return visitor.visitChildren(self)




    def classImplements(self):

        localctx = Java20Parser.ClassImplementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_classImplements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 969
            self.match(Java20Parser.IMPLEMENTS)
            self.state = 970
            self.interfaceTypeList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfaceTypeListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def interfaceType(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.InterfaceTypeContext)
            else:
                return self.getTypedRuleContext(Java20Parser.InterfaceTypeContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(Java20Parser.COMMA)
            else:
                return self.getToken(Java20Parser.COMMA, i)

        def getRuleIndex(self):
            return Java20Parser.RULE_interfaceTypeList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterfaceTypeList" ):
                listener.enterInterfaceTypeList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterfaceTypeList" ):
                listener.exitInterfaceTypeList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfaceTypeList" ):
                return visitor.visitInterfaceTypeList(self)
            else:
                return visitor.visitChildren(self)




    def interfaceTypeList(self):

        localctx = Java20Parser.InterfaceTypeListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_interfaceTypeList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 972
            self.interfaceType()
            self.state = 977
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Java20Parser.COMMA:
                self.state = 973
                self.match(Java20Parser.COMMA)
                self.state = 974
                self.interfaceType()
                self.state = 979
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassPermitsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PERMITS(self):
            return self.getToken(Java20Parser.PERMITS, 0)

        def typeName(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.TypeNameContext)
            else:
                return self.getTypedRuleContext(Java20Parser.TypeNameContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(Java20Parser.COMMA)
            else:
                return self.getToken(Java20Parser.COMMA, i)

        def getRuleIndex(self):
            return Java20Parser.RULE_classPermits

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassPermits" ):
                listener.enterClassPermits(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassPermits" ):
                listener.exitClassPermits(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassPermits" ):
                return visitor.visitClassPermits(self)
            else:
                return visitor.visitChildren(self)




    def classPermits(self):

        localctx = Java20Parser.ClassPermitsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_classPermits)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 980
            self.match(Java20Parser.PERMITS)
            self.state = 981
            self.typeName()
            self.state = 986
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Java20Parser.COMMA:
                self.state = 982
                self.match(Java20Parser.COMMA)
                self.state = 983
                self.typeName()
                self.state = 988
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(Java20Parser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(Java20Parser.RBRACE, 0)

        def classBodyDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.ClassBodyDeclarationContext)
            else:
                return self.getTypedRuleContext(Java20Parser.ClassBodyDeclarationContext,i)


        def getRuleIndex(self):
            return Java20Parser.RULE_classBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassBody" ):
                listener.enterClassBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassBody" ):
                listener.exitClassBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassBody" ):
                return visitor.visitClassBody(self)
            else:
                return visitor.visitChildren(self)




    def classBody(self):

        localctx = Java20Parser.ClassBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_classBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 989
            self.match(Java20Parser.LBRACE)
            self.state = 993
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java20Parser.EXPORTS) | (1 << Java20Parser.MODULE) | (1 << Java20Parser.NONSEALED) | (1 << Java20Parser.OPEN) | (1 << Java20Parser.OPENS) | (1 << Java20Parser.PERMITS) | (1 << Java20Parser.PROVIDES) | (1 << Java20Parser.RECORD) | (1 << Java20Parser.REQUIRES) | (1 << Java20Parser.SEALED) | (1 << Java20Parser.TO) | (1 << Java20Parser.TRANSITIVE) | (1 << Java20Parser.USES) | (1 << Java20Parser.VAR) | (1 << Java20Parser.WITH) | (1 << Java20Parser.YIELD) | (1 << Java20Parser.ABSTRACT) | (1 << Java20Parser.BOOLEAN) | (1 << Java20Parser.BYTE) | (1 << Java20Parser.CHAR) | (1 << Java20Parser.CLASS) | (1 << Java20Parser.DOUBLE) | (1 << Java20Parser.ENUM) | (1 << Java20Parser.FINAL) | (1 << Java20Parser.FLOAT) | (1 << Java20Parser.INT) | (1 << Java20Parser.INTERFACE) | (1 << Java20Parser.LONG) | (1 << Java20Parser.NATIVE) | (1 << Java20Parser.PRIVATE) | (1 << Java20Parser.PROTECTED) | (1 << Java20Parser.PUBLIC) | (1 << Java20Parser.SHORT) | (1 << Java20Parser.STATIC) | (1 << Java20Parser.STRICTFP) | (1 << Java20Parser.SYNCHRONIZED) | (1 << Java20Parser.TRANSIENT))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (Java20Parser.VOID - 65)) | (1 << (Java20Parser.VOLATILE - 65)) | (1 << (Java20Parser.LBRACE - 65)) | (1 << (Java20Parser.SEMI - 65)) | (1 << (Java20Parser.AT - 65)) | (1 << (Java20Parser.LT - 65)) | (1 << (Java20Parser.Identifier - 65)))) != 0):
                self.state = 990
                self.classBodyDeclaration()
                self.state = 995
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 996
            self.match(Java20Parser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassBodyDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classMemberDeclaration(self):
            return self.getTypedRuleContext(Java20Parser.ClassMemberDeclarationContext,0)


        def instanceInitializer(self):
            return self.getTypedRuleContext(Java20Parser.InstanceInitializerContext,0)


        def staticInitializer(self):
            return self.getTypedRuleContext(Java20Parser.StaticInitializerContext,0)


        def constructorDeclaration(self):
            return self.getTypedRuleContext(Java20Parser.ConstructorDeclarationContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_classBodyDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassBodyDeclaration" ):
                listener.enterClassBodyDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassBodyDeclaration" ):
                listener.exitClassBodyDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassBodyDeclaration" ):
                return visitor.visitClassBodyDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def classBodyDeclaration(self):

        localctx = Java20Parser.ClassBodyDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_classBodyDeclaration)
        try:
            self.state = 1002
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,72,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 998
                self.classMemberDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 999
                self.instanceInitializer()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1000
                self.staticInitializer()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1001
                self.constructorDeclaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassMemberDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fieldDeclaration(self):
            return self.getTypedRuleContext(Java20Parser.FieldDeclarationContext,0)


        def methodDeclaration(self):
            return self.getTypedRuleContext(Java20Parser.MethodDeclarationContext,0)


        def classDeclaration(self):
            return self.getTypedRuleContext(Java20Parser.ClassDeclarationContext,0)


        def interfaceDeclaration(self):
            return self.getTypedRuleContext(Java20Parser.InterfaceDeclarationContext,0)


        def SEMI(self):
            return self.getToken(Java20Parser.SEMI, 0)

        def getRuleIndex(self):
            return Java20Parser.RULE_classMemberDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassMemberDeclaration" ):
                listener.enterClassMemberDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassMemberDeclaration" ):
                listener.exitClassMemberDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassMemberDeclaration" ):
                return visitor.visitClassMemberDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def classMemberDeclaration(self):

        localctx = Java20Parser.ClassMemberDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_classMemberDeclaration)
        try:
            self.state = 1009
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,73,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1004
                self.fieldDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1005
                self.methodDeclaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1006
                self.classDeclaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1007
                self.interfaceDeclaration()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1008
                self.match(Java20Parser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unannType(self):
            return self.getTypedRuleContext(Java20Parser.UnannTypeContext,0)


        def variableDeclaratorList(self):
            return self.getTypedRuleContext(Java20Parser.VariableDeclaratorListContext,0)


        def SEMI(self):
            return self.getToken(Java20Parser.SEMI, 0)

        def fieldModifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.FieldModifierContext)
            else:
                return self.getTypedRuleContext(Java20Parser.FieldModifierContext,i)


        def getRuleIndex(self):
            return Java20Parser.RULE_fieldDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFieldDeclaration" ):
                listener.enterFieldDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFieldDeclaration" ):
                listener.exitFieldDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFieldDeclaration" ):
                return visitor.visitFieldDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def fieldDeclaration(self):

        localctx = Java20Parser.FieldDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_fieldDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1014
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 35)) & ~0x3f) == 0 and ((1 << (_la - 35)) & ((1 << (Java20Parser.FINAL - 35)) | (1 << (Java20Parser.PRIVATE - 35)) | (1 << (Java20Parser.PROTECTED - 35)) | (1 << (Java20Parser.PUBLIC - 35)) | (1 << (Java20Parser.STATIC - 35)) | (1 << (Java20Parser.TRANSIENT - 35)) | (1 << (Java20Parser.VOLATILE - 35)) | (1 << (Java20Parser.AT - 35)))) != 0):
                self.state = 1011
                self.fieldModifier()
                self.state = 1016
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1017
            self.unannType()
            self.state = 1018
            self.variableDeclaratorList()
            self.state = 1019
            self.match(Java20Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldModifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def annotation(self):
            return self.getTypedRuleContext(Java20Parser.AnnotationContext,0)


        def PUBLIC(self):
            return self.getToken(Java20Parser.PUBLIC, 0)

        def PROTECTED(self):
            return self.getToken(Java20Parser.PROTECTED, 0)

        def PRIVATE(self):
            return self.getToken(Java20Parser.PRIVATE, 0)

        def STATIC(self):
            return self.getToken(Java20Parser.STATIC, 0)

        def FINAL(self):
            return self.getToken(Java20Parser.FINAL, 0)

        def TRANSIENT(self):
            return self.getToken(Java20Parser.TRANSIENT, 0)

        def VOLATILE(self):
            return self.getToken(Java20Parser.VOLATILE, 0)

        def getRuleIndex(self):
            return Java20Parser.RULE_fieldModifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFieldModifier" ):
                listener.enterFieldModifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFieldModifier" ):
                listener.exitFieldModifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFieldModifier" ):
                return visitor.visitFieldModifier(self)
            else:
                return visitor.visitChildren(self)




    def fieldModifier(self):

        localctx = Java20Parser.FieldModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_fieldModifier)
        try:
            self.state = 1029
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Java20Parser.AT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1021
                self.annotation()
                pass
            elif token in [Java20Parser.PUBLIC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1022
                self.match(Java20Parser.PUBLIC)
                pass
            elif token in [Java20Parser.PROTECTED]:
                self.enterOuterAlt(localctx, 3)
                self.state = 1023
                self.match(Java20Parser.PROTECTED)
                pass
            elif token in [Java20Parser.PRIVATE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 1024
                self.match(Java20Parser.PRIVATE)
                pass
            elif token in [Java20Parser.STATIC]:
                self.enterOuterAlt(localctx, 5)
                self.state = 1025
                self.match(Java20Parser.STATIC)
                pass
            elif token in [Java20Parser.FINAL]:
                self.enterOuterAlt(localctx, 6)
                self.state = 1026
                self.match(Java20Parser.FINAL)
                pass
            elif token in [Java20Parser.TRANSIENT]:
                self.enterOuterAlt(localctx, 7)
                self.state = 1027
                self.match(Java20Parser.TRANSIENT)
                pass
            elif token in [Java20Parser.VOLATILE]:
                self.enterOuterAlt(localctx, 8)
                self.state = 1028
                self.match(Java20Parser.VOLATILE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclaratorListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDeclarator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.VariableDeclaratorContext)
            else:
                return self.getTypedRuleContext(Java20Parser.VariableDeclaratorContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(Java20Parser.COMMA)
            else:
                return self.getToken(Java20Parser.COMMA, i)

        def getRuleIndex(self):
            return Java20Parser.RULE_variableDeclaratorList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDeclaratorList" ):
                listener.enterVariableDeclaratorList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDeclaratorList" ):
                listener.exitVariableDeclaratorList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableDeclaratorList" ):
                return visitor.visitVariableDeclaratorList(self)
            else:
                return visitor.visitChildren(self)




    def variableDeclaratorList(self):

        localctx = Java20Parser.VariableDeclaratorListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_variableDeclaratorList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1031
            self.variableDeclarator()
            self.state = 1036
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,76,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1032
                    self.match(Java20Parser.COMMA)
                    self.state = 1033
                    self.variableDeclarator() 
                self.state = 1038
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,76,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclaratorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDeclaratorId(self):
            return self.getTypedRuleContext(Java20Parser.VariableDeclaratorIdContext,0)


        def ASSIGN(self):
            return self.getToken(Java20Parser.ASSIGN, 0)

        def variableInitializer(self):
            return self.getTypedRuleContext(Java20Parser.VariableInitializerContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_variableDeclarator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDeclarator" ):
                listener.enterVariableDeclarator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDeclarator" ):
                listener.exitVariableDeclarator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableDeclarator" ):
                return visitor.visitVariableDeclarator(self)
            else:
                return visitor.visitChildren(self)




    def variableDeclarator(self):

        localctx = Java20Parser.VariableDeclaratorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_variableDeclarator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1039
            self.variableDeclaratorId()
            self.state = 1042
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,77,self._ctx)
            if la_ == 1:
                self.state = 1040
                self.match(Java20Parser.ASSIGN)
                self.state = 1041
                self.variableInitializer()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclaratorIdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(Java20Parser.IdentifierContext,0)


        def dims(self):
            return self.getTypedRuleContext(Java20Parser.DimsContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_variableDeclaratorId

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDeclaratorId" ):
                listener.enterVariableDeclaratorId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDeclaratorId" ):
                listener.exitVariableDeclaratorId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableDeclaratorId" ):
                return visitor.visitVariableDeclaratorId(self)
            else:
                return visitor.visitChildren(self)




    def variableDeclaratorId(self):

        localctx = Java20Parser.VariableDeclaratorIdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_variableDeclaratorId)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1044
            self.identifier()
            self.state = 1046
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,78,self._ctx)
            if la_ == 1:
                self.state = 1045
                self.dims()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableInitializerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(Java20Parser.ExpressionContext,0)


        def arrayInitializer(self):
            return self.getTypedRuleContext(Java20Parser.ArrayInitializerContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_variableInitializer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableInitializer" ):
                listener.enterVariableInitializer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableInitializer" ):
                listener.exitVariableInitializer(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableInitializer" ):
                return visitor.visitVariableInitializer(self)
            else:
                return visitor.visitChildren(self)




    def variableInitializer(self):

        localctx = Java20Parser.VariableInitializerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_variableInitializer)
        try:
            self.state = 1050
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Java20Parser.EXPORTS, Java20Parser.MODULE, Java20Parser.NONSEALED, Java20Parser.OPEN, Java20Parser.OPENS, Java20Parser.PERMITS, Java20Parser.PROVIDES, Java20Parser.RECORD, Java20Parser.REQUIRES, Java20Parser.SEALED, Java20Parser.TO, Java20Parser.TRANSITIVE, Java20Parser.USES, Java20Parser.VAR, Java20Parser.WITH, Java20Parser.YIELD, Java20Parser.BOOLEAN, Java20Parser.BYTE, Java20Parser.CHAR, Java20Parser.DOUBLE, Java20Parser.FLOAT, Java20Parser.INT, Java20Parser.LONG, Java20Parser.NEW, Java20Parser.SHORT, Java20Parser.SUPER, Java20Parser.SWITCH, Java20Parser.THIS, Java20Parser.VOID, Java20Parser.IntegerLiteral, Java20Parser.FloatingPointLiteral, Java20Parser.BooleanLiteral, Java20Parser.CharacterLiteral, Java20Parser.StringLiteral, Java20Parser.TextBlock, Java20Parser.NullLiteral, Java20Parser.LPAREN, Java20Parser.AT, Java20Parser.BANG, Java20Parser.TILDE, Java20Parser.INC, Java20Parser.DEC, Java20Parser.ADD, Java20Parser.SUB, Java20Parser.Identifier]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1048
                self.expression()
                pass
            elif token in [Java20Parser.LBRACE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1049
                self.arrayInitializer()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnannTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unannPrimitiveType(self):
            return self.getTypedRuleContext(Java20Parser.UnannPrimitiveTypeContext,0)


        def unannReferenceType(self):
            return self.getTypedRuleContext(Java20Parser.UnannReferenceTypeContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_unannType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnannType" ):
                listener.enterUnannType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnannType" ):
                listener.exitUnannType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnannType" ):
                return visitor.visitUnannType(self)
            else:
                return visitor.visitChildren(self)




    def unannType(self):

        localctx = Java20Parser.UnannTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_unannType)
        try:
            self.state = 1054
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,80,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1052
                self.unannPrimitiveType()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1053
                self.unannReferenceType()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnannPrimitiveTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def numericType(self):
            return self.getTypedRuleContext(Java20Parser.NumericTypeContext,0)


        def BOOLEAN(self):
            return self.getToken(Java20Parser.BOOLEAN, 0)

        def getRuleIndex(self):
            return Java20Parser.RULE_unannPrimitiveType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnannPrimitiveType" ):
                listener.enterUnannPrimitiveType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnannPrimitiveType" ):
                listener.exitUnannPrimitiveType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnannPrimitiveType" ):
                return visitor.visitUnannPrimitiveType(self)
            else:
                return visitor.visitChildren(self)




    def unannPrimitiveType(self):

        localctx = Java20Parser.UnannPrimitiveTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 138, self.RULE_unannPrimitiveType)
        try:
            self.state = 1058
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Java20Parser.BYTE, Java20Parser.CHAR, Java20Parser.DOUBLE, Java20Parser.FLOAT, Java20Parser.INT, Java20Parser.LONG, Java20Parser.SHORT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1056
                self.numericType()
                pass
            elif token in [Java20Parser.BOOLEAN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1057
                self.match(Java20Parser.BOOLEAN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnannReferenceTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unannClassOrInterfaceType(self):
            return self.getTypedRuleContext(Java20Parser.UnannClassOrInterfaceTypeContext,0)


        def unannTypeVariable(self):
            return self.getTypedRuleContext(Java20Parser.UnannTypeVariableContext,0)


        def unannArrayType(self):
            return self.getTypedRuleContext(Java20Parser.UnannArrayTypeContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_unannReferenceType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnannReferenceType" ):
                listener.enterUnannReferenceType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnannReferenceType" ):
                listener.exitUnannReferenceType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnannReferenceType" ):
                return visitor.visitUnannReferenceType(self)
            else:
                return visitor.visitChildren(self)




    def unannReferenceType(self):

        localctx = Java20Parser.UnannReferenceTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 140, self.RULE_unannReferenceType)
        try:
            self.state = 1063
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,82,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1060
                self.unannClassOrInterfaceType()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1061
                self.unannTypeVariable()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1062
                self.unannArrayType()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnannClassOrInterfaceTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeIdentifier(self):
            return self.getTypedRuleContext(Java20Parser.TypeIdentifierContext,0)


        def packageName(self):
            return self.getTypedRuleContext(Java20Parser.PackageNameContext,0)


        def DOT(self):
            return self.getToken(Java20Parser.DOT, 0)

        def typeArguments(self):
            return self.getTypedRuleContext(Java20Parser.TypeArgumentsContext,0)


        def uCOIT(self):
            return self.getTypedRuleContext(Java20Parser.UCOITContext,0)


        def annotation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.AnnotationContext)
            else:
                return self.getTypedRuleContext(Java20Parser.AnnotationContext,i)


        def getRuleIndex(self):
            return Java20Parser.RULE_unannClassOrInterfaceType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnannClassOrInterfaceType" ):
                listener.enterUnannClassOrInterfaceType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnannClassOrInterfaceType" ):
                listener.exitUnannClassOrInterfaceType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnannClassOrInterfaceType" ):
                return visitor.visitUnannClassOrInterfaceType(self)
            else:
                return visitor.visitChildren(self)




    def unannClassOrInterfaceType(self):

        localctx = Java20Parser.UnannClassOrInterfaceTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 142, self.RULE_unannClassOrInterfaceType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1073
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,84,self._ctx)
            if la_ == 1:
                self.state = 1065
                self.packageName()
                self.state = 1066
                self.match(Java20Parser.DOT)
                self.state = 1070
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==Java20Parser.AT:
                    self.state = 1067
                    self.annotation()
                    self.state = 1072
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 1075
            self.typeIdentifier()
            self.state = 1077
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Java20Parser.LT:
                self.state = 1076
                self.typeArguments()


            self.state = 1080
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,86,self._ctx)
            if la_ == 1:
                self.state = 1079
                self.uCOIT()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UCOITContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self):
            return self.getToken(Java20Parser.DOT, 0)

        def typeIdentifier(self):
            return self.getTypedRuleContext(Java20Parser.TypeIdentifierContext,0)


        def annotation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.AnnotationContext)
            else:
                return self.getTypedRuleContext(Java20Parser.AnnotationContext,i)


        def typeArguments(self):
            return self.getTypedRuleContext(Java20Parser.TypeArgumentsContext,0)


        def uCOIT(self):
            return self.getTypedRuleContext(Java20Parser.UCOITContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_uCOIT

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUCOIT" ):
                listener.enterUCOIT(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUCOIT" ):
                listener.exitUCOIT(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUCOIT" ):
                return visitor.visitUCOIT(self)
            else:
                return visitor.visitChildren(self)




    def uCOIT(self):

        localctx = Java20Parser.UCOITContext(self, self._ctx, self.state)
        self.enterRule(localctx, 144, self.RULE_uCOIT)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1082
            self.match(Java20Parser.DOT)
            self.state = 1086
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Java20Parser.AT:
                self.state = 1083
                self.annotation()
                self.state = 1088
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1089
            self.typeIdentifier()
            self.state = 1091
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Java20Parser.LT:
                self.state = 1090
                self.typeArguments()


            self.state = 1094
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,89,self._ctx)
            if la_ == 1:
                self.state = 1093
                self.uCOIT()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnannClassTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeIdentifier(self):
            return self.getTypedRuleContext(Java20Parser.TypeIdentifierContext,0)


        def typeArguments(self):
            return self.getTypedRuleContext(Java20Parser.TypeArgumentsContext,0)


        def DOT(self):
            return self.getToken(Java20Parser.DOT, 0)

        def packageName(self):
            return self.getTypedRuleContext(Java20Parser.PackageNameContext,0)


        def unannClassOrInterfaceType(self):
            return self.getTypedRuleContext(Java20Parser.UnannClassOrInterfaceTypeContext,0)


        def annotation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.AnnotationContext)
            else:
                return self.getTypedRuleContext(Java20Parser.AnnotationContext,i)


        def getRuleIndex(self):
            return Java20Parser.RULE_unannClassType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnannClassType" ):
                listener.enterUnannClassType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnannClassType" ):
                listener.exitUnannClassType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnannClassType" ):
                return visitor.visitUnannClassType(self)
            else:
                return visitor.visitChildren(self)




    def unannClassType(self):

        localctx = Java20Parser.UnannClassTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 146, self.RULE_unannClassType)
        self._la = 0 # Token type
        try:
            self.state = 1115
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,94,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1096
                self.typeIdentifier()
                self.state = 1098
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Java20Parser.LT:
                    self.state = 1097
                    self.typeArguments()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1102
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,91,self._ctx)
                if la_ == 1:
                    self.state = 1100
                    self.packageName()
                    pass

                elif la_ == 2:
                    self.state = 1101
                    self.unannClassOrInterfaceType()
                    pass


                self.state = 1104
                self.match(Java20Parser.DOT)
                self.state = 1108
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==Java20Parser.AT:
                    self.state = 1105
                    self.annotation()
                    self.state = 1110
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 1111
                self.typeIdentifier()
                self.state = 1113
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Java20Parser.LT:
                    self.state = 1112
                    self.typeArguments()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnannInterfaceTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unannClassType(self):
            return self.getTypedRuleContext(Java20Parser.UnannClassTypeContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_unannInterfaceType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnannInterfaceType" ):
                listener.enterUnannInterfaceType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnannInterfaceType" ):
                listener.exitUnannInterfaceType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnannInterfaceType" ):
                return visitor.visitUnannInterfaceType(self)
            else:
                return visitor.visitChildren(self)




    def unannInterfaceType(self):

        localctx = Java20Parser.UnannInterfaceTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 148, self.RULE_unannInterfaceType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1117
            self.unannClassType()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnannTypeVariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeIdentifier(self):
            return self.getTypedRuleContext(Java20Parser.TypeIdentifierContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_unannTypeVariable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnannTypeVariable" ):
                listener.enterUnannTypeVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnannTypeVariable" ):
                listener.exitUnannTypeVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnannTypeVariable" ):
                return visitor.visitUnannTypeVariable(self)
            else:
                return visitor.visitChildren(self)




    def unannTypeVariable(self):

        localctx = Java20Parser.UnannTypeVariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 150, self.RULE_unannTypeVariable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1119
            self.typeIdentifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnannArrayTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dims(self):
            return self.getTypedRuleContext(Java20Parser.DimsContext,0)


        def unannPrimitiveType(self):
            return self.getTypedRuleContext(Java20Parser.UnannPrimitiveTypeContext,0)


        def unannClassOrInterfaceType(self):
            return self.getTypedRuleContext(Java20Parser.UnannClassOrInterfaceTypeContext,0)


        def unannTypeVariable(self):
            return self.getTypedRuleContext(Java20Parser.UnannTypeVariableContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_unannArrayType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnannArrayType" ):
                listener.enterUnannArrayType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnannArrayType" ):
                listener.exitUnannArrayType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnannArrayType" ):
                return visitor.visitUnannArrayType(self)
            else:
                return visitor.visitChildren(self)




    def unannArrayType(self):

        localctx = Java20Parser.UnannArrayTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 152, self.RULE_unannArrayType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1124
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,95,self._ctx)
            if la_ == 1:
                self.state = 1121
                self.unannPrimitiveType()
                pass

            elif la_ == 2:
                self.state = 1122
                self.unannClassOrInterfaceType()
                pass

            elif la_ == 3:
                self.state = 1123
                self.unannTypeVariable()
                pass


            self.state = 1126
            self.dims()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def methodHeader(self):
            return self.getTypedRuleContext(Java20Parser.MethodHeaderContext,0)


        def methodBody(self):
            return self.getTypedRuleContext(Java20Parser.MethodBodyContext,0)


        def methodModifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.MethodModifierContext)
            else:
                return self.getTypedRuleContext(Java20Parser.MethodModifierContext,i)


        def getRuleIndex(self):
            return Java20Parser.RULE_methodDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodDeclaration" ):
                listener.enterMethodDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodDeclaration" ):
                listener.exitMethodDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodDeclaration" ):
                return visitor.visitMethodDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def methodDeclaration(self):

        localctx = Java20Parser.MethodDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 154, self.RULE_methodDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java20Parser.ABSTRACT) | (1 << Java20Parser.FINAL) | (1 << Java20Parser.NATIVE) | (1 << Java20Parser.PRIVATE) | (1 << Java20Parser.PROTECTED) | (1 << Java20Parser.PUBLIC) | (1 << Java20Parser.STATIC) | (1 << Java20Parser.STRICTFP) | (1 << Java20Parser.SYNCHRONIZED))) != 0) or _la==Java20Parser.AT:
                self.state = 1128
                self.methodModifier()
                self.state = 1133
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1134
            self.methodHeader()
            self.state = 1135
            self.methodBody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodModifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def annotation(self):
            return self.getTypedRuleContext(Java20Parser.AnnotationContext,0)


        def PUBLIC(self):
            return self.getToken(Java20Parser.PUBLIC, 0)

        def PROTECTED(self):
            return self.getToken(Java20Parser.PROTECTED, 0)

        def PRIVATE(self):
            return self.getToken(Java20Parser.PRIVATE, 0)

        def ABSTRACT(self):
            return self.getToken(Java20Parser.ABSTRACT, 0)

        def STATIC(self):
            return self.getToken(Java20Parser.STATIC, 0)

        def FINAL(self):
            return self.getToken(Java20Parser.FINAL, 0)

        def SYNCHRONIZED(self):
            return self.getToken(Java20Parser.SYNCHRONIZED, 0)

        def NATIVE(self):
            return self.getToken(Java20Parser.NATIVE, 0)

        def STRICTFP(self):
            return self.getToken(Java20Parser.STRICTFP, 0)

        def getRuleIndex(self):
            return Java20Parser.RULE_methodModifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodModifier" ):
                listener.enterMethodModifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodModifier" ):
                listener.exitMethodModifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodModifier" ):
                return visitor.visitMethodModifier(self)
            else:
                return visitor.visitChildren(self)




    def methodModifier(self):

        localctx = Java20Parser.MethodModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 156, self.RULE_methodModifier)
        try:
            self.state = 1147
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Java20Parser.AT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1137
                self.annotation()
                pass
            elif token in [Java20Parser.PUBLIC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1138
                self.match(Java20Parser.PUBLIC)
                pass
            elif token in [Java20Parser.PROTECTED]:
                self.enterOuterAlt(localctx, 3)
                self.state = 1139
                self.match(Java20Parser.PROTECTED)
                pass
            elif token in [Java20Parser.PRIVATE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 1140
                self.match(Java20Parser.PRIVATE)
                pass
            elif token in [Java20Parser.ABSTRACT]:
                self.enterOuterAlt(localctx, 5)
                self.state = 1141
                self.match(Java20Parser.ABSTRACT)
                pass
            elif token in [Java20Parser.STATIC]:
                self.enterOuterAlt(localctx, 6)
                self.state = 1142
                self.match(Java20Parser.STATIC)
                pass
            elif token in [Java20Parser.FINAL]:
                self.enterOuterAlt(localctx, 7)
                self.state = 1143
                self.match(Java20Parser.FINAL)
                pass
            elif token in [Java20Parser.SYNCHRONIZED]:
                self.enterOuterAlt(localctx, 8)
                self.state = 1144
                self.match(Java20Parser.SYNCHRONIZED)
                pass
            elif token in [Java20Parser.NATIVE]:
                self.enterOuterAlt(localctx, 9)
                self.state = 1145
                self.match(Java20Parser.NATIVE)
                pass
            elif token in [Java20Parser.STRICTFP]:
                self.enterOuterAlt(localctx, 10)
                self.state = 1146
                self.match(Java20Parser.STRICTFP)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodHeaderContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def result(self):
            return self.getTypedRuleContext(Java20Parser.ResultContext,0)


        def methodDeclarator(self):
            return self.getTypedRuleContext(Java20Parser.MethodDeclaratorContext,0)


        def typeParameters(self):
            return self.getTypedRuleContext(Java20Parser.TypeParametersContext,0)


        def throwsT(self):
            return self.getTypedRuleContext(Java20Parser.ThrowsTContext,0)


        def annotation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.AnnotationContext)
            else:
                return self.getTypedRuleContext(Java20Parser.AnnotationContext,i)


        def getRuleIndex(self):
            return Java20Parser.RULE_methodHeader

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodHeader" ):
                listener.enterMethodHeader(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodHeader" ):
                listener.exitMethodHeader(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodHeader" ):
                return visitor.visitMethodHeader(self)
            else:
                return visitor.visitChildren(self)




    def methodHeader(self):

        localctx = Java20Parser.MethodHeaderContext(self, self._ctx, self.state)
        self.enterRule(localctx, 158, self.RULE_methodHeader)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1156
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Java20Parser.LT:
                self.state = 1149
                self.typeParameters()
                self.state = 1153
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==Java20Parser.AT:
                    self.state = 1150
                    self.annotation()
                    self.state = 1155
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 1158
            self.result()
            self.state = 1159
            self.methodDeclarator()
            self.state = 1161
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Java20Parser.THROWS:
                self.state = 1160
                self.throwsT()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ResultContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unannType(self):
            return self.getTypedRuleContext(Java20Parser.UnannTypeContext,0)


        def VOID(self):
            return self.getToken(Java20Parser.VOID, 0)

        def getRuleIndex(self):
            return Java20Parser.RULE_result

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterResult" ):
                listener.enterResult(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitResult" ):
                listener.exitResult(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitResult" ):
                return visitor.visitResult(self)
            else:
                return visitor.visitChildren(self)




    def result(self):

        localctx = Java20Parser.ResultContext(self, self._ctx, self.state)
        self.enterRule(localctx, 160, self.RULE_result)
        try:
            self.state = 1165
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Java20Parser.EXPORTS, Java20Parser.MODULE, Java20Parser.NONSEALED, Java20Parser.OPEN, Java20Parser.OPENS, Java20Parser.PERMITS, Java20Parser.PROVIDES, Java20Parser.RECORD, Java20Parser.REQUIRES, Java20Parser.SEALED, Java20Parser.TO, Java20Parser.TRANSITIVE, Java20Parser.USES, Java20Parser.VAR, Java20Parser.WITH, Java20Parser.YIELD, Java20Parser.BOOLEAN, Java20Parser.BYTE, Java20Parser.CHAR, Java20Parser.DOUBLE, Java20Parser.FLOAT, Java20Parser.INT, Java20Parser.LONG, Java20Parser.SHORT, Java20Parser.Identifier]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1163
                self.unannType()
                pass
            elif token in [Java20Parser.VOID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1164
                self.match(Java20Parser.VOID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodDeclaratorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(Java20Parser.IdentifierContext,0)


        def LPAREN(self):
            return self.getToken(Java20Parser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(Java20Parser.RPAREN, 0)

        def receiverParameter(self):
            return self.getTypedRuleContext(Java20Parser.ReceiverParameterContext,0)


        def COMMA(self):
            return self.getToken(Java20Parser.COMMA, 0)

        def formalParameterList(self):
            return self.getTypedRuleContext(Java20Parser.FormalParameterListContext,0)


        def dims(self):
            return self.getTypedRuleContext(Java20Parser.DimsContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_methodDeclarator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodDeclarator" ):
                listener.enterMethodDeclarator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodDeclarator" ):
                listener.exitMethodDeclarator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodDeclarator" ):
                return visitor.visitMethodDeclarator(self)
            else:
                return visitor.visitChildren(self)




    def methodDeclarator(self):

        localctx = Java20Parser.MethodDeclaratorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 162, self.RULE_methodDeclarator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1167
            self.identifier()
            self.state = 1168
            self.match(Java20Parser.LPAREN)
            self.state = 1172
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,102,self._ctx)
            if la_ == 1:
                self.state = 1169
                self.receiverParameter()
                self.state = 1170
                self.match(Java20Parser.COMMA)


            self.state = 1175
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java20Parser.EXPORTS) | (1 << Java20Parser.MODULE) | (1 << Java20Parser.NONSEALED) | (1 << Java20Parser.OPEN) | (1 << Java20Parser.OPENS) | (1 << Java20Parser.PERMITS) | (1 << Java20Parser.PROVIDES) | (1 << Java20Parser.RECORD) | (1 << Java20Parser.REQUIRES) | (1 << Java20Parser.SEALED) | (1 << Java20Parser.TO) | (1 << Java20Parser.TRANSITIVE) | (1 << Java20Parser.USES) | (1 << Java20Parser.VAR) | (1 << Java20Parser.WITH) | (1 << Java20Parser.YIELD) | (1 << Java20Parser.BOOLEAN) | (1 << Java20Parser.BYTE) | (1 << Java20Parser.CHAR) | (1 << Java20Parser.DOUBLE) | (1 << Java20Parser.FINAL) | (1 << Java20Parser.FLOAT) | (1 << Java20Parser.INT) | (1 << Java20Parser.LONG) | (1 << Java20Parser.SHORT))) != 0) or _la==Java20Parser.AT or _la==Java20Parser.Identifier:
                self.state = 1174
                self.formalParameterList()


            self.state = 1177
            self.match(Java20Parser.RPAREN)
            self.state = 1179
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Java20Parser.LBRACK or _la==Java20Parser.AT:
                self.state = 1178
                self.dims()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReceiverParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unannType(self):
            return self.getTypedRuleContext(Java20Parser.UnannTypeContext,0)


        def THIS(self):
            return self.getToken(Java20Parser.THIS, 0)

        def annotation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.AnnotationContext)
            else:
                return self.getTypedRuleContext(Java20Parser.AnnotationContext,i)


        def identifier(self):
            return self.getTypedRuleContext(Java20Parser.IdentifierContext,0)


        def DOT(self):
            return self.getToken(Java20Parser.DOT, 0)

        def getRuleIndex(self):
            return Java20Parser.RULE_receiverParameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReceiverParameter" ):
                listener.enterReceiverParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReceiverParameter" ):
                listener.exitReceiverParameter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReceiverParameter" ):
                return visitor.visitReceiverParameter(self)
            else:
                return visitor.visitChildren(self)




    def receiverParameter(self):

        localctx = Java20Parser.ReceiverParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 164, self.RULE_receiverParameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1184
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Java20Parser.AT:
                self.state = 1181
                self.annotation()
                self.state = 1186
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1187
            self.unannType()
            self.state = 1191
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java20Parser.EXPORTS) | (1 << Java20Parser.MODULE) | (1 << Java20Parser.NONSEALED) | (1 << Java20Parser.OPEN) | (1 << Java20Parser.OPENS) | (1 << Java20Parser.PERMITS) | (1 << Java20Parser.PROVIDES) | (1 << Java20Parser.RECORD) | (1 << Java20Parser.REQUIRES) | (1 << Java20Parser.SEALED) | (1 << Java20Parser.TO) | (1 << Java20Parser.TRANSITIVE) | (1 << Java20Parser.USES) | (1 << Java20Parser.VAR) | (1 << Java20Parser.WITH) | (1 << Java20Parser.YIELD))) != 0) or _la==Java20Parser.Identifier:
                self.state = 1188
                self.identifier()
                self.state = 1189
                self.match(Java20Parser.DOT)


            self.state = 1193
            self.match(Java20Parser.THIS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FormalParameterListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def formalParameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.FormalParameterContext)
            else:
                return self.getTypedRuleContext(Java20Parser.FormalParameterContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(Java20Parser.COMMA)
            else:
                return self.getToken(Java20Parser.COMMA, i)

        def getRuleIndex(self):
            return Java20Parser.RULE_formalParameterList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormalParameterList" ):
                listener.enterFormalParameterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormalParameterList" ):
                listener.exitFormalParameterList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFormalParameterList" ):
                return visitor.visitFormalParameterList(self)
            else:
                return visitor.visitChildren(self)




    def formalParameterList(self):

        localctx = Java20Parser.FormalParameterListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 166, self.RULE_formalParameterList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1195
            self.formalParameter()
            self.state = 1200
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Java20Parser.COMMA:
                self.state = 1196
                self.match(Java20Parser.COMMA)
                self.state = 1197
                self.formalParameter()
                self.state = 1202
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FormalParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unannType(self):
            return self.getTypedRuleContext(Java20Parser.UnannTypeContext,0)


        def variableDeclaratorId(self):
            return self.getTypedRuleContext(Java20Parser.VariableDeclaratorIdContext,0)


        def variableModifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.VariableModifierContext)
            else:
                return self.getTypedRuleContext(Java20Parser.VariableModifierContext,i)


        def variableArityParameter(self):
            return self.getTypedRuleContext(Java20Parser.VariableArityParameterContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_formalParameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormalParameter" ):
                listener.enterFormalParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormalParameter" ):
                listener.exitFormalParameter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFormalParameter" ):
                return visitor.visitFormalParameter(self)
            else:
                return visitor.visitChildren(self)




    def formalParameter(self):

        localctx = Java20Parser.FormalParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 168, self.RULE_formalParameter)
        self._la = 0 # Token type
        try:
            self.state = 1213
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,109,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1206
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==Java20Parser.FINAL or _la==Java20Parser.AT:
                    self.state = 1203
                    self.variableModifier()
                    self.state = 1208
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 1209
                self.unannType()
                self.state = 1210
                self.variableDeclaratorId()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1212
                self.variableArityParameter()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableArityParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unannType(self):
            return self.getTypedRuleContext(Java20Parser.UnannTypeContext,0)


        def ELLIPSIS(self):
            return self.getToken(Java20Parser.ELLIPSIS, 0)

        def identifier(self):
            return self.getTypedRuleContext(Java20Parser.IdentifierContext,0)


        def variableModifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.VariableModifierContext)
            else:
                return self.getTypedRuleContext(Java20Parser.VariableModifierContext,i)


        def annotation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.AnnotationContext)
            else:
                return self.getTypedRuleContext(Java20Parser.AnnotationContext,i)


        def getRuleIndex(self):
            return Java20Parser.RULE_variableArityParameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableArityParameter" ):
                listener.enterVariableArityParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableArityParameter" ):
                listener.exitVariableArityParameter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableArityParameter" ):
                return visitor.visitVariableArityParameter(self)
            else:
                return visitor.visitChildren(self)




    def variableArityParameter(self):

        localctx = Java20Parser.VariableArityParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 170, self.RULE_variableArityParameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1218
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Java20Parser.FINAL or _la==Java20Parser.AT:
                self.state = 1215
                self.variableModifier()
                self.state = 1220
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1221
            self.unannType()
            self.state = 1225
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Java20Parser.AT:
                self.state = 1222
                self.annotation()
                self.state = 1227
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1228
            self.match(Java20Parser.ELLIPSIS)
            self.state = 1229
            self.identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableModifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def annotation(self):
            return self.getTypedRuleContext(Java20Parser.AnnotationContext,0)


        def FINAL(self):
            return self.getToken(Java20Parser.FINAL, 0)

        def getRuleIndex(self):
            return Java20Parser.RULE_variableModifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableModifier" ):
                listener.enterVariableModifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableModifier" ):
                listener.exitVariableModifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableModifier" ):
                return visitor.visitVariableModifier(self)
            else:
                return visitor.visitChildren(self)




    def variableModifier(self):

        localctx = Java20Parser.VariableModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 172, self.RULE_variableModifier)
        try:
            self.state = 1233
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Java20Parser.AT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1231
                self.annotation()
                pass
            elif token in [Java20Parser.FINAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1232
                self.match(Java20Parser.FINAL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ThrowsTContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def THROWS(self):
            return self.getToken(Java20Parser.THROWS, 0)

        def exceptionTypeList(self):
            return self.getTypedRuleContext(Java20Parser.ExceptionTypeListContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_throwsT

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterThrowsT" ):
                listener.enterThrowsT(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitThrowsT" ):
                listener.exitThrowsT(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitThrowsT" ):
                return visitor.visitThrowsT(self)
            else:
                return visitor.visitChildren(self)




    def throwsT(self):

        localctx = Java20Parser.ThrowsTContext(self, self._ctx, self.state)
        self.enterRule(localctx, 174, self.RULE_throwsT)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1235
            self.match(Java20Parser.THROWS)
            self.state = 1236
            self.exceptionTypeList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExceptionTypeListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exceptionType(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.ExceptionTypeContext)
            else:
                return self.getTypedRuleContext(Java20Parser.ExceptionTypeContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(Java20Parser.COMMA)
            else:
                return self.getToken(Java20Parser.COMMA, i)

        def getRuleIndex(self):
            return Java20Parser.RULE_exceptionTypeList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExceptionTypeList" ):
                listener.enterExceptionTypeList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExceptionTypeList" ):
                listener.exitExceptionTypeList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExceptionTypeList" ):
                return visitor.visitExceptionTypeList(self)
            else:
                return visitor.visitChildren(self)




    def exceptionTypeList(self):

        localctx = Java20Parser.ExceptionTypeListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 176, self.RULE_exceptionTypeList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1238
            self.exceptionType()
            self.state = 1243
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Java20Parser.COMMA:
                self.state = 1239
                self.match(Java20Parser.COMMA)
                self.state = 1240
                self.exceptionType()
                self.state = 1245
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExceptionTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classType(self):
            return self.getTypedRuleContext(Java20Parser.ClassTypeContext,0)


        def typeVariable(self):
            return self.getTypedRuleContext(Java20Parser.TypeVariableContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_exceptionType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExceptionType" ):
                listener.enterExceptionType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExceptionType" ):
                listener.exitExceptionType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExceptionType" ):
                return visitor.visitExceptionType(self)
            else:
                return visitor.visitChildren(self)




    def exceptionType(self):

        localctx = Java20Parser.ExceptionTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 178, self.RULE_exceptionType)
        try:
            self.state = 1248
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,114,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1246
                self.classType()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1247
                self.typeVariable()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(Java20Parser.BlockContext,0)


        def SEMI(self):
            return self.getToken(Java20Parser.SEMI, 0)

        def getRuleIndex(self):
            return Java20Parser.RULE_methodBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodBody" ):
                listener.enterMethodBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodBody" ):
                listener.exitMethodBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodBody" ):
                return visitor.visitMethodBody(self)
            else:
                return visitor.visitChildren(self)




    def methodBody(self):

        localctx = Java20Parser.MethodBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 180, self.RULE_methodBody)
        try:
            self.state = 1252
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Java20Parser.LBRACE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1250
                self.block()
                pass
            elif token in [Java20Parser.SEMI]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1251
                self.match(Java20Parser.SEMI)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstanceInitializerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(Java20Parser.BlockContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_instanceInitializer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstanceInitializer" ):
                listener.enterInstanceInitializer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstanceInitializer" ):
                listener.exitInstanceInitializer(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstanceInitializer" ):
                return visitor.visitInstanceInitializer(self)
            else:
                return visitor.visitChildren(self)




    def instanceInitializer(self):

        localctx = Java20Parser.InstanceInitializerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 182, self.RULE_instanceInitializer)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1254
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StaticInitializerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STATIC(self):
            return self.getToken(Java20Parser.STATIC, 0)

        def block(self):
            return self.getTypedRuleContext(Java20Parser.BlockContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_staticInitializer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStaticInitializer" ):
                listener.enterStaticInitializer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStaticInitializer" ):
                listener.exitStaticInitializer(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStaticInitializer" ):
                return visitor.visitStaticInitializer(self)
            else:
                return visitor.visitChildren(self)




    def staticInitializer(self):

        localctx = Java20Parser.StaticInitializerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 184, self.RULE_staticInitializer)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1256
            self.match(Java20Parser.STATIC)
            self.state = 1257
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstructorDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def constructorDeclarator(self):
            return self.getTypedRuleContext(Java20Parser.ConstructorDeclaratorContext,0)


        def constructorBody(self):
            return self.getTypedRuleContext(Java20Parser.ConstructorBodyContext,0)


        def constructorModifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.ConstructorModifierContext)
            else:
                return self.getTypedRuleContext(Java20Parser.ConstructorModifierContext,i)


        def throwsT(self):
            return self.getTypedRuleContext(Java20Parser.ThrowsTContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_constructorDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstructorDeclaration" ):
                listener.enterConstructorDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstructorDeclaration" ):
                listener.exitConstructorDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstructorDeclaration" ):
                return visitor.visitConstructorDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def constructorDeclaration(self):

        localctx = Java20Parser.ConstructorDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 186, self.RULE_constructorDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1262
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 50)) & ~0x3f) == 0 and ((1 << (_la - 50)) & ((1 << (Java20Parser.PRIVATE - 50)) | (1 << (Java20Parser.PROTECTED - 50)) | (1 << (Java20Parser.PUBLIC - 50)) | (1 << (Java20Parser.AT - 50)))) != 0):
                self.state = 1259
                self.constructorModifier()
                self.state = 1264
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1265
            self.constructorDeclarator()
            self.state = 1267
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Java20Parser.THROWS:
                self.state = 1266
                self.throwsT()


            self.state = 1269
            self.constructorBody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstructorModifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def annotation(self):
            return self.getTypedRuleContext(Java20Parser.AnnotationContext,0)


        def PUBLIC(self):
            return self.getToken(Java20Parser.PUBLIC, 0)

        def PROTECTED(self):
            return self.getToken(Java20Parser.PROTECTED, 0)

        def PRIVATE(self):
            return self.getToken(Java20Parser.PRIVATE, 0)

        def getRuleIndex(self):
            return Java20Parser.RULE_constructorModifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstructorModifier" ):
                listener.enterConstructorModifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstructorModifier" ):
                listener.exitConstructorModifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstructorModifier" ):
                return visitor.visitConstructorModifier(self)
            else:
                return visitor.visitChildren(self)




    def constructorModifier(self):

        localctx = Java20Parser.ConstructorModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 188, self.RULE_constructorModifier)
        try:
            self.state = 1275
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Java20Parser.AT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1271
                self.annotation()
                pass
            elif token in [Java20Parser.PUBLIC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1272
                self.match(Java20Parser.PUBLIC)
                pass
            elif token in [Java20Parser.PROTECTED]:
                self.enterOuterAlt(localctx, 3)
                self.state = 1273
                self.match(Java20Parser.PROTECTED)
                pass
            elif token in [Java20Parser.PRIVATE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 1274
                self.match(Java20Parser.PRIVATE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstructorDeclaratorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simpleTypeName(self):
            return self.getTypedRuleContext(Java20Parser.SimpleTypeNameContext,0)


        def LPAREN(self):
            return self.getToken(Java20Parser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(Java20Parser.RPAREN, 0)

        def typeParameters(self):
            return self.getTypedRuleContext(Java20Parser.TypeParametersContext,0)


        def receiverParameter(self):
            return self.getTypedRuleContext(Java20Parser.ReceiverParameterContext,0)


        def COMMA(self):
            return self.getToken(Java20Parser.COMMA, 0)

        def formalParameterList(self):
            return self.getTypedRuleContext(Java20Parser.FormalParameterListContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_constructorDeclarator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstructorDeclarator" ):
                listener.enterConstructorDeclarator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstructorDeclarator" ):
                listener.exitConstructorDeclarator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstructorDeclarator" ):
                return visitor.visitConstructorDeclarator(self)
            else:
                return visitor.visitChildren(self)




    def constructorDeclarator(self):

        localctx = Java20Parser.ConstructorDeclaratorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 190, self.RULE_constructorDeclarator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1278
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Java20Parser.LT:
                self.state = 1277
                self.typeParameters()


            self.state = 1280
            self.simpleTypeName()
            self.state = 1281
            self.match(Java20Parser.LPAREN)
            self.state = 1285
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,120,self._ctx)
            if la_ == 1:
                self.state = 1282
                self.receiverParameter()
                self.state = 1283
                self.match(Java20Parser.COMMA)


            self.state = 1288
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java20Parser.EXPORTS) | (1 << Java20Parser.MODULE) | (1 << Java20Parser.NONSEALED) | (1 << Java20Parser.OPEN) | (1 << Java20Parser.OPENS) | (1 << Java20Parser.PERMITS) | (1 << Java20Parser.PROVIDES) | (1 << Java20Parser.RECORD) | (1 << Java20Parser.REQUIRES) | (1 << Java20Parser.SEALED) | (1 << Java20Parser.TO) | (1 << Java20Parser.TRANSITIVE) | (1 << Java20Parser.USES) | (1 << Java20Parser.VAR) | (1 << Java20Parser.WITH) | (1 << Java20Parser.YIELD) | (1 << Java20Parser.BOOLEAN) | (1 << Java20Parser.BYTE) | (1 << Java20Parser.CHAR) | (1 << Java20Parser.DOUBLE) | (1 << Java20Parser.FINAL) | (1 << Java20Parser.FLOAT) | (1 << Java20Parser.INT) | (1 << Java20Parser.LONG) | (1 << Java20Parser.SHORT))) != 0) or _la==Java20Parser.AT or _la==Java20Parser.Identifier:
                self.state = 1287
                self.formalParameterList()


            self.state = 1290
            self.match(Java20Parser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SimpleTypeNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeIdentifier(self):
            return self.getTypedRuleContext(Java20Parser.TypeIdentifierContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_simpleTypeName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimpleTypeName" ):
                listener.enterSimpleTypeName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimpleTypeName" ):
                listener.exitSimpleTypeName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimpleTypeName" ):
                return visitor.visitSimpleTypeName(self)
            else:
                return visitor.visitChildren(self)




    def simpleTypeName(self):

        localctx = Java20Parser.SimpleTypeNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 192, self.RULE_simpleTypeName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1292
            self.typeIdentifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstructorBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(Java20Parser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(Java20Parser.RBRACE, 0)

        def explicitConstructorInvocation(self):
            return self.getTypedRuleContext(Java20Parser.ExplicitConstructorInvocationContext,0)


        def blockStatements(self):
            return self.getTypedRuleContext(Java20Parser.BlockStatementsContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_constructorBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstructorBody" ):
                listener.enterConstructorBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstructorBody" ):
                listener.exitConstructorBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstructorBody" ):
                return visitor.visitConstructorBody(self)
            else:
                return visitor.visitChildren(self)




    def constructorBody(self):

        localctx = Java20Parser.ConstructorBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 194, self.RULE_constructorBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1294
            self.match(Java20Parser.LBRACE)
            self.state = 1296
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,122,self._ctx)
            if la_ == 1:
                self.state = 1295
                self.explicitConstructorInvocation()


            self.state = 1299
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java20Parser.EXPORTS) | (1 << Java20Parser.MODULE) | (1 << Java20Parser.NONSEALED) | (1 << Java20Parser.OPEN) | (1 << Java20Parser.OPENS) | (1 << Java20Parser.PERMITS) | (1 << Java20Parser.PROVIDES) | (1 << Java20Parser.RECORD) | (1 << Java20Parser.REQUIRES) | (1 << Java20Parser.SEALED) | (1 << Java20Parser.TO) | (1 << Java20Parser.TRANSITIVE) | (1 << Java20Parser.USES) | (1 << Java20Parser.VAR) | (1 << Java20Parser.WITH) | (1 << Java20Parser.YIELD) | (1 << Java20Parser.ABSTRACT) | (1 << Java20Parser.ASSERT) | (1 << Java20Parser.BOOLEAN) | (1 << Java20Parser.BREAK) | (1 << Java20Parser.BYTE) | (1 << Java20Parser.CHAR) | (1 << Java20Parser.CLASS) | (1 << Java20Parser.CONTINUE) | (1 << Java20Parser.DO) | (1 << Java20Parser.DOUBLE) | (1 << Java20Parser.ENUM) | (1 << Java20Parser.FINAL) | (1 << Java20Parser.FLOAT) | (1 << Java20Parser.FOR) | (1 << Java20Parser.IF) | (1 << Java20Parser.INT) | (1 << Java20Parser.INTERFACE) | (1 << Java20Parser.LONG) | (1 << Java20Parser.NEW) | (1 << Java20Parser.PRIVATE) | (1 << Java20Parser.PROTECTED) | (1 << Java20Parser.PUBLIC) | (1 << Java20Parser.RETURN) | (1 << Java20Parser.SHORT) | (1 << Java20Parser.STATIC) | (1 << Java20Parser.STRICTFP) | (1 << Java20Parser.SUPER) | (1 << Java20Parser.SWITCH) | (1 << Java20Parser.SYNCHRONIZED) | (1 << Java20Parser.THIS) | (1 << Java20Parser.THROW))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (Java20Parser.TRY - 64)) | (1 << (Java20Parser.VOID - 64)) | (1 << (Java20Parser.WHILE - 64)) | (1 << (Java20Parser.IntegerLiteral - 64)) | (1 << (Java20Parser.FloatingPointLiteral - 64)) | (1 << (Java20Parser.BooleanLiteral - 64)) | (1 << (Java20Parser.CharacterLiteral - 64)) | (1 << (Java20Parser.StringLiteral - 64)) | (1 << (Java20Parser.TextBlock - 64)) | (1 << (Java20Parser.NullLiteral - 64)) | (1 << (Java20Parser.LPAREN - 64)) | (1 << (Java20Parser.LBRACE - 64)) | (1 << (Java20Parser.SEMI - 64)) | (1 << (Java20Parser.AT - 64)) | (1 << (Java20Parser.INC - 64)) | (1 << (Java20Parser.DEC - 64)) | (1 << (Java20Parser.Identifier - 64)))) != 0):
                self.state = 1298
                self.blockStatements()


            self.state = 1301
            self.match(Java20Parser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExplicitConstructorInvocationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(Java20Parser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(Java20Parser.RPAREN, 0)

        def SEMI(self):
            return self.getToken(Java20Parser.SEMI, 0)

        def THIS(self):
            return self.getToken(Java20Parser.THIS, 0)

        def SUPER(self):
            return self.getToken(Java20Parser.SUPER, 0)

        def typeArguments(self):
            return self.getTypedRuleContext(Java20Parser.TypeArgumentsContext,0)


        def argumentList(self):
            return self.getTypedRuleContext(Java20Parser.ArgumentListContext,0)


        def DOT(self):
            return self.getToken(Java20Parser.DOT, 0)

        def expressionName(self):
            return self.getTypedRuleContext(Java20Parser.ExpressionNameContext,0)


        def primary(self):
            return self.getTypedRuleContext(Java20Parser.PrimaryContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_explicitConstructorInvocation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExplicitConstructorInvocation" ):
                listener.enterExplicitConstructorInvocation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExplicitConstructorInvocation" ):
                listener.exitExplicitConstructorInvocation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExplicitConstructorInvocation" ):
                return visitor.visitExplicitConstructorInvocation(self)
            else:
                return visitor.visitChildren(self)




    def explicitConstructorInvocation(self):

        localctx = Java20Parser.ExplicitConstructorInvocationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 196, self.RULE_explicitConstructorInvocation)
        self._la = 0 # Token type
        try:
            self.state = 1329
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,129,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1304
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Java20Parser.LT:
                    self.state = 1303
                    self.typeArguments()


                self.state = 1306
                _la = self._input.LA(1)
                if not(_la==Java20Parser.SUPER or _la==Java20Parser.THIS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 1307
                self.match(Java20Parser.LPAREN)
                self.state = 1309
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java20Parser.EXPORTS) | (1 << Java20Parser.MODULE) | (1 << Java20Parser.NONSEALED) | (1 << Java20Parser.OPEN) | (1 << Java20Parser.OPENS) | (1 << Java20Parser.PERMITS) | (1 << Java20Parser.PROVIDES) | (1 << Java20Parser.RECORD) | (1 << Java20Parser.REQUIRES) | (1 << Java20Parser.SEALED) | (1 << Java20Parser.TO) | (1 << Java20Parser.TRANSITIVE) | (1 << Java20Parser.USES) | (1 << Java20Parser.VAR) | (1 << Java20Parser.WITH) | (1 << Java20Parser.YIELD) | (1 << Java20Parser.BOOLEAN) | (1 << Java20Parser.BYTE) | (1 << Java20Parser.CHAR) | (1 << Java20Parser.DOUBLE) | (1 << Java20Parser.FLOAT) | (1 << Java20Parser.INT) | (1 << Java20Parser.LONG) | (1 << Java20Parser.NEW) | (1 << Java20Parser.SHORT) | (1 << Java20Parser.SUPER) | (1 << Java20Parser.SWITCH) | (1 << Java20Parser.THIS))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (Java20Parser.VOID - 65)) | (1 << (Java20Parser.IntegerLiteral - 65)) | (1 << (Java20Parser.FloatingPointLiteral - 65)) | (1 << (Java20Parser.BooleanLiteral - 65)) | (1 << (Java20Parser.CharacterLiteral - 65)) | (1 << (Java20Parser.StringLiteral - 65)) | (1 << (Java20Parser.TextBlock - 65)) | (1 << (Java20Parser.NullLiteral - 65)) | (1 << (Java20Parser.LPAREN - 65)) | (1 << (Java20Parser.AT - 65)) | (1 << (Java20Parser.BANG - 65)) | (1 << (Java20Parser.TILDE - 65)) | (1 << (Java20Parser.INC - 65)) | (1 << (Java20Parser.DEC - 65)) | (1 << (Java20Parser.ADD - 65)) | (1 << (Java20Parser.SUB - 65)) | (1 << (Java20Parser.Identifier - 65)))) != 0):
                    self.state = 1308
                    self.argumentList()


                self.state = 1311
                self.match(Java20Parser.RPAREN)
                self.state = 1312
                self.match(Java20Parser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1315
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,126,self._ctx)
                if la_ == 1:
                    self.state = 1313
                    self.expressionName()
                    pass

                elif la_ == 2:
                    self.state = 1314
                    self.primary()
                    pass


                self.state = 1317
                self.match(Java20Parser.DOT)
                self.state = 1319
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Java20Parser.LT:
                    self.state = 1318
                    self.typeArguments()


                self.state = 1321
                self.match(Java20Parser.SUPER)
                self.state = 1322
                self.match(Java20Parser.LPAREN)
                self.state = 1324
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java20Parser.EXPORTS) | (1 << Java20Parser.MODULE) | (1 << Java20Parser.NONSEALED) | (1 << Java20Parser.OPEN) | (1 << Java20Parser.OPENS) | (1 << Java20Parser.PERMITS) | (1 << Java20Parser.PROVIDES) | (1 << Java20Parser.RECORD) | (1 << Java20Parser.REQUIRES) | (1 << Java20Parser.SEALED) | (1 << Java20Parser.TO) | (1 << Java20Parser.TRANSITIVE) | (1 << Java20Parser.USES) | (1 << Java20Parser.VAR) | (1 << Java20Parser.WITH) | (1 << Java20Parser.YIELD) | (1 << Java20Parser.BOOLEAN) | (1 << Java20Parser.BYTE) | (1 << Java20Parser.CHAR) | (1 << Java20Parser.DOUBLE) | (1 << Java20Parser.FLOAT) | (1 << Java20Parser.INT) | (1 << Java20Parser.LONG) | (1 << Java20Parser.NEW) | (1 << Java20Parser.SHORT) | (1 << Java20Parser.SUPER) | (1 << Java20Parser.SWITCH) | (1 << Java20Parser.THIS))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (Java20Parser.VOID - 65)) | (1 << (Java20Parser.IntegerLiteral - 65)) | (1 << (Java20Parser.FloatingPointLiteral - 65)) | (1 << (Java20Parser.BooleanLiteral - 65)) | (1 << (Java20Parser.CharacterLiteral - 65)) | (1 << (Java20Parser.StringLiteral - 65)) | (1 << (Java20Parser.TextBlock - 65)) | (1 << (Java20Parser.NullLiteral - 65)) | (1 << (Java20Parser.LPAREN - 65)) | (1 << (Java20Parser.AT - 65)) | (1 << (Java20Parser.BANG - 65)) | (1 << (Java20Parser.TILDE - 65)) | (1 << (Java20Parser.INC - 65)) | (1 << (Java20Parser.DEC - 65)) | (1 << (Java20Parser.ADD - 65)) | (1 << (Java20Parser.SUB - 65)) | (1 << (Java20Parser.Identifier - 65)))) != 0):
                    self.state = 1323
                    self.argumentList()


                self.state = 1326
                self.match(Java20Parser.RPAREN)
                self.state = 1327
                self.match(Java20Parser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EnumDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ENUM(self):
            return self.getToken(Java20Parser.ENUM, 0)

        def typeIdentifier(self):
            return self.getTypedRuleContext(Java20Parser.TypeIdentifierContext,0)


        def enumBody(self):
            return self.getTypedRuleContext(Java20Parser.EnumBodyContext,0)


        def classModifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.ClassModifierContext)
            else:
                return self.getTypedRuleContext(Java20Parser.ClassModifierContext,i)


        def classImplements(self):
            return self.getTypedRuleContext(Java20Parser.ClassImplementsContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_enumDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnumDeclaration" ):
                listener.enterEnumDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnumDeclaration" ):
                listener.exitEnumDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnumDeclaration" ):
                return visitor.visitEnumDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def enumDeclaration(self):

        localctx = Java20Parser.EnumDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 198, self.RULE_enumDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1334
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java20Parser.NONSEALED) | (1 << Java20Parser.SEALED) | (1 << Java20Parser.ABSTRACT) | (1 << Java20Parser.FINAL) | (1 << Java20Parser.PRIVATE) | (1 << Java20Parser.PROTECTED) | (1 << Java20Parser.PUBLIC) | (1 << Java20Parser.STATIC) | (1 << Java20Parser.STRICTFP))) != 0) or _la==Java20Parser.AT:
                self.state = 1331
                self.classModifier()
                self.state = 1336
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1337
            self.match(Java20Parser.ENUM)
            self.state = 1338
            self.typeIdentifier()
            self.state = 1340
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Java20Parser.IMPLEMENTS:
                self.state = 1339
                self.classImplements()


            self.state = 1342
            self.enumBody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EnumBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(Java20Parser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(Java20Parser.RBRACE, 0)

        def enumConstantList(self):
            return self.getTypedRuleContext(Java20Parser.EnumConstantListContext,0)


        def COMMA(self):
            return self.getToken(Java20Parser.COMMA, 0)

        def enumBodyDeclarations(self):
            return self.getTypedRuleContext(Java20Parser.EnumBodyDeclarationsContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_enumBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnumBody" ):
                listener.enterEnumBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnumBody" ):
                listener.exitEnumBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnumBody" ):
                return visitor.visitEnumBody(self)
            else:
                return visitor.visitChildren(self)




    def enumBody(self):

        localctx = Java20Parser.EnumBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 200, self.RULE_enumBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1344
            self.match(Java20Parser.LBRACE)
            self.state = 1346
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java20Parser.EXPORTS) | (1 << Java20Parser.MODULE) | (1 << Java20Parser.NONSEALED) | (1 << Java20Parser.OPEN) | (1 << Java20Parser.OPENS) | (1 << Java20Parser.PERMITS) | (1 << Java20Parser.PROVIDES) | (1 << Java20Parser.RECORD) | (1 << Java20Parser.REQUIRES) | (1 << Java20Parser.SEALED) | (1 << Java20Parser.TO) | (1 << Java20Parser.TRANSITIVE) | (1 << Java20Parser.USES) | (1 << Java20Parser.VAR) | (1 << Java20Parser.WITH) | (1 << Java20Parser.YIELD))) != 0) or _la==Java20Parser.AT or _la==Java20Parser.Identifier:
                self.state = 1345
                self.enumConstantList()


            self.state = 1349
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Java20Parser.COMMA:
                self.state = 1348
                self.match(Java20Parser.COMMA)


            self.state = 1352
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Java20Parser.SEMI:
                self.state = 1351
                self.enumBodyDeclarations()


            self.state = 1354
            self.match(Java20Parser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EnumConstantListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def enumConstant(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.EnumConstantContext)
            else:
                return self.getTypedRuleContext(Java20Parser.EnumConstantContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(Java20Parser.COMMA)
            else:
                return self.getToken(Java20Parser.COMMA, i)

        def getRuleIndex(self):
            return Java20Parser.RULE_enumConstantList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnumConstantList" ):
                listener.enterEnumConstantList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnumConstantList" ):
                listener.exitEnumConstantList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnumConstantList" ):
                return visitor.visitEnumConstantList(self)
            else:
                return visitor.visitChildren(self)




    def enumConstantList(self):

        localctx = Java20Parser.EnumConstantListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 202, self.RULE_enumConstantList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1356
            self.enumConstant()
            self.state = 1361
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,135,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1357
                    self.match(Java20Parser.COMMA)
                    self.state = 1358
                    self.enumConstant() 
                self.state = 1363
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,135,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EnumConstantContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(Java20Parser.IdentifierContext,0)


        def enumConstantModifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.EnumConstantModifierContext)
            else:
                return self.getTypedRuleContext(Java20Parser.EnumConstantModifierContext,i)


        def LPAREN(self):
            return self.getToken(Java20Parser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(Java20Parser.RPAREN, 0)

        def classBody(self):
            return self.getTypedRuleContext(Java20Parser.ClassBodyContext,0)


        def argumentList(self):
            return self.getTypedRuleContext(Java20Parser.ArgumentListContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_enumConstant

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnumConstant" ):
                listener.enterEnumConstant(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnumConstant" ):
                listener.exitEnumConstant(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnumConstant" ):
                return visitor.visitEnumConstant(self)
            else:
                return visitor.visitChildren(self)




    def enumConstant(self):

        localctx = Java20Parser.EnumConstantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 204, self.RULE_enumConstant)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1367
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Java20Parser.AT:
                self.state = 1364
                self.enumConstantModifier()
                self.state = 1369
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1370
            self.identifier()
            self.state = 1376
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Java20Parser.LPAREN:
                self.state = 1371
                self.match(Java20Parser.LPAREN)
                self.state = 1373
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java20Parser.EXPORTS) | (1 << Java20Parser.MODULE) | (1 << Java20Parser.NONSEALED) | (1 << Java20Parser.OPEN) | (1 << Java20Parser.OPENS) | (1 << Java20Parser.PERMITS) | (1 << Java20Parser.PROVIDES) | (1 << Java20Parser.RECORD) | (1 << Java20Parser.REQUIRES) | (1 << Java20Parser.SEALED) | (1 << Java20Parser.TO) | (1 << Java20Parser.TRANSITIVE) | (1 << Java20Parser.USES) | (1 << Java20Parser.VAR) | (1 << Java20Parser.WITH) | (1 << Java20Parser.YIELD) | (1 << Java20Parser.BOOLEAN) | (1 << Java20Parser.BYTE) | (1 << Java20Parser.CHAR) | (1 << Java20Parser.DOUBLE) | (1 << Java20Parser.FLOAT) | (1 << Java20Parser.INT) | (1 << Java20Parser.LONG) | (1 << Java20Parser.NEW) | (1 << Java20Parser.SHORT) | (1 << Java20Parser.SUPER) | (1 << Java20Parser.SWITCH) | (1 << Java20Parser.THIS))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (Java20Parser.VOID - 65)) | (1 << (Java20Parser.IntegerLiteral - 65)) | (1 << (Java20Parser.FloatingPointLiteral - 65)) | (1 << (Java20Parser.BooleanLiteral - 65)) | (1 << (Java20Parser.CharacterLiteral - 65)) | (1 << (Java20Parser.StringLiteral - 65)) | (1 << (Java20Parser.TextBlock - 65)) | (1 << (Java20Parser.NullLiteral - 65)) | (1 << (Java20Parser.LPAREN - 65)) | (1 << (Java20Parser.AT - 65)) | (1 << (Java20Parser.BANG - 65)) | (1 << (Java20Parser.TILDE - 65)) | (1 << (Java20Parser.INC - 65)) | (1 << (Java20Parser.DEC - 65)) | (1 << (Java20Parser.ADD - 65)) | (1 << (Java20Parser.SUB - 65)) | (1 << (Java20Parser.Identifier - 65)))) != 0):
                    self.state = 1372
                    self.argumentList()


                self.state = 1375
                self.match(Java20Parser.RPAREN)


            self.state = 1379
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Java20Parser.LBRACE:
                self.state = 1378
                self.classBody()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EnumConstantModifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def annotation(self):
            return self.getTypedRuleContext(Java20Parser.AnnotationContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_enumConstantModifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnumConstantModifier" ):
                listener.enterEnumConstantModifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnumConstantModifier" ):
                listener.exitEnumConstantModifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnumConstantModifier" ):
                return visitor.visitEnumConstantModifier(self)
            else:
                return visitor.visitChildren(self)




    def enumConstantModifier(self):

        localctx = Java20Parser.EnumConstantModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 206, self.RULE_enumConstantModifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1381
            self.annotation()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EnumBodyDeclarationsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(Java20Parser.SEMI, 0)

        def classBodyDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.ClassBodyDeclarationContext)
            else:
                return self.getTypedRuleContext(Java20Parser.ClassBodyDeclarationContext,i)


        def getRuleIndex(self):
            return Java20Parser.RULE_enumBodyDeclarations

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnumBodyDeclarations" ):
                listener.enterEnumBodyDeclarations(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnumBodyDeclarations" ):
                listener.exitEnumBodyDeclarations(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnumBodyDeclarations" ):
                return visitor.visitEnumBodyDeclarations(self)
            else:
                return visitor.visitChildren(self)




    def enumBodyDeclarations(self):

        localctx = Java20Parser.EnumBodyDeclarationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 208, self.RULE_enumBodyDeclarations)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1383
            self.match(Java20Parser.SEMI)
            self.state = 1387
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java20Parser.EXPORTS) | (1 << Java20Parser.MODULE) | (1 << Java20Parser.NONSEALED) | (1 << Java20Parser.OPEN) | (1 << Java20Parser.OPENS) | (1 << Java20Parser.PERMITS) | (1 << Java20Parser.PROVIDES) | (1 << Java20Parser.RECORD) | (1 << Java20Parser.REQUIRES) | (1 << Java20Parser.SEALED) | (1 << Java20Parser.TO) | (1 << Java20Parser.TRANSITIVE) | (1 << Java20Parser.USES) | (1 << Java20Parser.VAR) | (1 << Java20Parser.WITH) | (1 << Java20Parser.YIELD) | (1 << Java20Parser.ABSTRACT) | (1 << Java20Parser.BOOLEAN) | (1 << Java20Parser.BYTE) | (1 << Java20Parser.CHAR) | (1 << Java20Parser.CLASS) | (1 << Java20Parser.DOUBLE) | (1 << Java20Parser.ENUM) | (1 << Java20Parser.FINAL) | (1 << Java20Parser.FLOAT) | (1 << Java20Parser.INT) | (1 << Java20Parser.INTERFACE) | (1 << Java20Parser.LONG) | (1 << Java20Parser.NATIVE) | (1 << Java20Parser.PRIVATE) | (1 << Java20Parser.PROTECTED) | (1 << Java20Parser.PUBLIC) | (1 << Java20Parser.SHORT) | (1 << Java20Parser.STATIC) | (1 << Java20Parser.STRICTFP) | (1 << Java20Parser.SYNCHRONIZED) | (1 << Java20Parser.TRANSIENT))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (Java20Parser.VOID - 65)) | (1 << (Java20Parser.VOLATILE - 65)) | (1 << (Java20Parser.LBRACE - 65)) | (1 << (Java20Parser.SEMI - 65)) | (1 << (Java20Parser.AT - 65)) | (1 << (Java20Parser.LT - 65)) | (1 << (Java20Parser.Identifier - 65)))) != 0):
                self.state = 1384
                self.classBodyDeclaration()
                self.state = 1389
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RecordDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RECORD(self):
            return self.getToken(Java20Parser.RECORD, 0)

        def typeIdentifier(self):
            return self.getTypedRuleContext(Java20Parser.TypeIdentifierContext,0)


        def recordHeader(self):
            return self.getTypedRuleContext(Java20Parser.RecordHeaderContext,0)


        def recordBody(self):
            return self.getTypedRuleContext(Java20Parser.RecordBodyContext,0)


        def classModifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.ClassModifierContext)
            else:
                return self.getTypedRuleContext(Java20Parser.ClassModifierContext,i)


        def typeParameters(self):
            return self.getTypedRuleContext(Java20Parser.TypeParametersContext,0)


        def classImplements(self):
            return self.getTypedRuleContext(Java20Parser.ClassImplementsContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_recordDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRecordDeclaration" ):
                listener.enterRecordDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRecordDeclaration" ):
                listener.exitRecordDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRecordDeclaration" ):
                return visitor.visitRecordDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def recordDeclaration(self):

        localctx = Java20Parser.RecordDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 210, self.RULE_recordDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1393
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java20Parser.NONSEALED) | (1 << Java20Parser.SEALED) | (1 << Java20Parser.ABSTRACT) | (1 << Java20Parser.FINAL) | (1 << Java20Parser.PRIVATE) | (1 << Java20Parser.PROTECTED) | (1 << Java20Parser.PUBLIC) | (1 << Java20Parser.STATIC) | (1 << Java20Parser.STRICTFP))) != 0) or _la==Java20Parser.AT:
                self.state = 1390
                self.classModifier()
                self.state = 1395
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1396
            self.match(Java20Parser.RECORD)
            self.state = 1397
            self.typeIdentifier()
            self.state = 1399
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Java20Parser.LT:
                self.state = 1398
                self.typeParameters()


            self.state = 1401
            self.recordHeader()
            self.state = 1403
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Java20Parser.IMPLEMENTS:
                self.state = 1402
                self.classImplements()


            self.state = 1405
            self.recordBody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RecordHeaderContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(Java20Parser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(Java20Parser.RPAREN, 0)

        def recordComponentList(self):
            return self.getTypedRuleContext(Java20Parser.RecordComponentListContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_recordHeader

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRecordHeader" ):
                listener.enterRecordHeader(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRecordHeader" ):
                listener.exitRecordHeader(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRecordHeader" ):
                return visitor.visitRecordHeader(self)
            else:
                return visitor.visitChildren(self)




    def recordHeader(self):

        localctx = Java20Parser.RecordHeaderContext(self, self._ctx, self.state)
        self.enterRule(localctx, 212, self.RULE_recordHeader)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1407
            self.match(Java20Parser.LPAREN)
            self.state = 1409
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java20Parser.EXPORTS) | (1 << Java20Parser.MODULE) | (1 << Java20Parser.NONSEALED) | (1 << Java20Parser.OPEN) | (1 << Java20Parser.OPENS) | (1 << Java20Parser.PERMITS) | (1 << Java20Parser.PROVIDES) | (1 << Java20Parser.RECORD) | (1 << Java20Parser.REQUIRES) | (1 << Java20Parser.SEALED) | (1 << Java20Parser.TO) | (1 << Java20Parser.TRANSITIVE) | (1 << Java20Parser.USES) | (1 << Java20Parser.VAR) | (1 << Java20Parser.WITH) | (1 << Java20Parser.YIELD) | (1 << Java20Parser.BOOLEAN) | (1 << Java20Parser.BYTE) | (1 << Java20Parser.CHAR) | (1 << Java20Parser.DOUBLE) | (1 << Java20Parser.FLOAT) | (1 << Java20Parser.INT) | (1 << Java20Parser.LONG) | (1 << Java20Parser.SHORT))) != 0) or _la==Java20Parser.AT or _la==Java20Parser.Identifier:
                self.state = 1408
                self.recordComponentList()


            self.state = 1411
            self.match(Java20Parser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RecordComponentListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def recordComponent(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.RecordComponentContext)
            else:
                return self.getTypedRuleContext(Java20Parser.RecordComponentContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(Java20Parser.COMMA)
            else:
                return self.getToken(Java20Parser.COMMA, i)

        def getRuleIndex(self):
            return Java20Parser.RULE_recordComponentList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRecordComponentList" ):
                listener.enterRecordComponentList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRecordComponentList" ):
                listener.exitRecordComponentList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRecordComponentList" ):
                return visitor.visitRecordComponentList(self)
            else:
                return visitor.visitChildren(self)




    def recordComponentList(self):

        localctx = Java20Parser.RecordComponentListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 214, self.RULE_recordComponentList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1413
            self.recordComponent()
            self.state = 1418
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Java20Parser.COMMA:
                self.state = 1414
                self.match(Java20Parser.COMMA)
                self.state = 1415
                self.recordComponent()
                self.state = 1420
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RecordComponentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unannType(self):
            return self.getTypedRuleContext(Java20Parser.UnannTypeContext,0)


        def identifier(self):
            return self.getTypedRuleContext(Java20Parser.IdentifierContext,0)


        def recordComponentModifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.RecordComponentModifierContext)
            else:
                return self.getTypedRuleContext(Java20Parser.RecordComponentModifierContext,i)


        def variableArityRecordComponent(self):
            return self.getTypedRuleContext(Java20Parser.VariableArityRecordComponentContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_recordComponent

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRecordComponent" ):
                listener.enterRecordComponent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRecordComponent" ):
                listener.exitRecordComponent(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRecordComponent" ):
                return visitor.visitRecordComponent(self)
            else:
                return visitor.visitChildren(self)




    def recordComponent(self):

        localctx = Java20Parser.RecordComponentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 216, self.RULE_recordComponent)
        self._la = 0 # Token type
        try:
            self.state = 1431
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,147,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1424
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==Java20Parser.AT:
                    self.state = 1421
                    self.recordComponentModifier()
                    self.state = 1426
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 1427
                self.unannType()
                self.state = 1428
                self.identifier()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1430
                self.variableArityRecordComponent()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableArityRecordComponentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unannType(self):
            return self.getTypedRuleContext(Java20Parser.UnannTypeContext,0)


        def ELLIPSIS(self):
            return self.getToken(Java20Parser.ELLIPSIS, 0)

        def identifier(self):
            return self.getTypedRuleContext(Java20Parser.IdentifierContext,0)


        def recordComponentModifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.RecordComponentModifierContext)
            else:
                return self.getTypedRuleContext(Java20Parser.RecordComponentModifierContext,i)


        def annotation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.AnnotationContext)
            else:
                return self.getTypedRuleContext(Java20Parser.AnnotationContext,i)


        def getRuleIndex(self):
            return Java20Parser.RULE_variableArityRecordComponent

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableArityRecordComponent" ):
                listener.enterVariableArityRecordComponent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableArityRecordComponent" ):
                listener.exitVariableArityRecordComponent(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableArityRecordComponent" ):
                return visitor.visitVariableArityRecordComponent(self)
            else:
                return visitor.visitChildren(self)




    def variableArityRecordComponent(self):

        localctx = Java20Parser.VariableArityRecordComponentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 218, self.RULE_variableArityRecordComponent)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1436
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Java20Parser.AT:
                self.state = 1433
                self.recordComponentModifier()
                self.state = 1438
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1439
            self.unannType()
            self.state = 1443
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Java20Parser.AT:
                self.state = 1440
                self.annotation()
                self.state = 1445
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1446
            self.match(Java20Parser.ELLIPSIS)
            self.state = 1447
            self.identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RecordComponentModifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def annotation(self):
            return self.getTypedRuleContext(Java20Parser.AnnotationContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_recordComponentModifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRecordComponentModifier" ):
                listener.enterRecordComponentModifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRecordComponentModifier" ):
                listener.exitRecordComponentModifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRecordComponentModifier" ):
                return visitor.visitRecordComponentModifier(self)
            else:
                return visitor.visitChildren(self)




    def recordComponentModifier(self):

        localctx = Java20Parser.RecordComponentModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 220, self.RULE_recordComponentModifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1449
            self.annotation()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RecordBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(Java20Parser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(Java20Parser.RBRACE, 0)

        def recordBodyDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.RecordBodyDeclarationContext)
            else:
                return self.getTypedRuleContext(Java20Parser.RecordBodyDeclarationContext,i)


        def getRuleIndex(self):
            return Java20Parser.RULE_recordBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRecordBody" ):
                listener.enterRecordBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRecordBody" ):
                listener.exitRecordBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRecordBody" ):
                return visitor.visitRecordBody(self)
            else:
                return visitor.visitChildren(self)




    def recordBody(self):

        localctx = Java20Parser.RecordBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 222, self.RULE_recordBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1451
            self.match(Java20Parser.LBRACE)
            self.state = 1455
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java20Parser.EXPORTS) | (1 << Java20Parser.MODULE) | (1 << Java20Parser.NONSEALED) | (1 << Java20Parser.OPEN) | (1 << Java20Parser.OPENS) | (1 << Java20Parser.PERMITS) | (1 << Java20Parser.PROVIDES) | (1 << Java20Parser.RECORD) | (1 << Java20Parser.REQUIRES) | (1 << Java20Parser.SEALED) | (1 << Java20Parser.TO) | (1 << Java20Parser.TRANSITIVE) | (1 << Java20Parser.USES) | (1 << Java20Parser.VAR) | (1 << Java20Parser.WITH) | (1 << Java20Parser.YIELD) | (1 << Java20Parser.ABSTRACT) | (1 << Java20Parser.BOOLEAN) | (1 << Java20Parser.BYTE) | (1 << Java20Parser.CHAR) | (1 << Java20Parser.CLASS) | (1 << Java20Parser.DOUBLE) | (1 << Java20Parser.ENUM) | (1 << Java20Parser.FINAL) | (1 << Java20Parser.FLOAT) | (1 << Java20Parser.INT) | (1 << Java20Parser.INTERFACE) | (1 << Java20Parser.LONG) | (1 << Java20Parser.NATIVE) | (1 << Java20Parser.PRIVATE) | (1 << Java20Parser.PROTECTED) | (1 << Java20Parser.PUBLIC) | (1 << Java20Parser.SHORT) | (1 << Java20Parser.STATIC) | (1 << Java20Parser.STRICTFP) | (1 << Java20Parser.SYNCHRONIZED) | (1 << Java20Parser.TRANSIENT))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (Java20Parser.VOID - 65)) | (1 << (Java20Parser.VOLATILE - 65)) | (1 << (Java20Parser.LBRACE - 65)) | (1 << (Java20Parser.SEMI - 65)) | (1 << (Java20Parser.AT - 65)) | (1 << (Java20Parser.LT - 65)) | (1 << (Java20Parser.Identifier - 65)))) != 0):
                self.state = 1452
                self.recordBodyDeclaration()
                self.state = 1457
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1458
            self.match(Java20Parser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RecordBodyDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classBodyDeclaration(self):
            return self.getTypedRuleContext(Java20Parser.ClassBodyDeclarationContext,0)


        def compactConstructorDeclaration(self):
            return self.getTypedRuleContext(Java20Parser.CompactConstructorDeclarationContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_recordBodyDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRecordBodyDeclaration" ):
                listener.enterRecordBodyDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRecordBodyDeclaration" ):
                listener.exitRecordBodyDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRecordBodyDeclaration" ):
                return visitor.visitRecordBodyDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def recordBodyDeclaration(self):

        localctx = Java20Parser.RecordBodyDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 224, self.RULE_recordBodyDeclaration)
        try:
            self.state = 1462
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,151,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1460
                self.classBodyDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1461
                self.compactConstructorDeclaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompactConstructorDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simpleTypeName(self):
            return self.getTypedRuleContext(Java20Parser.SimpleTypeNameContext,0)


        def constructorBody(self):
            return self.getTypedRuleContext(Java20Parser.ConstructorBodyContext,0)


        def constructorModifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.ConstructorModifierContext)
            else:
                return self.getTypedRuleContext(Java20Parser.ConstructorModifierContext,i)


        def getRuleIndex(self):
            return Java20Parser.RULE_compactConstructorDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompactConstructorDeclaration" ):
                listener.enterCompactConstructorDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompactConstructorDeclaration" ):
                listener.exitCompactConstructorDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompactConstructorDeclaration" ):
                return visitor.visitCompactConstructorDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def compactConstructorDeclaration(self):

        localctx = Java20Parser.CompactConstructorDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 226, self.RULE_compactConstructorDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1467
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 50)) & ~0x3f) == 0 and ((1 << (_la - 50)) & ((1 << (Java20Parser.PRIVATE - 50)) | (1 << (Java20Parser.PROTECTED - 50)) | (1 << (Java20Parser.PUBLIC - 50)) | (1 << (Java20Parser.AT - 50)))) != 0):
                self.state = 1464
                self.constructorModifier()
                self.state = 1469
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1470
            self.simpleTypeName()
            self.state = 1471
            self.constructorBody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfaceDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def normalInterfaceDeclaration(self):
            return self.getTypedRuleContext(Java20Parser.NormalInterfaceDeclarationContext,0)


        def annotationInterfaceDeclaration(self):
            return self.getTypedRuleContext(Java20Parser.AnnotationInterfaceDeclarationContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_interfaceDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterfaceDeclaration" ):
                listener.enterInterfaceDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterfaceDeclaration" ):
                listener.exitInterfaceDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfaceDeclaration" ):
                return visitor.visitInterfaceDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def interfaceDeclaration(self):

        localctx = Java20Parser.InterfaceDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 228, self.RULE_interfaceDeclaration)
        try:
            self.state = 1475
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,153,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1473
                self.normalInterfaceDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1474
                self.annotationInterfaceDeclaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NormalInterfaceDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTERFACE(self):
            return self.getToken(Java20Parser.INTERFACE, 0)

        def typeIdentifier(self):
            return self.getTypedRuleContext(Java20Parser.TypeIdentifierContext,0)


        def interfaceBody(self):
            return self.getTypedRuleContext(Java20Parser.InterfaceBodyContext,0)


        def interfaceModifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.InterfaceModifierContext)
            else:
                return self.getTypedRuleContext(Java20Parser.InterfaceModifierContext,i)


        def typeParameters(self):
            return self.getTypedRuleContext(Java20Parser.TypeParametersContext,0)


        def interfaceExtends(self):
            return self.getTypedRuleContext(Java20Parser.InterfaceExtendsContext,0)


        def interfacePermits(self):
            return self.getTypedRuleContext(Java20Parser.InterfacePermitsContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_normalInterfaceDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNormalInterfaceDeclaration" ):
                listener.enterNormalInterfaceDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNormalInterfaceDeclaration" ):
                listener.exitNormalInterfaceDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNormalInterfaceDeclaration" ):
                return visitor.visitNormalInterfaceDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def normalInterfaceDeclaration(self):

        localctx = Java20Parser.NormalInterfaceDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 230, self.RULE_normalInterfaceDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1480
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java20Parser.NONSEALED) | (1 << Java20Parser.SEALED) | (1 << Java20Parser.ABSTRACT) | (1 << Java20Parser.PRIVATE) | (1 << Java20Parser.PROTECTED) | (1 << Java20Parser.PUBLIC) | (1 << Java20Parser.STATIC) | (1 << Java20Parser.STRICTFP))) != 0) or _la==Java20Parser.AT:
                self.state = 1477
                self.interfaceModifier()
                self.state = 1482
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1483
            self.match(Java20Parser.INTERFACE)
            self.state = 1484
            self.typeIdentifier()
            self.state = 1486
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Java20Parser.LT:
                self.state = 1485
                self.typeParameters()


            self.state = 1489
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Java20Parser.EXTENDS:
                self.state = 1488
                self.interfaceExtends()


            self.state = 1492
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Java20Parser.PERMITS:
                self.state = 1491
                self.interfacePermits()


            self.state = 1494
            self.interfaceBody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfaceModifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def annotation(self):
            return self.getTypedRuleContext(Java20Parser.AnnotationContext,0)


        def PUBLIC(self):
            return self.getToken(Java20Parser.PUBLIC, 0)

        def PROTECTED(self):
            return self.getToken(Java20Parser.PROTECTED, 0)

        def PRIVATE(self):
            return self.getToken(Java20Parser.PRIVATE, 0)

        def ABSTRACT(self):
            return self.getToken(Java20Parser.ABSTRACT, 0)

        def STATIC(self):
            return self.getToken(Java20Parser.STATIC, 0)

        def SEALED(self):
            return self.getToken(Java20Parser.SEALED, 0)

        def NONSEALED(self):
            return self.getToken(Java20Parser.NONSEALED, 0)

        def STRICTFP(self):
            return self.getToken(Java20Parser.STRICTFP, 0)

        def getRuleIndex(self):
            return Java20Parser.RULE_interfaceModifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterfaceModifier" ):
                listener.enterInterfaceModifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterfaceModifier" ):
                listener.exitInterfaceModifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfaceModifier" ):
                return visitor.visitInterfaceModifier(self)
            else:
                return visitor.visitChildren(self)




    def interfaceModifier(self):

        localctx = Java20Parser.InterfaceModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 232, self.RULE_interfaceModifier)
        try:
            self.state = 1505
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Java20Parser.AT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1496
                self.annotation()
                pass
            elif token in [Java20Parser.PUBLIC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1497
                self.match(Java20Parser.PUBLIC)
                pass
            elif token in [Java20Parser.PROTECTED]:
                self.enterOuterAlt(localctx, 3)
                self.state = 1498
                self.match(Java20Parser.PROTECTED)
                pass
            elif token in [Java20Parser.PRIVATE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 1499
                self.match(Java20Parser.PRIVATE)
                pass
            elif token in [Java20Parser.ABSTRACT]:
                self.enterOuterAlt(localctx, 5)
                self.state = 1500
                self.match(Java20Parser.ABSTRACT)
                pass
            elif token in [Java20Parser.STATIC]:
                self.enterOuterAlt(localctx, 6)
                self.state = 1501
                self.match(Java20Parser.STATIC)
                pass
            elif token in [Java20Parser.SEALED]:
                self.enterOuterAlt(localctx, 7)
                self.state = 1502
                self.match(Java20Parser.SEALED)
                pass
            elif token in [Java20Parser.NONSEALED]:
                self.enterOuterAlt(localctx, 8)
                self.state = 1503
                self.match(Java20Parser.NONSEALED)
                pass
            elif token in [Java20Parser.STRICTFP]:
                self.enterOuterAlt(localctx, 9)
                self.state = 1504
                self.match(Java20Parser.STRICTFP)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfaceExtendsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EXTENDS(self):
            return self.getToken(Java20Parser.EXTENDS, 0)

        def interfaceTypeList(self):
            return self.getTypedRuleContext(Java20Parser.InterfaceTypeListContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_interfaceExtends

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterfaceExtends" ):
                listener.enterInterfaceExtends(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterfaceExtends" ):
                listener.exitInterfaceExtends(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfaceExtends" ):
                return visitor.visitInterfaceExtends(self)
            else:
                return visitor.visitChildren(self)




    def interfaceExtends(self):

        localctx = Java20Parser.InterfaceExtendsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 234, self.RULE_interfaceExtends)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1507
            self.match(Java20Parser.EXTENDS)
            self.state = 1508
            self.interfaceTypeList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfacePermitsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PERMITS(self):
            return self.getToken(Java20Parser.PERMITS, 0)

        def typeName(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.TypeNameContext)
            else:
                return self.getTypedRuleContext(Java20Parser.TypeNameContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(Java20Parser.COMMA)
            else:
                return self.getToken(Java20Parser.COMMA, i)

        def getRuleIndex(self):
            return Java20Parser.RULE_interfacePermits

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterfacePermits" ):
                listener.enterInterfacePermits(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterfacePermits" ):
                listener.exitInterfacePermits(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfacePermits" ):
                return visitor.visitInterfacePermits(self)
            else:
                return visitor.visitChildren(self)




    def interfacePermits(self):

        localctx = Java20Parser.InterfacePermitsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 236, self.RULE_interfacePermits)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1510
            self.match(Java20Parser.PERMITS)
            self.state = 1511
            self.typeName()
            self.state = 1516
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Java20Parser.COMMA:
                self.state = 1512
                self.match(Java20Parser.COMMA)
                self.state = 1513
                self.typeName()
                self.state = 1518
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfaceBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(Java20Parser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(Java20Parser.RBRACE, 0)

        def interfaceMemberDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.InterfaceMemberDeclarationContext)
            else:
                return self.getTypedRuleContext(Java20Parser.InterfaceMemberDeclarationContext,i)


        def getRuleIndex(self):
            return Java20Parser.RULE_interfaceBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterfaceBody" ):
                listener.enterInterfaceBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterfaceBody" ):
                listener.exitInterfaceBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfaceBody" ):
                return visitor.visitInterfaceBody(self)
            else:
                return visitor.visitChildren(self)




    def interfaceBody(self):

        localctx = Java20Parser.InterfaceBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 238, self.RULE_interfaceBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1519
            self.match(Java20Parser.LBRACE)
            self.state = 1523
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java20Parser.EXPORTS) | (1 << Java20Parser.MODULE) | (1 << Java20Parser.NONSEALED) | (1 << Java20Parser.OPEN) | (1 << Java20Parser.OPENS) | (1 << Java20Parser.PERMITS) | (1 << Java20Parser.PROVIDES) | (1 << Java20Parser.RECORD) | (1 << Java20Parser.REQUIRES) | (1 << Java20Parser.SEALED) | (1 << Java20Parser.TO) | (1 << Java20Parser.TRANSITIVE) | (1 << Java20Parser.USES) | (1 << Java20Parser.VAR) | (1 << Java20Parser.WITH) | (1 << Java20Parser.YIELD) | (1 << Java20Parser.ABSTRACT) | (1 << Java20Parser.BOOLEAN) | (1 << Java20Parser.BYTE) | (1 << Java20Parser.CHAR) | (1 << Java20Parser.CLASS) | (1 << Java20Parser.DEFAULT) | (1 << Java20Parser.DOUBLE) | (1 << Java20Parser.ENUM) | (1 << Java20Parser.FINAL) | (1 << Java20Parser.FLOAT) | (1 << Java20Parser.INT) | (1 << Java20Parser.INTERFACE) | (1 << Java20Parser.LONG) | (1 << Java20Parser.PRIVATE) | (1 << Java20Parser.PROTECTED) | (1 << Java20Parser.PUBLIC) | (1 << Java20Parser.SHORT) | (1 << Java20Parser.STATIC) | (1 << Java20Parser.STRICTFP))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (Java20Parser.VOID - 65)) | (1 << (Java20Parser.SEMI - 65)) | (1 << (Java20Parser.AT - 65)) | (1 << (Java20Parser.LT - 65)) | (1 << (Java20Parser.Identifier - 65)))) != 0):
                self.state = 1520
                self.interfaceMemberDeclaration()
                self.state = 1525
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1526
            self.match(Java20Parser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfaceMemberDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def constantDeclaration(self):
            return self.getTypedRuleContext(Java20Parser.ConstantDeclarationContext,0)


        def interfaceMethodDeclaration(self):
            return self.getTypedRuleContext(Java20Parser.InterfaceMethodDeclarationContext,0)


        def classDeclaration(self):
            return self.getTypedRuleContext(Java20Parser.ClassDeclarationContext,0)


        def interfaceDeclaration(self):
            return self.getTypedRuleContext(Java20Parser.InterfaceDeclarationContext,0)


        def SEMI(self):
            return self.getToken(Java20Parser.SEMI, 0)

        def getRuleIndex(self):
            return Java20Parser.RULE_interfaceMemberDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterfaceMemberDeclaration" ):
                listener.enterInterfaceMemberDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterfaceMemberDeclaration" ):
                listener.exitInterfaceMemberDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfaceMemberDeclaration" ):
                return visitor.visitInterfaceMemberDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def interfaceMemberDeclaration(self):

        localctx = Java20Parser.InterfaceMemberDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 240, self.RULE_interfaceMemberDeclaration)
        try:
            self.state = 1533
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,161,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1528
                self.constantDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1529
                self.interfaceMethodDeclaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1530
                self.classDeclaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1531
                self.interfaceDeclaration()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1532
                self.match(Java20Parser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstantDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unannType(self):
            return self.getTypedRuleContext(Java20Parser.UnannTypeContext,0)


        def variableDeclaratorList(self):
            return self.getTypedRuleContext(Java20Parser.VariableDeclaratorListContext,0)


        def SEMI(self):
            return self.getToken(Java20Parser.SEMI, 0)

        def constantModifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.ConstantModifierContext)
            else:
                return self.getTypedRuleContext(Java20Parser.ConstantModifierContext,i)


        def getRuleIndex(self):
            return Java20Parser.RULE_constantDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstantDeclaration" ):
                listener.enterConstantDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstantDeclaration" ):
                listener.exitConstantDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstantDeclaration" ):
                return visitor.visitConstantDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def constantDeclaration(self):

        localctx = Java20Parser.ConstantDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 242, self.RULE_constantDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1538
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 35)) & ~0x3f) == 0 and ((1 << (_la - 35)) & ((1 << (Java20Parser.FINAL - 35)) | (1 << (Java20Parser.PUBLIC - 35)) | (1 << (Java20Parser.STATIC - 35)) | (1 << (Java20Parser.AT - 35)))) != 0):
                self.state = 1535
                self.constantModifier()
                self.state = 1540
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1541
            self.unannType()
            self.state = 1542
            self.variableDeclaratorList()
            self.state = 1543
            self.match(Java20Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstantModifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def annotation(self):
            return self.getTypedRuleContext(Java20Parser.AnnotationContext,0)


        def PUBLIC(self):
            return self.getToken(Java20Parser.PUBLIC, 0)

        def STATIC(self):
            return self.getToken(Java20Parser.STATIC, 0)

        def FINAL(self):
            return self.getToken(Java20Parser.FINAL, 0)

        def getRuleIndex(self):
            return Java20Parser.RULE_constantModifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstantModifier" ):
                listener.enterConstantModifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstantModifier" ):
                listener.exitConstantModifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstantModifier" ):
                return visitor.visitConstantModifier(self)
            else:
                return visitor.visitChildren(self)




    def constantModifier(self):

        localctx = Java20Parser.ConstantModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 244, self.RULE_constantModifier)
        try:
            self.state = 1549
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Java20Parser.AT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1545
                self.annotation()
                pass
            elif token in [Java20Parser.PUBLIC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1546
                self.match(Java20Parser.PUBLIC)
                pass
            elif token in [Java20Parser.STATIC]:
                self.enterOuterAlt(localctx, 3)
                self.state = 1547
                self.match(Java20Parser.STATIC)
                pass
            elif token in [Java20Parser.FINAL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 1548
                self.match(Java20Parser.FINAL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfaceMethodDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def methodHeader(self):
            return self.getTypedRuleContext(Java20Parser.MethodHeaderContext,0)


        def methodBody(self):
            return self.getTypedRuleContext(Java20Parser.MethodBodyContext,0)


        def interfaceMethodModifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.InterfaceMethodModifierContext)
            else:
                return self.getTypedRuleContext(Java20Parser.InterfaceMethodModifierContext,i)


        def getRuleIndex(self):
            return Java20Parser.RULE_interfaceMethodDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterfaceMethodDeclaration" ):
                listener.enterInterfaceMethodDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterfaceMethodDeclaration" ):
                listener.exitInterfaceMethodDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfaceMethodDeclaration" ):
                return visitor.visitInterfaceMethodDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def interfaceMethodDeclaration(self):

        localctx = Java20Parser.InterfaceMethodDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 246, self.RULE_interfaceMethodDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1554
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java20Parser.ABSTRACT) | (1 << Java20Parser.DEFAULT) | (1 << Java20Parser.PRIVATE) | (1 << Java20Parser.PUBLIC) | (1 << Java20Parser.STATIC) | (1 << Java20Parser.STRICTFP))) != 0) or _la==Java20Parser.AT:
                self.state = 1551
                self.interfaceMethodModifier()
                self.state = 1556
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1557
            self.methodHeader()
            self.state = 1558
            self.methodBody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfaceMethodModifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def annotation(self):
            return self.getTypedRuleContext(Java20Parser.AnnotationContext,0)


        def PUBLIC(self):
            return self.getToken(Java20Parser.PUBLIC, 0)

        def PRIVATE(self):
            return self.getToken(Java20Parser.PRIVATE, 0)

        def ABSTRACT(self):
            return self.getToken(Java20Parser.ABSTRACT, 0)

        def DEFAULT(self):
            return self.getToken(Java20Parser.DEFAULT, 0)

        def STATIC(self):
            return self.getToken(Java20Parser.STATIC, 0)

        def STRICTFP(self):
            return self.getToken(Java20Parser.STRICTFP, 0)

        def getRuleIndex(self):
            return Java20Parser.RULE_interfaceMethodModifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterfaceMethodModifier" ):
                listener.enterInterfaceMethodModifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterfaceMethodModifier" ):
                listener.exitInterfaceMethodModifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfaceMethodModifier" ):
                return visitor.visitInterfaceMethodModifier(self)
            else:
                return visitor.visitChildren(self)




    def interfaceMethodModifier(self):

        localctx = Java20Parser.InterfaceMethodModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 248, self.RULE_interfaceMethodModifier)
        try:
            self.state = 1567
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Java20Parser.AT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1560
                self.annotation()
                pass
            elif token in [Java20Parser.PUBLIC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1561
                self.match(Java20Parser.PUBLIC)
                pass
            elif token in [Java20Parser.PRIVATE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 1562
                self.match(Java20Parser.PRIVATE)
                pass
            elif token in [Java20Parser.ABSTRACT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 1563
                self.match(Java20Parser.ABSTRACT)
                pass
            elif token in [Java20Parser.DEFAULT]:
                self.enterOuterAlt(localctx, 5)
                self.state = 1564
                self.match(Java20Parser.DEFAULT)
                pass
            elif token in [Java20Parser.STATIC]:
                self.enterOuterAlt(localctx, 6)
                self.state = 1565
                self.match(Java20Parser.STATIC)
                pass
            elif token in [Java20Parser.STRICTFP]:
                self.enterOuterAlt(localctx, 7)
                self.state = 1566
                self.match(Java20Parser.STRICTFP)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AnnotationInterfaceDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AT(self):
            return self.getToken(Java20Parser.AT, 0)

        def INTERFACE(self):
            return self.getToken(Java20Parser.INTERFACE, 0)

        def typeIdentifier(self):
            return self.getTypedRuleContext(Java20Parser.TypeIdentifierContext,0)


        def annotationInterfaceBody(self):
            return self.getTypedRuleContext(Java20Parser.AnnotationInterfaceBodyContext,0)


        def interfaceModifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.InterfaceModifierContext)
            else:
                return self.getTypedRuleContext(Java20Parser.InterfaceModifierContext,i)


        def getRuleIndex(self):
            return Java20Parser.RULE_annotationInterfaceDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnnotationInterfaceDeclaration" ):
                listener.enterAnnotationInterfaceDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnnotationInterfaceDeclaration" ):
                listener.exitAnnotationInterfaceDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAnnotationInterfaceDeclaration" ):
                return visitor.visitAnnotationInterfaceDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def annotationInterfaceDeclaration(self):

        localctx = Java20Parser.AnnotationInterfaceDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 250, self.RULE_annotationInterfaceDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1572
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,166,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1569
                    self.interfaceModifier() 
                self.state = 1574
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,166,self._ctx)

            self.state = 1575
            self.match(Java20Parser.AT)
            self.state = 1576
            self.match(Java20Parser.INTERFACE)
            self.state = 1577
            self.typeIdentifier()
            self.state = 1578
            self.annotationInterfaceBody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AnnotationInterfaceBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(Java20Parser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(Java20Parser.RBRACE, 0)

        def annotationInterfaceMemberDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.AnnotationInterfaceMemberDeclarationContext)
            else:
                return self.getTypedRuleContext(Java20Parser.AnnotationInterfaceMemberDeclarationContext,i)


        def getRuleIndex(self):
            return Java20Parser.RULE_annotationInterfaceBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnnotationInterfaceBody" ):
                listener.enterAnnotationInterfaceBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnnotationInterfaceBody" ):
                listener.exitAnnotationInterfaceBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAnnotationInterfaceBody" ):
                return visitor.visitAnnotationInterfaceBody(self)
            else:
                return visitor.visitChildren(self)




    def annotationInterfaceBody(self):

        localctx = Java20Parser.AnnotationInterfaceBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 252, self.RULE_annotationInterfaceBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1580
            self.match(Java20Parser.LBRACE)
            self.state = 1584
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java20Parser.EXPORTS) | (1 << Java20Parser.MODULE) | (1 << Java20Parser.NONSEALED) | (1 << Java20Parser.OPEN) | (1 << Java20Parser.OPENS) | (1 << Java20Parser.PERMITS) | (1 << Java20Parser.PROVIDES) | (1 << Java20Parser.RECORD) | (1 << Java20Parser.REQUIRES) | (1 << Java20Parser.SEALED) | (1 << Java20Parser.TO) | (1 << Java20Parser.TRANSITIVE) | (1 << Java20Parser.USES) | (1 << Java20Parser.VAR) | (1 << Java20Parser.WITH) | (1 << Java20Parser.YIELD) | (1 << Java20Parser.ABSTRACT) | (1 << Java20Parser.BOOLEAN) | (1 << Java20Parser.BYTE) | (1 << Java20Parser.CHAR) | (1 << Java20Parser.CLASS) | (1 << Java20Parser.DOUBLE) | (1 << Java20Parser.ENUM) | (1 << Java20Parser.FINAL) | (1 << Java20Parser.FLOAT) | (1 << Java20Parser.INT) | (1 << Java20Parser.INTERFACE) | (1 << Java20Parser.LONG) | (1 << Java20Parser.PRIVATE) | (1 << Java20Parser.PROTECTED) | (1 << Java20Parser.PUBLIC) | (1 << Java20Parser.SHORT) | (1 << Java20Parser.STATIC) | (1 << Java20Parser.STRICTFP))) != 0) or ((((_la - 82)) & ~0x3f) == 0 and ((1 << (_la - 82)) & ((1 << (Java20Parser.SEMI - 82)) | (1 << (Java20Parser.AT - 82)) | (1 << (Java20Parser.Identifier - 82)))) != 0):
                self.state = 1581
                self.annotationInterfaceMemberDeclaration()
                self.state = 1586
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1587
            self.match(Java20Parser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AnnotationInterfaceMemberDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def annotationInterfaceElementDeclaration(self):
            return self.getTypedRuleContext(Java20Parser.AnnotationInterfaceElementDeclarationContext,0)


        def constantDeclaration(self):
            return self.getTypedRuleContext(Java20Parser.ConstantDeclarationContext,0)


        def classDeclaration(self):
            return self.getTypedRuleContext(Java20Parser.ClassDeclarationContext,0)


        def interfaceDeclaration(self):
            return self.getTypedRuleContext(Java20Parser.InterfaceDeclarationContext,0)


        def SEMI(self):
            return self.getToken(Java20Parser.SEMI, 0)

        def getRuleIndex(self):
            return Java20Parser.RULE_annotationInterfaceMemberDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnnotationInterfaceMemberDeclaration" ):
                listener.enterAnnotationInterfaceMemberDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnnotationInterfaceMemberDeclaration" ):
                listener.exitAnnotationInterfaceMemberDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAnnotationInterfaceMemberDeclaration" ):
                return visitor.visitAnnotationInterfaceMemberDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def annotationInterfaceMemberDeclaration(self):

        localctx = Java20Parser.AnnotationInterfaceMemberDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 254, self.RULE_annotationInterfaceMemberDeclaration)
        try:
            self.state = 1594
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,168,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1589
                self.annotationInterfaceElementDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1590
                self.constantDeclaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1591
                self.classDeclaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1592
                self.interfaceDeclaration()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1593
                self.match(Java20Parser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AnnotationInterfaceElementDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unannType(self):
            return self.getTypedRuleContext(Java20Parser.UnannTypeContext,0)


        def identifier(self):
            return self.getTypedRuleContext(Java20Parser.IdentifierContext,0)


        def LPAREN(self):
            return self.getToken(Java20Parser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(Java20Parser.RPAREN, 0)

        def SEMI(self):
            return self.getToken(Java20Parser.SEMI, 0)

        def annotationInterfaceElementModifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.AnnotationInterfaceElementModifierContext)
            else:
                return self.getTypedRuleContext(Java20Parser.AnnotationInterfaceElementModifierContext,i)


        def dims(self):
            return self.getTypedRuleContext(Java20Parser.DimsContext,0)


        def defaultValue(self):
            return self.getTypedRuleContext(Java20Parser.DefaultValueContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_annotationInterfaceElementDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnnotationInterfaceElementDeclaration" ):
                listener.enterAnnotationInterfaceElementDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnnotationInterfaceElementDeclaration" ):
                listener.exitAnnotationInterfaceElementDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAnnotationInterfaceElementDeclaration" ):
                return visitor.visitAnnotationInterfaceElementDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def annotationInterfaceElementDeclaration(self):

        localctx = Java20Parser.AnnotationInterfaceElementDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 256, self.RULE_annotationInterfaceElementDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1599
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Java20Parser.ABSTRACT or _la==Java20Parser.PUBLIC or _la==Java20Parser.AT:
                self.state = 1596
                self.annotationInterfaceElementModifier()
                self.state = 1601
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1602
            self.unannType()
            self.state = 1603
            self.identifier()
            self.state = 1604
            self.match(Java20Parser.LPAREN)
            self.state = 1605
            self.match(Java20Parser.RPAREN)
            self.state = 1607
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Java20Parser.LBRACK or _la==Java20Parser.AT:
                self.state = 1606
                self.dims()


            self.state = 1610
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Java20Parser.DEFAULT:
                self.state = 1609
                self.defaultValue()


            self.state = 1612
            self.match(Java20Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AnnotationInterfaceElementModifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def annotation(self):
            return self.getTypedRuleContext(Java20Parser.AnnotationContext,0)


        def PUBLIC(self):
            return self.getToken(Java20Parser.PUBLIC, 0)

        def ABSTRACT(self):
            return self.getToken(Java20Parser.ABSTRACT, 0)

        def getRuleIndex(self):
            return Java20Parser.RULE_annotationInterfaceElementModifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnnotationInterfaceElementModifier" ):
                listener.enterAnnotationInterfaceElementModifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnnotationInterfaceElementModifier" ):
                listener.exitAnnotationInterfaceElementModifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAnnotationInterfaceElementModifier" ):
                return visitor.visitAnnotationInterfaceElementModifier(self)
            else:
                return visitor.visitChildren(self)




    def annotationInterfaceElementModifier(self):

        localctx = Java20Parser.AnnotationInterfaceElementModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 258, self.RULE_annotationInterfaceElementModifier)
        try:
            self.state = 1617
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Java20Parser.AT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1614
                self.annotation()
                pass
            elif token in [Java20Parser.PUBLIC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1615
                self.match(Java20Parser.PUBLIC)
                pass
            elif token in [Java20Parser.ABSTRACT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 1616
                self.match(Java20Parser.ABSTRACT)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefaultValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEFAULT(self):
            return self.getToken(Java20Parser.DEFAULT, 0)

        def elementValue(self):
            return self.getTypedRuleContext(Java20Parser.ElementValueContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_defaultValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefaultValue" ):
                listener.enterDefaultValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefaultValue" ):
                listener.exitDefaultValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefaultValue" ):
                return visitor.visitDefaultValue(self)
            else:
                return visitor.visitChildren(self)




    def defaultValue(self):

        localctx = Java20Parser.DefaultValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 260, self.RULE_defaultValue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1619
            self.match(Java20Parser.DEFAULT)
            self.state = 1620
            self.elementValue()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AnnotationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def normalAnnotation(self):
            return self.getTypedRuleContext(Java20Parser.NormalAnnotationContext,0)


        def markerAnnotation(self):
            return self.getTypedRuleContext(Java20Parser.MarkerAnnotationContext,0)


        def singleElementAnnotation(self):
            return self.getTypedRuleContext(Java20Parser.SingleElementAnnotationContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_annotation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnnotation" ):
                listener.enterAnnotation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnnotation" ):
                listener.exitAnnotation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAnnotation" ):
                return visitor.visitAnnotation(self)
            else:
                return visitor.visitChildren(self)




    def annotation(self):

        localctx = Java20Parser.AnnotationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 262, self.RULE_annotation)
        try:
            self.state = 1625
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,173,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1622
                self.normalAnnotation()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1623
                self.markerAnnotation()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1624
                self.singleElementAnnotation()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NormalAnnotationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AT(self):
            return self.getToken(Java20Parser.AT, 0)

        def typeName(self):
            return self.getTypedRuleContext(Java20Parser.TypeNameContext,0)


        def LPAREN(self):
            return self.getToken(Java20Parser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(Java20Parser.RPAREN, 0)

        def elementValuePairList(self):
            return self.getTypedRuleContext(Java20Parser.ElementValuePairListContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_normalAnnotation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNormalAnnotation" ):
                listener.enterNormalAnnotation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNormalAnnotation" ):
                listener.exitNormalAnnotation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNormalAnnotation" ):
                return visitor.visitNormalAnnotation(self)
            else:
                return visitor.visitChildren(self)




    def normalAnnotation(self):

        localctx = Java20Parser.NormalAnnotationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 264, self.RULE_normalAnnotation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1627
            self.match(Java20Parser.AT)
            self.state = 1628
            self.typeName()
            self.state = 1629
            self.match(Java20Parser.LPAREN)
            self.state = 1631
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java20Parser.EXPORTS) | (1 << Java20Parser.MODULE) | (1 << Java20Parser.NONSEALED) | (1 << Java20Parser.OPEN) | (1 << Java20Parser.OPENS) | (1 << Java20Parser.PERMITS) | (1 << Java20Parser.PROVIDES) | (1 << Java20Parser.RECORD) | (1 << Java20Parser.REQUIRES) | (1 << Java20Parser.SEALED) | (1 << Java20Parser.TO) | (1 << Java20Parser.TRANSITIVE) | (1 << Java20Parser.USES) | (1 << Java20Parser.VAR) | (1 << Java20Parser.WITH) | (1 << Java20Parser.YIELD))) != 0) or _la==Java20Parser.Identifier:
                self.state = 1630
                self.elementValuePairList()


            self.state = 1633
            self.match(Java20Parser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementValuePairListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elementValuePair(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.ElementValuePairContext)
            else:
                return self.getTypedRuleContext(Java20Parser.ElementValuePairContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(Java20Parser.COMMA)
            else:
                return self.getToken(Java20Parser.COMMA, i)

        def getRuleIndex(self):
            return Java20Parser.RULE_elementValuePairList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElementValuePairList" ):
                listener.enterElementValuePairList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElementValuePairList" ):
                listener.exitElementValuePairList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElementValuePairList" ):
                return visitor.visitElementValuePairList(self)
            else:
                return visitor.visitChildren(self)




    def elementValuePairList(self):

        localctx = Java20Parser.ElementValuePairListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 266, self.RULE_elementValuePairList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1635
            self.elementValuePair()
            self.state = 1640
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Java20Parser.COMMA:
                self.state = 1636
                self.match(Java20Parser.COMMA)
                self.state = 1637
                self.elementValuePair()
                self.state = 1642
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementValuePairContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(Java20Parser.IdentifierContext,0)


        def ASSIGN(self):
            return self.getToken(Java20Parser.ASSIGN, 0)

        def elementValue(self):
            return self.getTypedRuleContext(Java20Parser.ElementValueContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_elementValuePair

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElementValuePair" ):
                listener.enterElementValuePair(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElementValuePair" ):
                listener.exitElementValuePair(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElementValuePair" ):
                return visitor.visitElementValuePair(self)
            else:
                return visitor.visitChildren(self)




    def elementValuePair(self):

        localctx = Java20Parser.ElementValuePairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 268, self.RULE_elementValuePair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1643
            self.identifier()
            self.state = 1644
            self.match(Java20Parser.ASSIGN)
            self.state = 1645
            self.elementValue()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conditionalExpression(self):
            return self.getTypedRuleContext(Java20Parser.ConditionalExpressionContext,0)


        def elementValueArrayInitializer(self):
            return self.getTypedRuleContext(Java20Parser.ElementValueArrayInitializerContext,0)


        def annotation(self):
            return self.getTypedRuleContext(Java20Parser.AnnotationContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_elementValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElementValue" ):
                listener.enterElementValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElementValue" ):
                listener.exitElementValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElementValue" ):
                return visitor.visitElementValue(self)
            else:
                return visitor.visitChildren(self)




    def elementValue(self):

        localctx = Java20Parser.ElementValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 270, self.RULE_elementValue)
        try:
            self.state = 1650
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,176,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1647
                self.conditionalExpression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1648
                self.elementValueArrayInitializer()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1649
                self.annotation()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementValueArrayInitializerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(Java20Parser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(Java20Parser.RBRACE, 0)

        def elementValueList(self):
            return self.getTypedRuleContext(Java20Parser.ElementValueListContext,0)


        def COMMA(self):
            return self.getToken(Java20Parser.COMMA, 0)

        def getRuleIndex(self):
            return Java20Parser.RULE_elementValueArrayInitializer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElementValueArrayInitializer" ):
                listener.enterElementValueArrayInitializer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElementValueArrayInitializer" ):
                listener.exitElementValueArrayInitializer(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElementValueArrayInitializer" ):
                return visitor.visitElementValueArrayInitializer(self)
            else:
                return visitor.visitChildren(self)




    def elementValueArrayInitializer(self):

        localctx = Java20Parser.ElementValueArrayInitializerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 272, self.RULE_elementValueArrayInitializer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1652
            self.match(Java20Parser.LBRACE)
            self.state = 1654
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java20Parser.EXPORTS) | (1 << Java20Parser.MODULE) | (1 << Java20Parser.NONSEALED) | (1 << Java20Parser.OPEN) | (1 << Java20Parser.OPENS) | (1 << Java20Parser.PERMITS) | (1 << Java20Parser.PROVIDES) | (1 << Java20Parser.RECORD) | (1 << Java20Parser.REQUIRES) | (1 << Java20Parser.SEALED) | (1 << Java20Parser.TO) | (1 << Java20Parser.TRANSITIVE) | (1 << Java20Parser.USES) | (1 << Java20Parser.VAR) | (1 << Java20Parser.WITH) | (1 << Java20Parser.YIELD) | (1 << Java20Parser.BOOLEAN) | (1 << Java20Parser.BYTE) | (1 << Java20Parser.CHAR) | (1 << Java20Parser.DOUBLE) | (1 << Java20Parser.FLOAT) | (1 << Java20Parser.INT) | (1 << Java20Parser.LONG) | (1 << Java20Parser.NEW) | (1 << Java20Parser.SHORT) | (1 << Java20Parser.SUPER) | (1 << Java20Parser.SWITCH) | (1 << Java20Parser.THIS))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (Java20Parser.VOID - 65)) | (1 << (Java20Parser.IntegerLiteral - 65)) | (1 << (Java20Parser.FloatingPointLiteral - 65)) | (1 << (Java20Parser.BooleanLiteral - 65)) | (1 << (Java20Parser.CharacterLiteral - 65)) | (1 << (Java20Parser.StringLiteral - 65)) | (1 << (Java20Parser.TextBlock - 65)) | (1 << (Java20Parser.NullLiteral - 65)) | (1 << (Java20Parser.LPAREN - 65)) | (1 << (Java20Parser.LBRACE - 65)) | (1 << (Java20Parser.AT - 65)) | (1 << (Java20Parser.BANG - 65)) | (1 << (Java20Parser.TILDE - 65)) | (1 << (Java20Parser.INC - 65)) | (1 << (Java20Parser.DEC - 65)) | (1 << (Java20Parser.ADD - 65)) | (1 << (Java20Parser.SUB - 65)) | (1 << (Java20Parser.Identifier - 65)))) != 0):
                self.state = 1653
                self.elementValueList()


            self.state = 1657
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Java20Parser.COMMA:
                self.state = 1656
                self.match(Java20Parser.COMMA)


            self.state = 1659
            self.match(Java20Parser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementValueListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elementValue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.ElementValueContext)
            else:
                return self.getTypedRuleContext(Java20Parser.ElementValueContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(Java20Parser.COMMA)
            else:
                return self.getToken(Java20Parser.COMMA, i)

        def getRuleIndex(self):
            return Java20Parser.RULE_elementValueList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElementValueList" ):
                listener.enterElementValueList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElementValueList" ):
                listener.exitElementValueList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElementValueList" ):
                return visitor.visitElementValueList(self)
            else:
                return visitor.visitChildren(self)




    def elementValueList(self):

        localctx = Java20Parser.ElementValueListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 274, self.RULE_elementValueList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1661
            self.elementValue()
            self.state = 1666
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,179,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1662
                    self.match(Java20Parser.COMMA)
                    self.state = 1663
                    self.elementValue() 
                self.state = 1668
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,179,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MarkerAnnotationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AT(self):
            return self.getToken(Java20Parser.AT, 0)

        def typeName(self):
            return self.getTypedRuleContext(Java20Parser.TypeNameContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_markerAnnotation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMarkerAnnotation" ):
                listener.enterMarkerAnnotation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMarkerAnnotation" ):
                listener.exitMarkerAnnotation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMarkerAnnotation" ):
                return visitor.visitMarkerAnnotation(self)
            else:
                return visitor.visitChildren(self)




    def markerAnnotation(self):

        localctx = Java20Parser.MarkerAnnotationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 276, self.RULE_markerAnnotation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1669
            self.match(Java20Parser.AT)
            self.state = 1670
            self.typeName()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SingleElementAnnotationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AT(self):
            return self.getToken(Java20Parser.AT, 0)

        def typeName(self):
            return self.getTypedRuleContext(Java20Parser.TypeNameContext,0)


        def LPAREN(self):
            return self.getToken(Java20Parser.LPAREN, 0)

        def elementValue(self):
            return self.getTypedRuleContext(Java20Parser.ElementValueContext,0)


        def RPAREN(self):
            return self.getToken(Java20Parser.RPAREN, 0)

        def getRuleIndex(self):
            return Java20Parser.RULE_singleElementAnnotation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSingleElementAnnotation" ):
                listener.enterSingleElementAnnotation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSingleElementAnnotation" ):
                listener.exitSingleElementAnnotation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSingleElementAnnotation" ):
                return visitor.visitSingleElementAnnotation(self)
            else:
                return visitor.visitChildren(self)




    def singleElementAnnotation(self):

        localctx = Java20Parser.SingleElementAnnotationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 278, self.RULE_singleElementAnnotation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1672
            self.match(Java20Parser.AT)
            self.state = 1673
            self.typeName()
            self.state = 1674
            self.match(Java20Parser.LPAREN)
            self.state = 1675
            self.elementValue()
            self.state = 1676
            self.match(Java20Parser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayInitializerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(Java20Parser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(Java20Parser.RBRACE, 0)

        def variableInitializerList(self):
            return self.getTypedRuleContext(Java20Parser.VariableInitializerListContext,0)


        def COMMA(self):
            return self.getToken(Java20Parser.COMMA, 0)

        def getRuleIndex(self):
            return Java20Parser.RULE_arrayInitializer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayInitializer" ):
                listener.enterArrayInitializer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayInitializer" ):
                listener.exitArrayInitializer(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayInitializer" ):
                return visitor.visitArrayInitializer(self)
            else:
                return visitor.visitChildren(self)




    def arrayInitializer(self):

        localctx = Java20Parser.ArrayInitializerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 280, self.RULE_arrayInitializer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1678
            self.match(Java20Parser.LBRACE)
            self.state = 1680
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java20Parser.EXPORTS) | (1 << Java20Parser.MODULE) | (1 << Java20Parser.NONSEALED) | (1 << Java20Parser.OPEN) | (1 << Java20Parser.OPENS) | (1 << Java20Parser.PERMITS) | (1 << Java20Parser.PROVIDES) | (1 << Java20Parser.RECORD) | (1 << Java20Parser.REQUIRES) | (1 << Java20Parser.SEALED) | (1 << Java20Parser.TO) | (1 << Java20Parser.TRANSITIVE) | (1 << Java20Parser.USES) | (1 << Java20Parser.VAR) | (1 << Java20Parser.WITH) | (1 << Java20Parser.YIELD) | (1 << Java20Parser.BOOLEAN) | (1 << Java20Parser.BYTE) | (1 << Java20Parser.CHAR) | (1 << Java20Parser.DOUBLE) | (1 << Java20Parser.FLOAT) | (1 << Java20Parser.INT) | (1 << Java20Parser.LONG) | (1 << Java20Parser.NEW) | (1 << Java20Parser.SHORT) | (1 << Java20Parser.SUPER) | (1 << Java20Parser.SWITCH) | (1 << Java20Parser.THIS))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (Java20Parser.VOID - 65)) | (1 << (Java20Parser.IntegerLiteral - 65)) | (1 << (Java20Parser.FloatingPointLiteral - 65)) | (1 << (Java20Parser.BooleanLiteral - 65)) | (1 << (Java20Parser.CharacterLiteral - 65)) | (1 << (Java20Parser.StringLiteral - 65)) | (1 << (Java20Parser.TextBlock - 65)) | (1 << (Java20Parser.NullLiteral - 65)) | (1 << (Java20Parser.LPAREN - 65)) | (1 << (Java20Parser.LBRACE - 65)) | (1 << (Java20Parser.AT - 65)) | (1 << (Java20Parser.BANG - 65)) | (1 << (Java20Parser.TILDE - 65)) | (1 << (Java20Parser.INC - 65)) | (1 << (Java20Parser.DEC - 65)) | (1 << (Java20Parser.ADD - 65)) | (1 << (Java20Parser.SUB - 65)) | (1 << (Java20Parser.Identifier - 65)))) != 0):
                self.state = 1679
                self.variableInitializerList()


            self.state = 1683
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Java20Parser.COMMA:
                self.state = 1682
                self.match(Java20Parser.COMMA)


            self.state = 1685
            self.match(Java20Parser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableInitializerListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableInitializer(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.VariableInitializerContext)
            else:
                return self.getTypedRuleContext(Java20Parser.VariableInitializerContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(Java20Parser.COMMA)
            else:
                return self.getToken(Java20Parser.COMMA, i)

        def getRuleIndex(self):
            return Java20Parser.RULE_variableInitializerList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableInitializerList" ):
                listener.enterVariableInitializerList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableInitializerList" ):
                listener.exitVariableInitializerList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableInitializerList" ):
                return visitor.visitVariableInitializerList(self)
            else:
                return visitor.visitChildren(self)




    def variableInitializerList(self):

        localctx = Java20Parser.VariableInitializerListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 282, self.RULE_variableInitializerList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1687
            self.variableInitializer()
            self.state = 1692
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,182,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1688
                    self.match(Java20Parser.COMMA)
                    self.state = 1689
                    self.variableInitializer() 
                self.state = 1694
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,182,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(Java20Parser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(Java20Parser.RBRACE, 0)

        def blockStatements(self):
            return self.getTypedRuleContext(Java20Parser.BlockStatementsContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = Java20Parser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 284, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1695
            self.match(Java20Parser.LBRACE)
            self.state = 1697
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java20Parser.EXPORTS) | (1 << Java20Parser.MODULE) | (1 << Java20Parser.NONSEALED) | (1 << Java20Parser.OPEN) | (1 << Java20Parser.OPENS) | (1 << Java20Parser.PERMITS) | (1 << Java20Parser.PROVIDES) | (1 << Java20Parser.RECORD) | (1 << Java20Parser.REQUIRES) | (1 << Java20Parser.SEALED) | (1 << Java20Parser.TO) | (1 << Java20Parser.TRANSITIVE) | (1 << Java20Parser.USES) | (1 << Java20Parser.VAR) | (1 << Java20Parser.WITH) | (1 << Java20Parser.YIELD) | (1 << Java20Parser.ABSTRACT) | (1 << Java20Parser.ASSERT) | (1 << Java20Parser.BOOLEAN) | (1 << Java20Parser.BREAK) | (1 << Java20Parser.BYTE) | (1 << Java20Parser.CHAR) | (1 << Java20Parser.CLASS) | (1 << Java20Parser.CONTINUE) | (1 << Java20Parser.DO) | (1 << Java20Parser.DOUBLE) | (1 << Java20Parser.ENUM) | (1 << Java20Parser.FINAL) | (1 << Java20Parser.FLOAT) | (1 << Java20Parser.FOR) | (1 << Java20Parser.IF) | (1 << Java20Parser.INT) | (1 << Java20Parser.INTERFACE) | (1 << Java20Parser.LONG) | (1 << Java20Parser.NEW) | (1 << Java20Parser.PRIVATE) | (1 << Java20Parser.PROTECTED) | (1 << Java20Parser.PUBLIC) | (1 << Java20Parser.RETURN) | (1 << Java20Parser.SHORT) | (1 << Java20Parser.STATIC) | (1 << Java20Parser.STRICTFP) | (1 << Java20Parser.SUPER) | (1 << Java20Parser.SWITCH) | (1 << Java20Parser.SYNCHRONIZED) | (1 << Java20Parser.THIS) | (1 << Java20Parser.THROW))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (Java20Parser.TRY - 64)) | (1 << (Java20Parser.VOID - 64)) | (1 << (Java20Parser.WHILE - 64)) | (1 << (Java20Parser.IntegerLiteral - 64)) | (1 << (Java20Parser.FloatingPointLiteral - 64)) | (1 << (Java20Parser.BooleanLiteral - 64)) | (1 << (Java20Parser.CharacterLiteral - 64)) | (1 << (Java20Parser.StringLiteral - 64)) | (1 << (Java20Parser.TextBlock - 64)) | (1 << (Java20Parser.NullLiteral - 64)) | (1 << (Java20Parser.LPAREN - 64)) | (1 << (Java20Parser.LBRACE - 64)) | (1 << (Java20Parser.SEMI - 64)) | (1 << (Java20Parser.AT - 64)) | (1 << (Java20Parser.INC - 64)) | (1 << (Java20Parser.DEC - 64)) | (1 << (Java20Parser.Identifier - 64)))) != 0):
                self.state = 1696
                self.blockStatements()


            self.state = 1699
            self.match(Java20Parser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockStatementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def blockStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.BlockStatementContext)
            else:
                return self.getTypedRuleContext(Java20Parser.BlockStatementContext,i)


        def getRuleIndex(self):
            return Java20Parser.RULE_blockStatements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlockStatements" ):
                listener.enterBlockStatements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlockStatements" ):
                listener.exitBlockStatements(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockStatements" ):
                return visitor.visitBlockStatements(self)
            else:
                return visitor.visitChildren(self)




    def blockStatements(self):

        localctx = Java20Parser.BlockStatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 286, self.RULE_blockStatements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1701
            self.blockStatement()
            self.state = 1705
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java20Parser.EXPORTS) | (1 << Java20Parser.MODULE) | (1 << Java20Parser.NONSEALED) | (1 << Java20Parser.OPEN) | (1 << Java20Parser.OPENS) | (1 << Java20Parser.PERMITS) | (1 << Java20Parser.PROVIDES) | (1 << Java20Parser.RECORD) | (1 << Java20Parser.REQUIRES) | (1 << Java20Parser.SEALED) | (1 << Java20Parser.TO) | (1 << Java20Parser.TRANSITIVE) | (1 << Java20Parser.USES) | (1 << Java20Parser.VAR) | (1 << Java20Parser.WITH) | (1 << Java20Parser.YIELD) | (1 << Java20Parser.ABSTRACT) | (1 << Java20Parser.ASSERT) | (1 << Java20Parser.BOOLEAN) | (1 << Java20Parser.BREAK) | (1 << Java20Parser.BYTE) | (1 << Java20Parser.CHAR) | (1 << Java20Parser.CLASS) | (1 << Java20Parser.CONTINUE) | (1 << Java20Parser.DO) | (1 << Java20Parser.DOUBLE) | (1 << Java20Parser.ENUM) | (1 << Java20Parser.FINAL) | (1 << Java20Parser.FLOAT) | (1 << Java20Parser.FOR) | (1 << Java20Parser.IF) | (1 << Java20Parser.INT) | (1 << Java20Parser.INTERFACE) | (1 << Java20Parser.LONG) | (1 << Java20Parser.NEW) | (1 << Java20Parser.PRIVATE) | (1 << Java20Parser.PROTECTED) | (1 << Java20Parser.PUBLIC) | (1 << Java20Parser.RETURN) | (1 << Java20Parser.SHORT) | (1 << Java20Parser.STATIC) | (1 << Java20Parser.STRICTFP) | (1 << Java20Parser.SUPER) | (1 << Java20Parser.SWITCH) | (1 << Java20Parser.SYNCHRONIZED) | (1 << Java20Parser.THIS) | (1 << Java20Parser.THROW))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (Java20Parser.TRY - 64)) | (1 << (Java20Parser.VOID - 64)) | (1 << (Java20Parser.WHILE - 64)) | (1 << (Java20Parser.IntegerLiteral - 64)) | (1 << (Java20Parser.FloatingPointLiteral - 64)) | (1 << (Java20Parser.BooleanLiteral - 64)) | (1 << (Java20Parser.CharacterLiteral - 64)) | (1 << (Java20Parser.StringLiteral - 64)) | (1 << (Java20Parser.TextBlock - 64)) | (1 << (Java20Parser.NullLiteral - 64)) | (1 << (Java20Parser.LPAREN - 64)) | (1 << (Java20Parser.LBRACE - 64)) | (1 << (Java20Parser.SEMI - 64)) | (1 << (Java20Parser.AT - 64)) | (1 << (Java20Parser.INC - 64)) | (1 << (Java20Parser.DEC - 64)) | (1 << (Java20Parser.Identifier - 64)))) != 0):
                self.state = 1702
                self.blockStatement()
                self.state = 1707
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def localClassOrInterfaceDeclaration(self):
            return self.getTypedRuleContext(Java20Parser.LocalClassOrInterfaceDeclarationContext,0)


        def localVariableDeclarationStatement(self):
            return self.getTypedRuleContext(Java20Parser.LocalVariableDeclarationStatementContext,0)


        def statement(self):
            return self.getTypedRuleContext(Java20Parser.StatementContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_blockStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlockStatement" ):
                listener.enterBlockStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlockStatement" ):
                listener.exitBlockStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockStatement" ):
                return visitor.visitBlockStatement(self)
            else:
                return visitor.visitChildren(self)




    def blockStatement(self):

        localctx = Java20Parser.BlockStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 288, self.RULE_blockStatement)
        try:
            self.state = 1711
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,185,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1708
                self.localClassOrInterfaceDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1709
                self.localVariableDeclarationStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1710
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LocalClassOrInterfaceDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classDeclaration(self):
            return self.getTypedRuleContext(Java20Parser.ClassDeclarationContext,0)


        def normalInterfaceDeclaration(self):
            return self.getTypedRuleContext(Java20Parser.NormalInterfaceDeclarationContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_localClassOrInterfaceDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLocalClassOrInterfaceDeclaration" ):
                listener.enterLocalClassOrInterfaceDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLocalClassOrInterfaceDeclaration" ):
                listener.exitLocalClassOrInterfaceDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLocalClassOrInterfaceDeclaration" ):
                return visitor.visitLocalClassOrInterfaceDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def localClassOrInterfaceDeclaration(self):

        localctx = Java20Parser.LocalClassOrInterfaceDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 290, self.RULE_localClassOrInterfaceDeclaration)
        try:
            self.state = 1715
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,186,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1713
                self.classDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1714
                self.normalInterfaceDeclaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LocalVariableDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def localVariableType(self):
            return self.getTypedRuleContext(Java20Parser.LocalVariableTypeContext,0)


        def variableDeclaratorList(self):
            return self.getTypedRuleContext(Java20Parser.VariableDeclaratorListContext,0)


        def variableModifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.VariableModifierContext)
            else:
                return self.getTypedRuleContext(Java20Parser.VariableModifierContext,i)


        def getRuleIndex(self):
            return Java20Parser.RULE_localVariableDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLocalVariableDeclaration" ):
                listener.enterLocalVariableDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLocalVariableDeclaration" ):
                listener.exitLocalVariableDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLocalVariableDeclaration" ):
                return visitor.visitLocalVariableDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def localVariableDeclaration(self):

        localctx = Java20Parser.LocalVariableDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 292, self.RULE_localVariableDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1720
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Java20Parser.FINAL or _la==Java20Parser.AT:
                self.state = 1717
                self.variableModifier()
                self.state = 1722
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1723
            self.localVariableType()
            self.state = 1724
            self.variableDeclaratorList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LocalVariableTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unannType(self):
            return self.getTypedRuleContext(Java20Parser.UnannTypeContext,0)


        def VAR(self):
            return self.getToken(Java20Parser.VAR, 0)

        def getRuleIndex(self):
            return Java20Parser.RULE_localVariableType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLocalVariableType" ):
                listener.enterLocalVariableType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLocalVariableType" ):
                listener.exitLocalVariableType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLocalVariableType" ):
                return visitor.visitLocalVariableType(self)
            else:
                return visitor.visitChildren(self)




    def localVariableType(self):

        localctx = Java20Parser.LocalVariableTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 294, self.RULE_localVariableType)
        try:
            self.state = 1728
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,188,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1726
                self.unannType()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1727
                self.match(Java20Parser.VAR)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LocalVariableDeclarationStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def localVariableDeclaration(self):
            return self.getTypedRuleContext(Java20Parser.LocalVariableDeclarationContext,0)


        def SEMI(self):
            return self.getToken(Java20Parser.SEMI, 0)

        def getRuleIndex(self):
            return Java20Parser.RULE_localVariableDeclarationStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLocalVariableDeclarationStatement" ):
                listener.enterLocalVariableDeclarationStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLocalVariableDeclarationStatement" ):
                listener.exitLocalVariableDeclarationStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLocalVariableDeclarationStatement" ):
                return visitor.visitLocalVariableDeclarationStatement(self)
            else:
                return visitor.visitChildren(self)




    def localVariableDeclarationStatement(self):

        localctx = Java20Parser.LocalVariableDeclarationStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 296, self.RULE_localVariableDeclarationStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1730
            self.localVariableDeclaration()
            self.state = 1731
            self.match(Java20Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statementWithoutTrailingSubstatement(self):
            return self.getTypedRuleContext(Java20Parser.StatementWithoutTrailingSubstatementContext,0)


        def labeledStatement(self):
            return self.getTypedRuleContext(Java20Parser.LabeledStatementContext,0)


        def ifThenStatement(self):
            return self.getTypedRuleContext(Java20Parser.IfThenStatementContext,0)


        def ifThenElseStatement(self):
            return self.getTypedRuleContext(Java20Parser.IfThenElseStatementContext,0)


        def whileStatement(self):
            return self.getTypedRuleContext(Java20Parser.WhileStatementContext,0)


        def forStatement(self):
            return self.getTypedRuleContext(Java20Parser.ForStatementContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = Java20Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 298, self.RULE_statement)
        try:
            self.state = 1739
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,189,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1733
                self.statementWithoutTrailingSubstatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1734
                self.labeledStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1735
                self.ifThenStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1736
                self.ifThenElseStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1737
                self.whileStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 1738
                self.forStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementNoShortIfContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statementWithoutTrailingSubstatement(self):
            return self.getTypedRuleContext(Java20Parser.StatementWithoutTrailingSubstatementContext,0)


        def labeledStatementNoShortIf(self):
            return self.getTypedRuleContext(Java20Parser.LabeledStatementNoShortIfContext,0)


        def ifThenElseStatementNoShortIf(self):
            return self.getTypedRuleContext(Java20Parser.IfThenElseStatementNoShortIfContext,0)


        def whileStatementNoShortIf(self):
            return self.getTypedRuleContext(Java20Parser.WhileStatementNoShortIfContext,0)


        def forStatementNoShortIf(self):
            return self.getTypedRuleContext(Java20Parser.ForStatementNoShortIfContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_statementNoShortIf

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatementNoShortIf" ):
                listener.enterStatementNoShortIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatementNoShortIf" ):
                listener.exitStatementNoShortIf(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatementNoShortIf" ):
                return visitor.visitStatementNoShortIf(self)
            else:
                return visitor.visitChildren(self)




    def statementNoShortIf(self):

        localctx = Java20Parser.StatementNoShortIfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 300, self.RULE_statementNoShortIf)
        try:
            self.state = 1746
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,190,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1741
                self.statementWithoutTrailingSubstatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1742
                self.labeledStatementNoShortIf()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1743
                self.ifThenElseStatementNoShortIf()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1744
                self.whileStatementNoShortIf()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1745
                self.forStatementNoShortIf()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementWithoutTrailingSubstatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(Java20Parser.BlockContext,0)


        def emptyStatement_(self):
            return self.getTypedRuleContext(Java20Parser.EmptyStatement_Context,0)


        def expressionStatement(self):
            return self.getTypedRuleContext(Java20Parser.ExpressionStatementContext,0)


        def assertStatement(self):
            return self.getTypedRuleContext(Java20Parser.AssertStatementContext,0)


        def switchStatement(self):
            return self.getTypedRuleContext(Java20Parser.SwitchStatementContext,0)


        def doStatement(self):
            return self.getTypedRuleContext(Java20Parser.DoStatementContext,0)


        def breakStatement(self):
            return self.getTypedRuleContext(Java20Parser.BreakStatementContext,0)


        def continueStatement(self):
            return self.getTypedRuleContext(Java20Parser.ContinueStatementContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(Java20Parser.ReturnStatementContext,0)


        def synchronizedStatement(self):
            return self.getTypedRuleContext(Java20Parser.SynchronizedStatementContext,0)


        def throwStatement(self):
            return self.getTypedRuleContext(Java20Parser.ThrowStatementContext,0)


        def tryStatement(self):
            return self.getTypedRuleContext(Java20Parser.TryStatementContext,0)


        def yieldStatement(self):
            return self.getTypedRuleContext(Java20Parser.YieldStatementContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_statementWithoutTrailingSubstatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatementWithoutTrailingSubstatement" ):
                listener.enterStatementWithoutTrailingSubstatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatementWithoutTrailingSubstatement" ):
                listener.exitStatementWithoutTrailingSubstatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatementWithoutTrailingSubstatement" ):
                return visitor.visitStatementWithoutTrailingSubstatement(self)
            else:
                return visitor.visitChildren(self)




    def statementWithoutTrailingSubstatement(self):

        localctx = Java20Parser.StatementWithoutTrailingSubstatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 302, self.RULE_statementWithoutTrailingSubstatement)
        try:
            self.state = 1761
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,191,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1748
                self.block()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1749
                self.emptyStatement_()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1750
                self.expressionStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1751
                self.assertStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1752
                self.switchStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 1753
                self.doStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 1754
                self.breakStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 1755
                self.continueStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 1756
                self.returnStatement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 1757
                self.synchronizedStatement()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 1758
                self.throwStatement()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 1759
                self.tryStatement()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 1760
                self.yieldStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EmptyStatement_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(Java20Parser.SEMI, 0)

        def getRuleIndex(self):
            return Java20Parser.RULE_emptyStatement_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmptyStatement_" ):
                listener.enterEmptyStatement_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmptyStatement_" ):
                listener.exitEmptyStatement_(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEmptyStatement_" ):
                return visitor.visitEmptyStatement_(self)
            else:
                return visitor.visitChildren(self)




    def emptyStatement_(self):

        localctx = Java20Parser.EmptyStatement_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 304, self.RULE_emptyStatement_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1763
            self.match(Java20Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LabeledStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(Java20Parser.IdentifierContext,0)


        def COLON(self):
            return self.getToken(Java20Parser.COLON, 0)

        def statement(self):
            return self.getTypedRuleContext(Java20Parser.StatementContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_labeledStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabeledStatement" ):
                listener.enterLabeledStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabeledStatement" ):
                listener.exitLabeledStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLabeledStatement" ):
                return visitor.visitLabeledStatement(self)
            else:
                return visitor.visitChildren(self)




    def labeledStatement(self):

        localctx = Java20Parser.LabeledStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 306, self.RULE_labeledStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1765
            self.identifier()
            self.state = 1766
            self.match(Java20Parser.COLON)
            self.state = 1767
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LabeledStatementNoShortIfContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(Java20Parser.IdentifierContext,0)


        def COLON(self):
            return self.getToken(Java20Parser.COLON, 0)

        def statementNoShortIf(self):
            return self.getTypedRuleContext(Java20Parser.StatementNoShortIfContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_labeledStatementNoShortIf

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabeledStatementNoShortIf" ):
                listener.enterLabeledStatementNoShortIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabeledStatementNoShortIf" ):
                listener.exitLabeledStatementNoShortIf(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLabeledStatementNoShortIf" ):
                return visitor.visitLabeledStatementNoShortIf(self)
            else:
                return visitor.visitChildren(self)




    def labeledStatementNoShortIf(self):

        localctx = Java20Parser.LabeledStatementNoShortIfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 308, self.RULE_labeledStatementNoShortIf)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1769
            self.identifier()
            self.state = 1770
            self.match(Java20Parser.COLON)
            self.state = 1771
            self.statementNoShortIf()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statementExpression(self):
            return self.getTypedRuleContext(Java20Parser.StatementExpressionContext,0)


        def SEMI(self):
            return self.getToken(Java20Parser.SEMI, 0)

        def getRuleIndex(self):
            return Java20Parser.RULE_expressionStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionStatement" ):
                listener.enterExpressionStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionStatement" ):
                listener.exitExpressionStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionStatement" ):
                return visitor.visitExpressionStatement(self)
            else:
                return visitor.visitChildren(self)




    def expressionStatement(self):

        localctx = Java20Parser.ExpressionStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 310, self.RULE_expressionStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1773
            self.statementExpression()
            self.state = 1774
            self.match(Java20Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(Java20Parser.AssignmentContext,0)


        def preIncrementExpression(self):
            return self.getTypedRuleContext(Java20Parser.PreIncrementExpressionContext,0)


        def preDecrementExpression(self):
            return self.getTypedRuleContext(Java20Parser.PreDecrementExpressionContext,0)


        def postIncrementExpression(self):
            return self.getTypedRuleContext(Java20Parser.PostIncrementExpressionContext,0)


        def postDecrementExpression(self):
            return self.getTypedRuleContext(Java20Parser.PostDecrementExpressionContext,0)


        def methodInvocation(self):
            return self.getTypedRuleContext(Java20Parser.MethodInvocationContext,0)


        def classInstanceCreationExpression(self):
            return self.getTypedRuleContext(Java20Parser.ClassInstanceCreationExpressionContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_statementExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatementExpression" ):
                listener.enterStatementExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatementExpression" ):
                listener.exitStatementExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatementExpression" ):
                return visitor.visitStatementExpression(self)
            else:
                return visitor.visitChildren(self)




    def statementExpression(self):

        localctx = Java20Parser.StatementExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 312, self.RULE_statementExpression)
        try:
            self.state = 1783
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,192,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1776
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1777
                self.preIncrementExpression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1778
                self.preDecrementExpression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1779
                self.postIncrementExpression()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1780
                self.postDecrementExpression()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 1781
                self.methodInvocation()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 1782
                self.classInstanceCreationExpression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfThenStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(Java20Parser.IF, 0)

        def LPAREN(self):
            return self.getToken(Java20Parser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(Java20Parser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(Java20Parser.RPAREN, 0)

        def statement(self):
            return self.getTypedRuleContext(Java20Parser.StatementContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_ifThenStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfThenStatement" ):
                listener.enterIfThenStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfThenStatement" ):
                listener.exitIfThenStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfThenStatement" ):
                return visitor.visitIfThenStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifThenStatement(self):

        localctx = Java20Parser.IfThenStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 314, self.RULE_ifThenStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1785
            self.match(Java20Parser.IF)
            self.state = 1786
            self.match(Java20Parser.LPAREN)
            self.state = 1787
            self.expression()
            self.state = 1788
            self.match(Java20Parser.RPAREN)
            self.state = 1789
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfThenElseStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(Java20Parser.IF, 0)

        def LPAREN(self):
            return self.getToken(Java20Parser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(Java20Parser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(Java20Parser.RPAREN, 0)

        def statementNoShortIf(self):
            return self.getTypedRuleContext(Java20Parser.StatementNoShortIfContext,0)


        def ELSE(self):
            return self.getToken(Java20Parser.ELSE, 0)

        def statement(self):
            return self.getTypedRuleContext(Java20Parser.StatementContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_ifThenElseStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfThenElseStatement" ):
                listener.enterIfThenElseStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfThenElseStatement" ):
                listener.exitIfThenElseStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfThenElseStatement" ):
                return visitor.visitIfThenElseStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifThenElseStatement(self):

        localctx = Java20Parser.IfThenElseStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 316, self.RULE_ifThenElseStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1791
            self.match(Java20Parser.IF)
            self.state = 1792
            self.match(Java20Parser.LPAREN)
            self.state = 1793
            self.expression()
            self.state = 1794
            self.match(Java20Parser.RPAREN)
            self.state = 1795
            self.statementNoShortIf()
            self.state = 1796
            self.match(Java20Parser.ELSE)
            self.state = 1797
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfThenElseStatementNoShortIfContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(Java20Parser.IF, 0)

        def LPAREN(self):
            return self.getToken(Java20Parser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(Java20Parser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(Java20Parser.RPAREN, 0)

        def statementNoShortIf(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.StatementNoShortIfContext)
            else:
                return self.getTypedRuleContext(Java20Parser.StatementNoShortIfContext,i)


        def ELSE(self):
            return self.getToken(Java20Parser.ELSE, 0)

        def getRuleIndex(self):
            return Java20Parser.RULE_ifThenElseStatementNoShortIf

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfThenElseStatementNoShortIf" ):
                listener.enterIfThenElseStatementNoShortIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfThenElseStatementNoShortIf" ):
                listener.exitIfThenElseStatementNoShortIf(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfThenElseStatementNoShortIf" ):
                return visitor.visitIfThenElseStatementNoShortIf(self)
            else:
                return visitor.visitChildren(self)




    def ifThenElseStatementNoShortIf(self):

        localctx = Java20Parser.IfThenElseStatementNoShortIfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 318, self.RULE_ifThenElseStatementNoShortIf)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1799
            self.match(Java20Parser.IF)
            self.state = 1800
            self.match(Java20Parser.LPAREN)
            self.state = 1801
            self.expression()
            self.state = 1802
            self.match(Java20Parser.RPAREN)
            self.state = 1803
            self.statementNoShortIf()
            self.state = 1804
            self.match(Java20Parser.ELSE)
            self.state = 1805
            self.statementNoShortIf()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssertStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSERT(self):
            return self.getToken(Java20Parser.ASSERT, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(Java20Parser.ExpressionContext,i)


        def SEMI(self):
            return self.getToken(Java20Parser.SEMI, 0)

        def COLON(self):
            return self.getToken(Java20Parser.COLON, 0)

        def getRuleIndex(self):
            return Java20Parser.RULE_assertStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssertStatement" ):
                listener.enterAssertStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssertStatement" ):
                listener.exitAssertStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssertStatement" ):
                return visitor.visitAssertStatement(self)
            else:
                return visitor.visitChildren(self)




    def assertStatement(self):

        localctx = Java20Parser.AssertStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 320, self.RULE_assertStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1807
            self.match(Java20Parser.ASSERT)
            self.state = 1808
            self.expression()
            self.state = 1811
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Java20Parser.COLON:
                self.state = 1809
                self.match(Java20Parser.COLON)
                self.state = 1810
                self.expression()


            self.state = 1813
            self.match(Java20Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SwitchStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SWITCH(self):
            return self.getToken(Java20Parser.SWITCH, 0)

        def LPAREN(self):
            return self.getToken(Java20Parser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(Java20Parser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(Java20Parser.RPAREN, 0)

        def switchBlock(self):
            return self.getTypedRuleContext(Java20Parser.SwitchBlockContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_switchStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitchStatement" ):
                listener.enterSwitchStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitchStatement" ):
                listener.exitSwitchStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSwitchStatement" ):
                return visitor.visitSwitchStatement(self)
            else:
                return visitor.visitChildren(self)




    def switchStatement(self):

        localctx = Java20Parser.SwitchStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 322, self.RULE_switchStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1815
            self.match(Java20Parser.SWITCH)
            self.state = 1816
            self.match(Java20Parser.LPAREN)
            self.state = 1817
            self.expression()
            self.state = 1818
            self.match(Java20Parser.RPAREN)
            self.state = 1819
            self.switchBlock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SwitchBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(Java20Parser.LBRACE, 0)

        def switchRule(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.SwitchRuleContext)
            else:
                return self.getTypedRuleContext(Java20Parser.SwitchRuleContext,i)


        def RBRACE(self):
            return self.getToken(Java20Parser.RBRACE, 0)

        def switchBlockStatementGroup(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.SwitchBlockStatementGroupContext)
            else:
                return self.getTypedRuleContext(Java20Parser.SwitchBlockStatementGroupContext,i)


        def switchLabel(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.SwitchLabelContext)
            else:
                return self.getTypedRuleContext(Java20Parser.SwitchLabelContext,i)


        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(Java20Parser.COLON)
            else:
                return self.getToken(Java20Parser.COLON, i)

        def getRuleIndex(self):
            return Java20Parser.RULE_switchBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitchBlock" ):
                listener.enterSwitchBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitchBlock" ):
                listener.exitSwitchBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSwitchBlock" ):
                return visitor.visitSwitchBlock(self)
            else:
                return visitor.visitChildren(self)




    def switchBlock(self):

        localctx = Java20Parser.SwitchBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 324, self.RULE_switchBlock)
        self._la = 0 # Token type
        try:
            self.state = 1847
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,197,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1821
                self.match(Java20Parser.LBRACE)
                self.state = 1822
                self.switchRule()
                self.state = 1826
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==Java20Parser.CASE or _la==Java20Parser.DEFAULT:
                    self.state = 1823
                    self.switchRule()
                    self.state = 1828
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 1829
                self.match(Java20Parser.RBRACE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1831
                self.match(Java20Parser.LBRACE)
                self.state = 1835
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,195,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 1832
                        self.switchBlockStatementGroup() 
                    self.state = 1837
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,195,self._ctx)

                self.state = 1843
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==Java20Parser.CASE or _la==Java20Parser.DEFAULT:
                    self.state = 1838
                    self.switchLabel()
                    self.state = 1839
                    self.match(Java20Parser.COLON)
                    self.state = 1845
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 1846
                self.match(Java20Parser.RBRACE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SwitchRuleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def switchLabel(self):
            return self.getTypedRuleContext(Java20Parser.SwitchLabelContext,0)


        def ARROW(self):
            return self.getToken(Java20Parser.ARROW, 0)

        def expression(self):
            return self.getTypedRuleContext(Java20Parser.ExpressionContext,0)


        def SEMI(self):
            return self.getToken(Java20Parser.SEMI, 0)

        def block(self):
            return self.getTypedRuleContext(Java20Parser.BlockContext,0)


        def throwStatement(self):
            return self.getTypedRuleContext(Java20Parser.ThrowStatementContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_switchRule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitchRule" ):
                listener.enterSwitchRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitchRule" ):
                listener.exitSwitchRule(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSwitchRule" ):
                return visitor.visitSwitchRule(self)
            else:
                return visitor.visitChildren(self)




    def switchRule(self):

        localctx = Java20Parser.SwitchRuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 326, self.RULE_switchRule)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1849
            self.switchLabel()
            self.state = 1850
            self.match(Java20Parser.ARROW)
            self.state = 1856
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Java20Parser.EXPORTS, Java20Parser.MODULE, Java20Parser.NONSEALED, Java20Parser.OPEN, Java20Parser.OPENS, Java20Parser.PERMITS, Java20Parser.PROVIDES, Java20Parser.RECORD, Java20Parser.REQUIRES, Java20Parser.SEALED, Java20Parser.TO, Java20Parser.TRANSITIVE, Java20Parser.USES, Java20Parser.VAR, Java20Parser.WITH, Java20Parser.YIELD, Java20Parser.BOOLEAN, Java20Parser.BYTE, Java20Parser.CHAR, Java20Parser.DOUBLE, Java20Parser.FLOAT, Java20Parser.INT, Java20Parser.LONG, Java20Parser.NEW, Java20Parser.SHORT, Java20Parser.SUPER, Java20Parser.SWITCH, Java20Parser.THIS, Java20Parser.VOID, Java20Parser.IntegerLiteral, Java20Parser.FloatingPointLiteral, Java20Parser.BooleanLiteral, Java20Parser.CharacterLiteral, Java20Parser.StringLiteral, Java20Parser.TextBlock, Java20Parser.NullLiteral, Java20Parser.LPAREN, Java20Parser.AT, Java20Parser.BANG, Java20Parser.TILDE, Java20Parser.INC, Java20Parser.DEC, Java20Parser.ADD, Java20Parser.SUB, Java20Parser.Identifier]:
                self.state = 1851
                self.expression()
                self.state = 1852
                self.match(Java20Parser.SEMI)
                pass
            elif token in [Java20Parser.LBRACE]:
                self.state = 1854
                self.block()
                pass
            elif token in [Java20Parser.THROW]:
                self.state = 1855
                self.throwStatement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SwitchBlockStatementGroupContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def switchLabel(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.SwitchLabelContext)
            else:
                return self.getTypedRuleContext(Java20Parser.SwitchLabelContext,i)


        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(Java20Parser.COLON)
            else:
                return self.getToken(Java20Parser.COLON, i)

        def blockStatements(self):
            return self.getTypedRuleContext(Java20Parser.BlockStatementsContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_switchBlockStatementGroup

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitchBlockStatementGroup" ):
                listener.enterSwitchBlockStatementGroup(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitchBlockStatementGroup" ):
                listener.exitSwitchBlockStatementGroup(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSwitchBlockStatementGroup" ):
                return visitor.visitSwitchBlockStatementGroup(self)
            else:
                return visitor.visitChildren(self)




    def switchBlockStatementGroup(self):

        localctx = Java20Parser.SwitchBlockStatementGroupContext(self, self._ctx, self.state)
        self.enterRule(localctx, 328, self.RULE_switchBlockStatementGroup)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1858
            self.switchLabel()
            self.state = 1859
            self.match(Java20Parser.COLON)
            self.state = 1865
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Java20Parser.CASE or _la==Java20Parser.DEFAULT:
                self.state = 1860
                self.switchLabel()
                self.state = 1861
                self.match(Java20Parser.COLON)
                self.state = 1867
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1868
            self.blockStatements()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SwitchLabelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CASE(self):
            return self.getToken(Java20Parser.CASE, 0)

        def caseConstant(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.CaseConstantContext)
            else:
                return self.getTypedRuleContext(Java20Parser.CaseConstantContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(Java20Parser.COMMA)
            else:
                return self.getToken(Java20Parser.COMMA, i)

        def DEFAULT(self):
            return self.getToken(Java20Parser.DEFAULT, 0)

        def getRuleIndex(self):
            return Java20Parser.RULE_switchLabel

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitchLabel" ):
                listener.enterSwitchLabel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitchLabel" ):
                listener.exitSwitchLabel(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSwitchLabel" ):
                return visitor.visitSwitchLabel(self)
            else:
                return visitor.visitChildren(self)




    def switchLabel(self):

        localctx = Java20Parser.SwitchLabelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 330, self.RULE_switchLabel)
        self._la = 0 # Token type
        try:
            self.state = 1880
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Java20Parser.CASE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1870
                self.match(Java20Parser.CASE)
                self.state = 1871
                self.caseConstant()
                self.state = 1876
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==Java20Parser.COMMA:
                    self.state = 1872
                    self.match(Java20Parser.COMMA)
                    self.state = 1873
                    self.caseConstant()
                    self.state = 1878
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [Java20Parser.DEFAULT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1879
                self.match(Java20Parser.DEFAULT)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CaseConstantContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conditionalExpression(self):
            return self.getTypedRuleContext(Java20Parser.ConditionalExpressionContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_caseConstant

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCaseConstant" ):
                listener.enterCaseConstant(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCaseConstant" ):
                listener.exitCaseConstant(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCaseConstant" ):
                return visitor.visitCaseConstant(self)
            else:
                return visitor.visitChildren(self)




    def caseConstant(self):

        localctx = Java20Parser.CaseConstantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 332, self.RULE_caseConstant)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1882
            self.conditionalExpression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(Java20Parser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(Java20Parser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(Java20Parser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(Java20Parser.RPAREN, 0)

        def statement(self):
            return self.getTypedRuleContext(Java20Parser.StatementContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_whileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStatement" ):
                return visitor.visitWhileStatement(self)
            else:
                return visitor.visitChildren(self)




    def whileStatement(self):

        localctx = Java20Parser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 334, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1884
            self.match(Java20Parser.WHILE)
            self.state = 1885
            self.match(Java20Parser.LPAREN)
            self.state = 1886
            self.expression()
            self.state = 1887
            self.match(Java20Parser.RPAREN)
            self.state = 1888
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStatementNoShortIfContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(Java20Parser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(Java20Parser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(Java20Parser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(Java20Parser.RPAREN, 0)

        def statementNoShortIf(self):
            return self.getTypedRuleContext(Java20Parser.StatementNoShortIfContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_whileStatementNoShortIf

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatementNoShortIf" ):
                listener.enterWhileStatementNoShortIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatementNoShortIf" ):
                listener.exitWhileStatementNoShortIf(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStatementNoShortIf" ):
                return visitor.visitWhileStatementNoShortIf(self)
            else:
                return visitor.visitChildren(self)




    def whileStatementNoShortIf(self):

        localctx = Java20Parser.WhileStatementNoShortIfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 336, self.RULE_whileStatementNoShortIf)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1890
            self.match(Java20Parser.WHILE)
            self.state = 1891
            self.match(Java20Parser.LPAREN)
            self.state = 1892
            self.expression()
            self.state = 1893
            self.match(Java20Parser.RPAREN)
            self.state = 1894
            self.statementNoShortIf()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DoStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(Java20Parser.DO, 0)

        def statement(self):
            return self.getTypedRuleContext(Java20Parser.StatementContext,0)


        def WHILE(self):
            return self.getToken(Java20Parser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(Java20Parser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(Java20Parser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(Java20Parser.RPAREN, 0)

        def SEMI(self):
            return self.getToken(Java20Parser.SEMI, 0)

        def getRuleIndex(self):
            return Java20Parser.RULE_doStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDoStatement" ):
                listener.enterDoStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDoStatement" ):
                listener.exitDoStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDoStatement" ):
                return visitor.visitDoStatement(self)
            else:
                return visitor.visitChildren(self)




    def doStatement(self):

        localctx = Java20Parser.DoStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 338, self.RULE_doStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1896
            self.match(Java20Parser.DO)
            self.state = 1897
            self.statement()
            self.state = 1898
            self.match(Java20Parser.WHILE)
            self.state = 1899
            self.match(Java20Parser.LPAREN)
            self.state = 1900
            self.expression()
            self.state = 1901
            self.match(Java20Parser.RPAREN)
            self.state = 1902
            self.match(Java20Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def basicForStatement(self):
            return self.getTypedRuleContext(Java20Parser.BasicForStatementContext,0)


        def enhancedForStatement(self):
            return self.getTypedRuleContext(Java20Parser.EnhancedForStatementContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_forStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStatement" ):
                listener.enterForStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStatement" ):
                listener.exitForStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStatement" ):
                return visitor.visitForStatement(self)
            else:
                return visitor.visitChildren(self)




    def forStatement(self):

        localctx = Java20Parser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 340, self.RULE_forStatement)
        try:
            self.state = 1906
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,202,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1904
                self.basicForStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1905
                self.enhancedForStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStatementNoShortIfContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def basicForStatementNoShortIf(self):
            return self.getTypedRuleContext(Java20Parser.BasicForStatementNoShortIfContext,0)


        def enhancedForStatementNoShortIf(self):
            return self.getTypedRuleContext(Java20Parser.EnhancedForStatementNoShortIfContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_forStatementNoShortIf

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStatementNoShortIf" ):
                listener.enterForStatementNoShortIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStatementNoShortIf" ):
                listener.exitForStatementNoShortIf(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStatementNoShortIf" ):
                return visitor.visitForStatementNoShortIf(self)
            else:
                return visitor.visitChildren(self)




    def forStatementNoShortIf(self):

        localctx = Java20Parser.ForStatementNoShortIfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 342, self.RULE_forStatementNoShortIf)
        try:
            self.state = 1910
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,203,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1908
                self.basicForStatementNoShortIf()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1909
                self.enhancedForStatementNoShortIf()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BasicForStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(Java20Parser.FOR, 0)

        def LPAREN(self):
            return self.getToken(Java20Parser.LPAREN, 0)

        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(Java20Parser.SEMI)
            else:
                return self.getToken(Java20Parser.SEMI, i)

        def RPAREN(self):
            return self.getToken(Java20Parser.RPAREN, 0)

        def statement(self):
            return self.getTypedRuleContext(Java20Parser.StatementContext,0)


        def forInit(self):
            return self.getTypedRuleContext(Java20Parser.ForInitContext,0)


        def expression(self):
            return self.getTypedRuleContext(Java20Parser.ExpressionContext,0)


        def forUpdate(self):
            return self.getTypedRuleContext(Java20Parser.ForUpdateContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_basicForStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBasicForStatement" ):
                listener.enterBasicForStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBasicForStatement" ):
                listener.exitBasicForStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBasicForStatement" ):
                return visitor.visitBasicForStatement(self)
            else:
                return visitor.visitChildren(self)




    def basicForStatement(self):

        localctx = Java20Parser.BasicForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 344, self.RULE_basicForStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1912
            self.match(Java20Parser.FOR)
            self.state = 1913
            self.match(Java20Parser.LPAREN)
            self.state = 1915
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java20Parser.EXPORTS) | (1 << Java20Parser.MODULE) | (1 << Java20Parser.NONSEALED) | (1 << Java20Parser.OPEN) | (1 << Java20Parser.OPENS) | (1 << Java20Parser.PERMITS) | (1 << Java20Parser.PROVIDES) | (1 << Java20Parser.RECORD) | (1 << Java20Parser.REQUIRES) | (1 << Java20Parser.SEALED) | (1 << Java20Parser.TO) | (1 << Java20Parser.TRANSITIVE) | (1 << Java20Parser.USES) | (1 << Java20Parser.VAR) | (1 << Java20Parser.WITH) | (1 << Java20Parser.YIELD) | (1 << Java20Parser.BOOLEAN) | (1 << Java20Parser.BYTE) | (1 << Java20Parser.CHAR) | (1 << Java20Parser.DOUBLE) | (1 << Java20Parser.FINAL) | (1 << Java20Parser.FLOAT) | (1 << Java20Parser.INT) | (1 << Java20Parser.LONG) | (1 << Java20Parser.NEW) | (1 << Java20Parser.SHORT) | (1 << Java20Parser.SUPER) | (1 << Java20Parser.THIS))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (Java20Parser.VOID - 65)) | (1 << (Java20Parser.IntegerLiteral - 65)) | (1 << (Java20Parser.FloatingPointLiteral - 65)) | (1 << (Java20Parser.BooleanLiteral - 65)) | (1 << (Java20Parser.CharacterLiteral - 65)) | (1 << (Java20Parser.StringLiteral - 65)) | (1 << (Java20Parser.TextBlock - 65)) | (1 << (Java20Parser.NullLiteral - 65)) | (1 << (Java20Parser.LPAREN - 65)) | (1 << (Java20Parser.AT - 65)) | (1 << (Java20Parser.INC - 65)) | (1 << (Java20Parser.DEC - 65)) | (1 << (Java20Parser.Identifier - 65)))) != 0):
                self.state = 1914
                self.forInit()


            self.state = 1917
            self.match(Java20Parser.SEMI)
            self.state = 1919
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java20Parser.EXPORTS) | (1 << Java20Parser.MODULE) | (1 << Java20Parser.NONSEALED) | (1 << Java20Parser.OPEN) | (1 << Java20Parser.OPENS) | (1 << Java20Parser.PERMITS) | (1 << Java20Parser.PROVIDES) | (1 << Java20Parser.RECORD) | (1 << Java20Parser.REQUIRES) | (1 << Java20Parser.SEALED) | (1 << Java20Parser.TO) | (1 << Java20Parser.TRANSITIVE) | (1 << Java20Parser.USES) | (1 << Java20Parser.VAR) | (1 << Java20Parser.WITH) | (1 << Java20Parser.YIELD) | (1 << Java20Parser.BOOLEAN) | (1 << Java20Parser.BYTE) | (1 << Java20Parser.CHAR) | (1 << Java20Parser.DOUBLE) | (1 << Java20Parser.FLOAT) | (1 << Java20Parser.INT) | (1 << Java20Parser.LONG) | (1 << Java20Parser.NEW) | (1 << Java20Parser.SHORT) | (1 << Java20Parser.SUPER) | (1 << Java20Parser.SWITCH) | (1 << Java20Parser.THIS))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (Java20Parser.VOID - 65)) | (1 << (Java20Parser.IntegerLiteral - 65)) | (1 << (Java20Parser.FloatingPointLiteral - 65)) | (1 << (Java20Parser.BooleanLiteral - 65)) | (1 << (Java20Parser.CharacterLiteral - 65)) | (1 << (Java20Parser.StringLiteral - 65)) | (1 << (Java20Parser.TextBlock - 65)) | (1 << (Java20Parser.NullLiteral - 65)) | (1 << (Java20Parser.LPAREN - 65)) | (1 << (Java20Parser.AT - 65)) | (1 << (Java20Parser.BANG - 65)) | (1 << (Java20Parser.TILDE - 65)) | (1 << (Java20Parser.INC - 65)) | (1 << (Java20Parser.DEC - 65)) | (1 << (Java20Parser.ADD - 65)) | (1 << (Java20Parser.SUB - 65)) | (1 << (Java20Parser.Identifier - 65)))) != 0):
                self.state = 1918
                self.expression()


            self.state = 1921
            self.match(Java20Parser.SEMI)
            self.state = 1923
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java20Parser.EXPORTS) | (1 << Java20Parser.MODULE) | (1 << Java20Parser.NONSEALED) | (1 << Java20Parser.OPEN) | (1 << Java20Parser.OPENS) | (1 << Java20Parser.PERMITS) | (1 << Java20Parser.PROVIDES) | (1 << Java20Parser.RECORD) | (1 << Java20Parser.REQUIRES) | (1 << Java20Parser.SEALED) | (1 << Java20Parser.TO) | (1 << Java20Parser.TRANSITIVE) | (1 << Java20Parser.USES) | (1 << Java20Parser.VAR) | (1 << Java20Parser.WITH) | (1 << Java20Parser.YIELD) | (1 << Java20Parser.BOOLEAN) | (1 << Java20Parser.BYTE) | (1 << Java20Parser.CHAR) | (1 << Java20Parser.DOUBLE) | (1 << Java20Parser.FLOAT) | (1 << Java20Parser.INT) | (1 << Java20Parser.LONG) | (1 << Java20Parser.NEW) | (1 << Java20Parser.SHORT) | (1 << Java20Parser.SUPER) | (1 << Java20Parser.THIS))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (Java20Parser.VOID - 65)) | (1 << (Java20Parser.IntegerLiteral - 65)) | (1 << (Java20Parser.FloatingPointLiteral - 65)) | (1 << (Java20Parser.BooleanLiteral - 65)) | (1 << (Java20Parser.CharacterLiteral - 65)) | (1 << (Java20Parser.StringLiteral - 65)) | (1 << (Java20Parser.TextBlock - 65)) | (1 << (Java20Parser.NullLiteral - 65)) | (1 << (Java20Parser.LPAREN - 65)) | (1 << (Java20Parser.AT - 65)) | (1 << (Java20Parser.INC - 65)) | (1 << (Java20Parser.DEC - 65)) | (1 << (Java20Parser.Identifier - 65)))) != 0):
                self.state = 1922
                self.forUpdate()


            self.state = 1925
            self.match(Java20Parser.RPAREN)
            self.state = 1926
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BasicForStatementNoShortIfContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(Java20Parser.FOR, 0)

        def LPAREN(self):
            return self.getToken(Java20Parser.LPAREN, 0)

        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(Java20Parser.SEMI)
            else:
                return self.getToken(Java20Parser.SEMI, i)

        def RPAREN(self):
            return self.getToken(Java20Parser.RPAREN, 0)

        def statementNoShortIf(self):
            return self.getTypedRuleContext(Java20Parser.StatementNoShortIfContext,0)


        def forInit(self):
            return self.getTypedRuleContext(Java20Parser.ForInitContext,0)


        def expression(self):
            return self.getTypedRuleContext(Java20Parser.ExpressionContext,0)


        def forUpdate(self):
            return self.getTypedRuleContext(Java20Parser.ForUpdateContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_basicForStatementNoShortIf

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBasicForStatementNoShortIf" ):
                listener.enterBasicForStatementNoShortIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBasicForStatementNoShortIf" ):
                listener.exitBasicForStatementNoShortIf(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBasicForStatementNoShortIf" ):
                return visitor.visitBasicForStatementNoShortIf(self)
            else:
                return visitor.visitChildren(self)




    def basicForStatementNoShortIf(self):

        localctx = Java20Parser.BasicForStatementNoShortIfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 346, self.RULE_basicForStatementNoShortIf)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1928
            self.match(Java20Parser.FOR)
            self.state = 1929
            self.match(Java20Parser.LPAREN)
            self.state = 1931
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java20Parser.EXPORTS) | (1 << Java20Parser.MODULE) | (1 << Java20Parser.NONSEALED) | (1 << Java20Parser.OPEN) | (1 << Java20Parser.OPENS) | (1 << Java20Parser.PERMITS) | (1 << Java20Parser.PROVIDES) | (1 << Java20Parser.RECORD) | (1 << Java20Parser.REQUIRES) | (1 << Java20Parser.SEALED) | (1 << Java20Parser.TO) | (1 << Java20Parser.TRANSITIVE) | (1 << Java20Parser.USES) | (1 << Java20Parser.VAR) | (1 << Java20Parser.WITH) | (1 << Java20Parser.YIELD) | (1 << Java20Parser.BOOLEAN) | (1 << Java20Parser.BYTE) | (1 << Java20Parser.CHAR) | (1 << Java20Parser.DOUBLE) | (1 << Java20Parser.FINAL) | (1 << Java20Parser.FLOAT) | (1 << Java20Parser.INT) | (1 << Java20Parser.LONG) | (1 << Java20Parser.NEW) | (1 << Java20Parser.SHORT) | (1 << Java20Parser.SUPER) | (1 << Java20Parser.THIS))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (Java20Parser.VOID - 65)) | (1 << (Java20Parser.IntegerLiteral - 65)) | (1 << (Java20Parser.FloatingPointLiteral - 65)) | (1 << (Java20Parser.BooleanLiteral - 65)) | (1 << (Java20Parser.CharacterLiteral - 65)) | (1 << (Java20Parser.StringLiteral - 65)) | (1 << (Java20Parser.TextBlock - 65)) | (1 << (Java20Parser.NullLiteral - 65)) | (1 << (Java20Parser.LPAREN - 65)) | (1 << (Java20Parser.AT - 65)) | (1 << (Java20Parser.INC - 65)) | (1 << (Java20Parser.DEC - 65)) | (1 << (Java20Parser.Identifier - 65)))) != 0):
                self.state = 1930
                self.forInit()


            self.state = 1933
            self.match(Java20Parser.SEMI)
            self.state = 1935
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java20Parser.EXPORTS) | (1 << Java20Parser.MODULE) | (1 << Java20Parser.NONSEALED) | (1 << Java20Parser.OPEN) | (1 << Java20Parser.OPENS) | (1 << Java20Parser.PERMITS) | (1 << Java20Parser.PROVIDES) | (1 << Java20Parser.RECORD) | (1 << Java20Parser.REQUIRES) | (1 << Java20Parser.SEALED) | (1 << Java20Parser.TO) | (1 << Java20Parser.TRANSITIVE) | (1 << Java20Parser.USES) | (1 << Java20Parser.VAR) | (1 << Java20Parser.WITH) | (1 << Java20Parser.YIELD) | (1 << Java20Parser.BOOLEAN) | (1 << Java20Parser.BYTE) | (1 << Java20Parser.CHAR) | (1 << Java20Parser.DOUBLE) | (1 << Java20Parser.FLOAT) | (1 << Java20Parser.INT) | (1 << Java20Parser.LONG) | (1 << Java20Parser.NEW) | (1 << Java20Parser.SHORT) | (1 << Java20Parser.SUPER) | (1 << Java20Parser.SWITCH) | (1 << Java20Parser.THIS))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (Java20Parser.VOID - 65)) | (1 << (Java20Parser.IntegerLiteral - 65)) | (1 << (Java20Parser.FloatingPointLiteral - 65)) | (1 << (Java20Parser.BooleanLiteral - 65)) | (1 << (Java20Parser.CharacterLiteral - 65)) | (1 << (Java20Parser.StringLiteral - 65)) | (1 << (Java20Parser.TextBlock - 65)) | (1 << (Java20Parser.NullLiteral - 65)) | (1 << (Java20Parser.LPAREN - 65)) | (1 << (Java20Parser.AT - 65)) | (1 << (Java20Parser.BANG - 65)) | (1 << (Java20Parser.TILDE - 65)) | (1 << (Java20Parser.INC - 65)) | (1 << (Java20Parser.DEC - 65)) | (1 << (Java20Parser.ADD - 65)) | (1 << (Java20Parser.SUB - 65)) | (1 << (Java20Parser.Identifier - 65)))) != 0):
                self.state = 1934
                self.expression()


            self.state = 1937
            self.match(Java20Parser.SEMI)
            self.state = 1939
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java20Parser.EXPORTS) | (1 << Java20Parser.MODULE) | (1 << Java20Parser.NONSEALED) | (1 << Java20Parser.OPEN) | (1 << Java20Parser.OPENS) | (1 << Java20Parser.PERMITS) | (1 << Java20Parser.PROVIDES) | (1 << Java20Parser.RECORD) | (1 << Java20Parser.REQUIRES) | (1 << Java20Parser.SEALED) | (1 << Java20Parser.TO) | (1 << Java20Parser.TRANSITIVE) | (1 << Java20Parser.USES) | (1 << Java20Parser.VAR) | (1 << Java20Parser.WITH) | (1 << Java20Parser.YIELD) | (1 << Java20Parser.BOOLEAN) | (1 << Java20Parser.BYTE) | (1 << Java20Parser.CHAR) | (1 << Java20Parser.DOUBLE) | (1 << Java20Parser.FLOAT) | (1 << Java20Parser.INT) | (1 << Java20Parser.LONG) | (1 << Java20Parser.NEW) | (1 << Java20Parser.SHORT) | (1 << Java20Parser.SUPER) | (1 << Java20Parser.THIS))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (Java20Parser.VOID - 65)) | (1 << (Java20Parser.IntegerLiteral - 65)) | (1 << (Java20Parser.FloatingPointLiteral - 65)) | (1 << (Java20Parser.BooleanLiteral - 65)) | (1 << (Java20Parser.CharacterLiteral - 65)) | (1 << (Java20Parser.StringLiteral - 65)) | (1 << (Java20Parser.TextBlock - 65)) | (1 << (Java20Parser.NullLiteral - 65)) | (1 << (Java20Parser.LPAREN - 65)) | (1 << (Java20Parser.AT - 65)) | (1 << (Java20Parser.INC - 65)) | (1 << (Java20Parser.DEC - 65)) | (1 << (Java20Parser.Identifier - 65)))) != 0):
                self.state = 1938
                self.forUpdate()


            self.state = 1941
            self.match(Java20Parser.RPAREN)
            self.state = 1942
            self.statementNoShortIf()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForInitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statementExpressionList(self):
            return self.getTypedRuleContext(Java20Parser.StatementExpressionListContext,0)


        def localVariableDeclaration(self):
            return self.getTypedRuleContext(Java20Parser.LocalVariableDeclarationContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_forInit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForInit" ):
                listener.enterForInit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForInit" ):
                listener.exitForInit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForInit" ):
                return visitor.visitForInit(self)
            else:
                return visitor.visitChildren(self)




    def forInit(self):

        localctx = Java20Parser.ForInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 348, self.RULE_forInit)
        try:
            self.state = 1946
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,210,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1944
                self.statementExpressionList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1945
                self.localVariableDeclaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForUpdateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statementExpressionList(self):
            return self.getTypedRuleContext(Java20Parser.StatementExpressionListContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_forUpdate

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForUpdate" ):
                listener.enterForUpdate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForUpdate" ):
                listener.exitForUpdate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForUpdate" ):
                return visitor.visitForUpdate(self)
            else:
                return visitor.visitChildren(self)




    def forUpdate(self):

        localctx = Java20Parser.ForUpdateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 350, self.RULE_forUpdate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1948
            self.statementExpressionList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementExpressionListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statementExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.StatementExpressionContext)
            else:
                return self.getTypedRuleContext(Java20Parser.StatementExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(Java20Parser.COMMA)
            else:
                return self.getToken(Java20Parser.COMMA, i)

        def getRuleIndex(self):
            return Java20Parser.RULE_statementExpressionList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatementExpressionList" ):
                listener.enterStatementExpressionList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatementExpressionList" ):
                listener.exitStatementExpressionList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatementExpressionList" ):
                return visitor.visitStatementExpressionList(self)
            else:
                return visitor.visitChildren(self)




    def statementExpressionList(self):

        localctx = Java20Parser.StatementExpressionListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 352, self.RULE_statementExpressionList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1950
            self.statementExpression()
            self.state = 1955
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Java20Parser.COMMA:
                self.state = 1951
                self.match(Java20Parser.COMMA)
                self.state = 1952
                self.statementExpression()
                self.state = 1957
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EnhancedForStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(Java20Parser.FOR, 0)

        def LPAREN(self):
            return self.getToken(Java20Parser.LPAREN, 0)

        def localVariableDeclaration(self):
            return self.getTypedRuleContext(Java20Parser.LocalVariableDeclarationContext,0)


        def COLON(self):
            return self.getToken(Java20Parser.COLON, 0)

        def expression(self):
            return self.getTypedRuleContext(Java20Parser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(Java20Parser.RPAREN, 0)

        def statement(self):
            return self.getTypedRuleContext(Java20Parser.StatementContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_enhancedForStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnhancedForStatement" ):
                listener.enterEnhancedForStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnhancedForStatement" ):
                listener.exitEnhancedForStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnhancedForStatement" ):
                return visitor.visitEnhancedForStatement(self)
            else:
                return visitor.visitChildren(self)




    def enhancedForStatement(self):

        localctx = Java20Parser.EnhancedForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 354, self.RULE_enhancedForStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1958
            self.match(Java20Parser.FOR)
            self.state = 1959
            self.match(Java20Parser.LPAREN)
            self.state = 1960
            self.localVariableDeclaration()
            self.state = 1961
            self.match(Java20Parser.COLON)
            self.state = 1962
            self.expression()
            self.state = 1963
            self.match(Java20Parser.RPAREN)
            self.state = 1964
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EnhancedForStatementNoShortIfContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(Java20Parser.FOR, 0)

        def LPAREN(self):
            return self.getToken(Java20Parser.LPAREN, 0)

        def localVariableDeclaration(self):
            return self.getTypedRuleContext(Java20Parser.LocalVariableDeclarationContext,0)


        def COLON(self):
            return self.getToken(Java20Parser.COLON, 0)

        def expression(self):
            return self.getTypedRuleContext(Java20Parser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(Java20Parser.RPAREN, 0)

        def statementNoShortIf(self):
            return self.getTypedRuleContext(Java20Parser.StatementNoShortIfContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_enhancedForStatementNoShortIf

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnhancedForStatementNoShortIf" ):
                listener.enterEnhancedForStatementNoShortIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnhancedForStatementNoShortIf" ):
                listener.exitEnhancedForStatementNoShortIf(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnhancedForStatementNoShortIf" ):
                return visitor.visitEnhancedForStatementNoShortIf(self)
            else:
                return visitor.visitChildren(self)




    def enhancedForStatementNoShortIf(self):

        localctx = Java20Parser.EnhancedForStatementNoShortIfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 356, self.RULE_enhancedForStatementNoShortIf)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1966
            self.match(Java20Parser.FOR)
            self.state = 1967
            self.match(Java20Parser.LPAREN)
            self.state = 1968
            self.localVariableDeclaration()
            self.state = 1969
            self.match(Java20Parser.COLON)
            self.state = 1970
            self.expression()
            self.state = 1971
            self.match(Java20Parser.RPAREN)
            self.state = 1972
            self.statementNoShortIf()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(Java20Parser.BREAK, 0)

        def SEMI(self):
            return self.getToken(Java20Parser.SEMI, 0)

        def identifier(self):
            return self.getTypedRuleContext(Java20Parser.IdentifierContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_breakStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreakStatement" ):
                listener.enterBreakStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreakStatement" ):
                listener.exitBreakStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakStatement" ):
                return visitor.visitBreakStatement(self)
            else:
                return visitor.visitChildren(self)




    def breakStatement(self):

        localctx = Java20Parser.BreakStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 358, self.RULE_breakStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1974
            self.match(Java20Parser.BREAK)
            self.state = 1976
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java20Parser.EXPORTS) | (1 << Java20Parser.MODULE) | (1 << Java20Parser.NONSEALED) | (1 << Java20Parser.OPEN) | (1 << Java20Parser.OPENS) | (1 << Java20Parser.PERMITS) | (1 << Java20Parser.PROVIDES) | (1 << Java20Parser.RECORD) | (1 << Java20Parser.REQUIRES) | (1 << Java20Parser.SEALED) | (1 << Java20Parser.TO) | (1 << Java20Parser.TRANSITIVE) | (1 << Java20Parser.USES) | (1 << Java20Parser.VAR) | (1 << Java20Parser.WITH) | (1 << Java20Parser.YIELD))) != 0) or _la==Java20Parser.Identifier:
                self.state = 1975
                self.identifier()


            self.state = 1978
            self.match(Java20Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinueStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(Java20Parser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(Java20Parser.SEMI, 0)

        def identifier(self):
            return self.getTypedRuleContext(Java20Parser.IdentifierContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_continueStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContinueStatement" ):
                listener.enterContinueStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContinueStatement" ):
                listener.exitContinueStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinueStatement" ):
                return visitor.visitContinueStatement(self)
            else:
                return visitor.visitChildren(self)




    def continueStatement(self):

        localctx = Java20Parser.ContinueStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 360, self.RULE_continueStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1980
            self.match(Java20Parser.CONTINUE)
            self.state = 1982
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java20Parser.EXPORTS) | (1 << Java20Parser.MODULE) | (1 << Java20Parser.NONSEALED) | (1 << Java20Parser.OPEN) | (1 << Java20Parser.OPENS) | (1 << Java20Parser.PERMITS) | (1 << Java20Parser.PROVIDES) | (1 << Java20Parser.RECORD) | (1 << Java20Parser.REQUIRES) | (1 << Java20Parser.SEALED) | (1 << Java20Parser.TO) | (1 << Java20Parser.TRANSITIVE) | (1 << Java20Parser.USES) | (1 << Java20Parser.VAR) | (1 << Java20Parser.WITH) | (1 << Java20Parser.YIELD))) != 0) or _la==Java20Parser.Identifier:
                self.state = 1981
                self.identifier()


            self.state = 1984
            self.match(Java20Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(Java20Parser.RETURN, 0)

        def SEMI(self):
            return self.getToken(Java20Parser.SEMI, 0)

        def expression(self):
            return self.getTypedRuleContext(Java20Parser.ExpressionContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_returnStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStatement" ):
                listener.enterReturnStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStatement" ):
                listener.exitReturnStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStatement" ):
                return visitor.visitReturnStatement(self)
            else:
                return visitor.visitChildren(self)




    def returnStatement(self):

        localctx = Java20Parser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 362, self.RULE_returnStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1986
            self.match(Java20Parser.RETURN)
            self.state = 1988
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java20Parser.EXPORTS) | (1 << Java20Parser.MODULE) | (1 << Java20Parser.NONSEALED) | (1 << Java20Parser.OPEN) | (1 << Java20Parser.OPENS) | (1 << Java20Parser.PERMITS) | (1 << Java20Parser.PROVIDES) | (1 << Java20Parser.RECORD) | (1 << Java20Parser.REQUIRES) | (1 << Java20Parser.SEALED) | (1 << Java20Parser.TO) | (1 << Java20Parser.TRANSITIVE) | (1 << Java20Parser.USES) | (1 << Java20Parser.VAR) | (1 << Java20Parser.WITH) | (1 << Java20Parser.YIELD) | (1 << Java20Parser.BOOLEAN) | (1 << Java20Parser.BYTE) | (1 << Java20Parser.CHAR) | (1 << Java20Parser.DOUBLE) | (1 << Java20Parser.FLOAT) | (1 << Java20Parser.INT) | (1 << Java20Parser.LONG) | (1 << Java20Parser.NEW) | (1 << Java20Parser.SHORT) | (1 << Java20Parser.SUPER) | (1 << Java20Parser.SWITCH) | (1 << Java20Parser.THIS))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (Java20Parser.VOID - 65)) | (1 << (Java20Parser.IntegerLiteral - 65)) | (1 << (Java20Parser.FloatingPointLiteral - 65)) | (1 << (Java20Parser.BooleanLiteral - 65)) | (1 << (Java20Parser.CharacterLiteral - 65)) | (1 << (Java20Parser.StringLiteral - 65)) | (1 << (Java20Parser.TextBlock - 65)) | (1 << (Java20Parser.NullLiteral - 65)) | (1 << (Java20Parser.LPAREN - 65)) | (1 << (Java20Parser.AT - 65)) | (1 << (Java20Parser.BANG - 65)) | (1 << (Java20Parser.TILDE - 65)) | (1 << (Java20Parser.INC - 65)) | (1 << (Java20Parser.DEC - 65)) | (1 << (Java20Parser.ADD - 65)) | (1 << (Java20Parser.SUB - 65)) | (1 << (Java20Parser.Identifier - 65)))) != 0):
                self.state = 1987
                self.expression()


            self.state = 1990
            self.match(Java20Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ThrowStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def THROW(self):
            return self.getToken(Java20Parser.THROW, 0)

        def expression(self):
            return self.getTypedRuleContext(Java20Parser.ExpressionContext,0)


        def SEMI(self):
            return self.getToken(Java20Parser.SEMI, 0)

        def getRuleIndex(self):
            return Java20Parser.RULE_throwStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterThrowStatement" ):
                listener.enterThrowStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitThrowStatement" ):
                listener.exitThrowStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitThrowStatement" ):
                return visitor.visitThrowStatement(self)
            else:
                return visitor.visitChildren(self)




    def throwStatement(self):

        localctx = Java20Parser.ThrowStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 364, self.RULE_throwStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1992
            self.match(Java20Parser.THROW)
            self.state = 1993
            self.expression()
            self.state = 1994
            self.match(Java20Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SynchronizedStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SYNCHRONIZED(self):
            return self.getToken(Java20Parser.SYNCHRONIZED, 0)

        def LPAREN(self):
            return self.getToken(Java20Parser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(Java20Parser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(Java20Parser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(Java20Parser.BlockContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_synchronizedStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSynchronizedStatement" ):
                listener.enterSynchronizedStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSynchronizedStatement" ):
                listener.exitSynchronizedStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSynchronizedStatement" ):
                return visitor.visitSynchronizedStatement(self)
            else:
                return visitor.visitChildren(self)




    def synchronizedStatement(self):

        localctx = Java20Parser.SynchronizedStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 366, self.RULE_synchronizedStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1996
            self.match(Java20Parser.SYNCHRONIZED)
            self.state = 1997
            self.match(Java20Parser.LPAREN)
            self.state = 1998
            self.expression()
            self.state = 1999
            self.match(Java20Parser.RPAREN)
            self.state = 2000
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TryStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRY(self):
            return self.getToken(Java20Parser.TRY, 0)

        def block(self):
            return self.getTypedRuleContext(Java20Parser.BlockContext,0)


        def catches(self):
            return self.getTypedRuleContext(Java20Parser.CatchesContext,0)


        def finallyBlock(self):
            return self.getTypedRuleContext(Java20Parser.FinallyBlockContext,0)


        def tryWithResourcesStatement(self):
            return self.getTypedRuleContext(Java20Parser.TryWithResourcesStatementContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_tryStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTryStatement" ):
                listener.enterTryStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTryStatement" ):
                listener.exitTryStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTryStatement" ):
                return visitor.visitTryStatement(self)
            else:
                return visitor.visitChildren(self)




    def tryStatement(self):

        localctx = Java20Parser.TryStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 368, self.RULE_tryStatement)
        self._la = 0 # Token type
        try:
            self.state = 2018
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,216,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2002
                self.match(Java20Parser.TRY)
                self.state = 2003
                self.block()
                self.state = 2004
                self.catches()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2006
                self.match(Java20Parser.TRY)
                self.state = 2007
                self.block()
                self.state = 2008
                self.finallyBlock()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2010
                self.match(Java20Parser.TRY)
                self.state = 2011
                self.block()
                self.state = 2013
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Java20Parser.CATCH:
                    self.state = 2012
                    self.catches()


                self.state = 2015
                self.finallyBlock()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 2017
                self.tryWithResourcesStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CatchesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def catchClause(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.CatchClauseContext)
            else:
                return self.getTypedRuleContext(Java20Parser.CatchClauseContext,i)


        def getRuleIndex(self):
            return Java20Parser.RULE_catches

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCatches" ):
                listener.enterCatches(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCatches" ):
                listener.exitCatches(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCatches" ):
                return visitor.visitCatches(self)
            else:
                return visitor.visitChildren(self)




    def catches(self):

        localctx = Java20Parser.CatchesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 370, self.RULE_catches)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2020
            self.catchClause()
            self.state = 2024
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Java20Parser.CATCH:
                self.state = 2021
                self.catchClause()
                self.state = 2026
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CatchClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CATCH(self):
            return self.getToken(Java20Parser.CATCH, 0)

        def LPAREN(self):
            return self.getToken(Java20Parser.LPAREN, 0)

        def catchFormalParameter(self):
            return self.getTypedRuleContext(Java20Parser.CatchFormalParameterContext,0)


        def RPAREN(self):
            return self.getToken(Java20Parser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(Java20Parser.BlockContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_catchClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCatchClause" ):
                listener.enterCatchClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCatchClause" ):
                listener.exitCatchClause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCatchClause" ):
                return visitor.visitCatchClause(self)
            else:
                return visitor.visitChildren(self)




    def catchClause(self):

        localctx = Java20Parser.CatchClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 372, self.RULE_catchClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2027
            self.match(Java20Parser.CATCH)
            self.state = 2028
            self.match(Java20Parser.LPAREN)
            self.state = 2029
            self.catchFormalParameter()
            self.state = 2030
            self.match(Java20Parser.RPAREN)
            self.state = 2031
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CatchFormalParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def catchType(self):
            return self.getTypedRuleContext(Java20Parser.CatchTypeContext,0)


        def variableDeclaratorId(self):
            return self.getTypedRuleContext(Java20Parser.VariableDeclaratorIdContext,0)


        def variableModifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.VariableModifierContext)
            else:
                return self.getTypedRuleContext(Java20Parser.VariableModifierContext,i)


        def getRuleIndex(self):
            return Java20Parser.RULE_catchFormalParameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCatchFormalParameter" ):
                listener.enterCatchFormalParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCatchFormalParameter" ):
                listener.exitCatchFormalParameter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCatchFormalParameter" ):
                return visitor.visitCatchFormalParameter(self)
            else:
                return visitor.visitChildren(self)




    def catchFormalParameter(self):

        localctx = Java20Parser.CatchFormalParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 374, self.RULE_catchFormalParameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2036
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Java20Parser.FINAL or _la==Java20Parser.AT:
                self.state = 2033
                self.variableModifier()
                self.state = 2038
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 2039
            self.catchType()
            self.state = 2040
            self.variableDeclaratorId()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CatchTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unannClassType(self):
            return self.getTypedRuleContext(Java20Parser.UnannClassTypeContext,0)


        def BITOR(self, i:int=None):
            if i is None:
                return self.getTokens(Java20Parser.BITOR)
            else:
                return self.getToken(Java20Parser.BITOR, i)

        def classType(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.ClassTypeContext)
            else:
                return self.getTypedRuleContext(Java20Parser.ClassTypeContext,i)


        def getRuleIndex(self):
            return Java20Parser.RULE_catchType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCatchType" ):
                listener.enterCatchType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCatchType" ):
                listener.exitCatchType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCatchType" ):
                return visitor.visitCatchType(self)
            else:
                return visitor.visitChildren(self)




    def catchType(self):

        localctx = Java20Parser.CatchTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 376, self.RULE_catchType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2042
            self.unannClassType()
            self.state = 2047
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Java20Parser.BITOR:
                self.state = 2043
                self.match(Java20Parser.BITOR)
                self.state = 2044
                self.classType()
                self.state = 2049
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FinallyBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FINALLY(self):
            return self.getToken(Java20Parser.FINALLY, 0)

        def block(self):
            return self.getTypedRuleContext(Java20Parser.BlockContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_finallyBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFinallyBlock" ):
                listener.enterFinallyBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFinallyBlock" ):
                listener.exitFinallyBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFinallyBlock" ):
                return visitor.visitFinallyBlock(self)
            else:
                return visitor.visitChildren(self)




    def finallyBlock(self):

        localctx = Java20Parser.FinallyBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 378, self.RULE_finallyBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2050
            self.match(Java20Parser.FINALLY)
            self.state = 2051
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TryWithResourcesStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRY(self):
            return self.getToken(Java20Parser.TRY, 0)

        def resourceSpecification(self):
            return self.getTypedRuleContext(Java20Parser.ResourceSpecificationContext,0)


        def block(self):
            return self.getTypedRuleContext(Java20Parser.BlockContext,0)


        def catches(self):
            return self.getTypedRuleContext(Java20Parser.CatchesContext,0)


        def finallyBlock(self):
            return self.getTypedRuleContext(Java20Parser.FinallyBlockContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_tryWithResourcesStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTryWithResourcesStatement" ):
                listener.enterTryWithResourcesStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTryWithResourcesStatement" ):
                listener.exitTryWithResourcesStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTryWithResourcesStatement" ):
                return visitor.visitTryWithResourcesStatement(self)
            else:
                return visitor.visitChildren(self)




    def tryWithResourcesStatement(self):

        localctx = Java20Parser.TryWithResourcesStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 380, self.RULE_tryWithResourcesStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2053
            self.match(Java20Parser.TRY)
            self.state = 2054
            self.resourceSpecification()
            self.state = 2055
            self.block()
            self.state = 2057
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Java20Parser.CATCH:
                self.state = 2056
                self.catches()


            self.state = 2060
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Java20Parser.FINALLY:
                self.state = 2059
                self.finallyBlock()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ResourceSpecificationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(Java20Parser.LPAREN, 0)

        def resourceList(self):
            return self.getTypedRuleContext(Java20Parser.ResourceListContext,0)


        def RPAREN(self):
            return self.getToken(Java20Parser.RPAREN, 0)

        def SEMI(self):
            return self.getToken(Java20Parser.SEMI, 0)

        def getRuleIndex(self):
            return Java20Parser.RULE_resourceSpecification

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterResourceSpecification" ):
                listener.enterResourceSpecification(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitResourceSpecification" ):
                listener.exitResourceSpecification(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitResourceSpecification" ):
                return visitor.visitResourceSpecification(self)
            else:
                return visitor.visitChildren(self)




    def resourceSpecification(self):

        localctx = Java20Parser.ResourceSpecificationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 382, self.RULE_resourceSpecification)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2062
            self.match(Java20Parser.LPAREN)
            self.state = 2063
            self.resourceList()
            self.state = 2065
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Java20Parser.SEMI:
                self.state = 2064
                self.match(Java20Parser.SEMI)


            self.state = 2067
            self.match(Java20Parser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ResourceListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def resource(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.ResourceContext)
            else:
                return self.getTypedRuleContext(Java20Parser.ResourceContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(Java20Parser.SEMI)
            else:
                return self.getToken(Java20Parser.SEMI, i)

        def getRuleIndex(self):
            return Java20Parser.RULE_resourceList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterResourceList" ):
                listener.enterResourceList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitResourceList" ):
                listener.exitResourceList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitResourceList" ):
                return visitor.visitResourceList(self)
            else:
                return visitor.visitChildren(self)




    def resourceList(self):

        localctx = Java20Parser.ResourceListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 384, self.RULE_resourceList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2069
            self.resource()
            self.state = 2074
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,223,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 2070
                    self.match(Java20Parser.SEMI)
                    self.state = 2071
                    self.resource() 
                self.state = 2076
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,223,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ResourceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def localVariableDeclaration(self):
            return self.getTypedRuleContext(Java20Parser.LocalVariableDeclarationContext,0)


        def variableAccess(self):
            return self.getTypedRuleContext(Java20Parser.VariableAccessContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_resource

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterResource" ):
                listener.enterResource(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitResource" ):
                listener.exitResource(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitResource" ):
                return visitor.visitResource(self)
            else:
                return visitor.visitChildren(self)




    def resource(self):

        localctx = Java20Parser.ResourceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 386, self.RULE_resource)
        try:
            self.state = 2079
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,224,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2077
                self.localVariableDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2078
                self.variableAccess()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableAccessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressionName(self):
            return self.getTypedRuleContext(Java20Parser.ExpressionNameContext,0)


        def fieldAccess(self):
            return self.getTypedRuleContext(Java20Parser.FieldAccessContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_variableAccess

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableAccess" ):
                listener.enterVariableAccess(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableAccess" ):
                listener.exitVariableAccess(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableAccess" ):
                return visitor.visitVariableAccess(self)
            else:
                return visitor.visitChildren(self)




    def variableAccess(self):

        localctx = Java20Parser.VariableAccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 388, self.RULE_variableAccess)
        try:
            self.state = 2083
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,225,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2081
                self.expressionName()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2082
                self.fieldAccess()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class YieldStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def YIELD(self):
            return self.getToken(Java20Parser.YIELD, 0)

        def expression(self):
            return self.getTypedRuleContext(Java20Parser.ExpressionContext,0)


        def SEMI(self):
            return self.getToken(Java20Parser.SEMI, 0)

        def getRuleIndex(self):
            return Java20Parser.RULE_yieldStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterYieldStatement" ):
                listener.enterYieldStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitYieldStatement" ):
                listener.exitYieldStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitYieldStatement" ):
                return visitor.visitYieldStatement(self)
            else:
                return visitor.visitChildren(self)




    def yieldStatement(self):

        localctx = Java20Parser.YieldStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 390, self.RULE_yieldStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2085
            self.match(Java20Parser.YIELD)
            self.state = 2086
            self.expression()
            self.state = 2087
            self.match(Java20Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PatternContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typePattern(self):
            return self.getTypedRuleContext(Java20Parser.TypePatternContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_pattern

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPattern" ):
                listener.enterPattern(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPattern" ):
                listener.exitPattern(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPattern" ):
                return visitor.visitPattern(self)
            else:
                return visitor.visitChildren(self)




    def pattern(self):

        localctx = Java20Parser.PatternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 392, self.RULE_pattern)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2089
            self.typePattern()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypePatternContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def localVariableDeclaration(self):
            return self.getTypedRuleContext(Java20Parser.LocalVariableDeclarationContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_typePattern

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypePattern" ):
                listener.enterTypePattern(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypePattern" ):
                listener.exitTypePattern(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypePattern" ):
                return visitor.visitTypePattern(self)
            else:
                return visitor.visitChildren(self)




    def typePattern(self):

        localctx = Java20Parser.TypePatternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 394, self.RULE_typePattern)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2091
            self.localVariableDeclaration()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lambdaExpression(self):
            return self.getTypedRuleContext(Java20Parser.LambdaExpressionContext,0)


        def assignmentExpression(self):
            return self.getTypedRuleContext(Java20Parser.AssignmentExpressionContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = Java20Parser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 396, self.RULE_expression)
        try:
            self.state = 2095
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,226,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2093
                self.lambdaExpression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2094
                self.assignmentExpression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primaryNoNewArray(self):
            return self.getTypedRuleContext(Java20Parser.PrimaryNoNewArrayContext,0)


        def arrayCreationExpression(self):
            return self.getTypedRuleContext(Java20Parser.ArrayCreationExpressionContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_primary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary" ):
                listener.enterPrimary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary" ):
                listener.exitPrimary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimary" ):
                return visitor.visitPrimary(self)
            else:
                return visitor.visitChildren(self)




    def primary(self):

        localctx = Java20Parser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 398, self.RULE_primary)
        try:
            self.state = 2099
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,227,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2097
                self.primaryNoNewArray()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2098
                self.arrayCreationExpression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryNoNewArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(Java20Parser.LiteralContext,0)


        def pNNA(self):
            return self.getTypedRuleContext(Java20Parser.PNNAContext,0)


        def classLiteral(self):
            return self.getTypedRuleContext(Java20Parser.ClassLiteralContext,0)


        def THIS(self):
            return self.getToken(Java20Parser.THIS, 0)

        def typeName(self):
            return self.getTypedRuleContext(Java20Parser.TypeNameContext,0)


        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(Java20Parser.DOT)
            else:
                return self.getToken(Java20Parser.DOT, i)

        def LPAREN(self):
            return self.getToken(Java20Parser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(Java20Parser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(Java20Parser.RPAREN, 0)

        def unqualifiedClassInstanceCreationExpression(self):
            return self.getTypedRuleContext(Java20Parser.UnqualifiedClassInstanceCreationExpressionContext,0)


        def expressionName(self):
            return self.getTypedRuleContext(Java20Parser.ExpressionNameContext,0)


        def arrayCreationExpression(self):
            return self.getTypedRuleContext(Java20Parser.ArrayCreationExpressionContext,0)


        def identifier(self):
            return self.getTypedRuleContext(Java20Parser.IdentifierContext,0)


        def SUPER(self):
            return self.getToken(Java20Parser.SUPER, 0)

        def LBRACK(self):
            return self.getToken(Java20Parser.LBRACK, 0)

        def RBRACK(self):
            return self.getToken(Java20Parser.RBRACK, 0)

        def arrayCreationExpressionWithInitializer(self):
            return self.getTypedRuleContext(Java20Parser.ArrayCreationExpressionWithInitializerContext,0)


        def methodName(self):
            return self.getTypedRuleContext(Java20Parser.MethodNameContext,0)


        def argumentList(self):
            return self.getTypedRuleContext(Java20Parser.ArgumentListContext,0)


        def typeArguments(self):
            return self.getTypedRuleContext(Java20Parser.TypeArgumentsContext,0)


        def COLONCOLON(self):
            return self.getToken(Java20Parser.COLONCOLON, 0)

        def referenceType(self):
            return self.getTypedRuleContext(Java20Parser.ReferenceTypeContext,0)


        def classType(self):
            return self.getTypedRuleContext(Java20Parser.ClassTypeContext,0)


        def NEW(self):
            return self.getToken(Java20Parser.NEW, 0)

        def arrayType(self):
            return self.getTypedRuleContext(Java20Parser.ArrayTypeContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_primaryNoNewArray

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimaryNoNewArray" ):
                listener.enterPrimaryNoNewArray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimaryNoNewArray" ):
                listener.exitPrimaryNoNewArray(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimaryNoNewArray" ):
                return visitor.visitPrimaryNoNewArray(self)
            else:
                return visitor.visitChildren(self)




    def primaryNoNewArray(self):

        localctx = Java20Parser.PrimaryNoNewArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 400, self.RULE_primaryNoNewArray)
        self._la = 0 # Token type
        try:
            self.state = 2318
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,271,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2101
                self.literal()
                self.state = 2103
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,228,self._ctx)
                if la_ == 1:
                    self.state = 2102
                    self.pNNA()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2105
                self.classLiteral()
                self.state = 2107
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,229,self._ctx)
                if la_ == 1:
                    self.state = 2106
                    self.pNNA()


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2109
                self.match(Java20Parser.THIS)
                self.state = 2111
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,230,self._ctx)
                if la_ == 1:
                    self.state = 2110
                    self.pNNA()


                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 2113
                self.typeName()
                self.state = 2114
                self.match(Java20Parser.DOT)
                self.state = 2115
                self.match(Java20Parser.THIS)
                self.state = 2117
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,231,self._ctx)
                if la_ == 1:
                    self.state = 2116
                    self.pNNA()


                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 2119
                self.match(Java20Parser.LPAREN)
                self.state = 2120
                self.expression()
                self.state = 2121
                self.match(Java20Parser.RPAREN)
                self.state = 2123
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,232,self._ctx)
                if la_ == 1:
                    self.state = 2122
                    self.pNNA()


                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 2125
                self.unqualifiedClassInstanceCreationExpression()
                self.state = 2127
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,233,self._ctx)
                if la_ == 1:
                    self.state = 2126
                    self.pNNA()


                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 2129
                self.expressionName()
                self.state = 2130
                self.match(Java20Parser.DOT)
                self.state = 2131
                self.unqualifiedClassInstanceCreationExpression()
                self.state = 2133
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,234,self._ctx)
                if la_ == 1:
                    self.state = 2132
                    self.pNNA()


                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 2135
                self.arrayCreationExpression()
                self.state = 2136
                self.match(Java20Parser.DOT)
                self.state = 2137
                self.unqualifiedClassInstanceCreationExpression()
                self.state = 2139
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,235,self._ctx)
                if la_ == 1:
                    self.state = 2138
                    self.pNNA()


                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 2141
                self.arrayCreationExpression()
                self.state = 2142
                self.match(Java20Parser.DOT)
                self.state = 2143
                self.identifier()
                self.state = 2145
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,236,self._ctx)
                if la_ == 1:
                    self.state = 2144
                    self.pNNA()


                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 2147
                self.match(Java20Parser.SUPER)
                self.state = 2148
                self.match(Java20Parser.DOT)
                self.state = 2149
                self.identifier()
                self.state = 2151
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,237,self._ctx)
                if la_ == 1:
                    self.state = 2150
                    self.pNNA()


                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 2153
                self.typeName()
                self.state = 2154
                self.match(Java20Parser.DOT)
                self.state = 2155
                self.match(Java20Parser.SUPER)
                self.state = 2156
                self.match(Java20Parser.DOT)
                self.state = 2157
                self.identifier()
                self.state = 2159
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,238,self._ctx)
                if la_ == 1:
                    self.state = 2158
                    self.pNNA()


                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 2161
                self.expressionName()
                self.state = 2162
                self.match(Java20Parser.LBRACK)
                self.state = 2163
                self.expression()
                self.state = 2164
                self.match(Java20Parser.RBRACK)
                self.state = 2166
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,239,self._ctx)
                if la_ == 1:
                    self.state = 2165
                    self.pNNA()


                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 2168
                self.arrayCreationExpressionWithInitializer()
                self.state = 2169
                self.match(Java20Parser.LBRACK)
                self.state = 2170
                self.expression()
                self.state = 2171
                self.match(Java20Parser.RBRACK)
                self.state = 2173
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,240,self._ctx)
                if la_ == 1:
                    self.state = 2172
                    self.pNNA()


                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 2175
                self.methodName()
                self.state = 2176
                self.match(Java20Parser.LPAREN)
                self.state = 2178
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java20Parser.EXPORTS) | (1 << Java20Parser.MODULE) | (1 << Java20Parser.NONSEALED) | (1 << Java20Parser.OPEN) | (1 << Java20Parser.OPENS) | (1 << Java20Parser.PERMITS) | (1 << Java20Parser.PROVIDES) | (1 << Java20Parser.RECORD) | (1 << Java20Parser.REQUIRES) | (1 << Java20Parser.SEALED) | (1 << Java20Parser.TO) | (1 << Java20Parser.TRANSITIVE) | (1 << Java20Parser.USES) | (1 << Java20Parser.VAR) | (1 << Java20Parser.WITH) | (1 << Java20Parser.YIELD) | (1 << Java20Parser.BOOLEAN) | (1 << Java20Parser.BYTE) | (1 << Java20Parser.CHAR) | (1 << Java20Parser.DOUBLE) | (1 << Java20Parser.FLOAT) | (1 << Java20Parser.INT) | (1 << Java20Parser.LONG) | (1 << Java20Parser.NEW) | (1 << Java20Parser.SHORT) | (1 << Java20Parser.SUPER) | (1 << Java20Parser.SWITCH) | (1 << Java20Parser.THIS))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (Java20Parser.VOID - 65)) | (1 << (Java20Parser.IntegerLiteral - 65)) | (1 << (Java20Parser.FloatingPointLiteral - 65)) | (1 << (Java20Parser.BooleanLiteral - 65)) | (1 << (Java20Parser.CharacterLiteral - 65)) | (1 << (Java20Parser.StringLiteral - 65)) | (1 << (Java20Parser.TextBlock - 65)) | (1 << (Java20Parser.NullLiteral - 65)) | (1 << (Java20Parser.LPAREN - 65)) | (1 << (Java20Parser.AT - 65)) | (1 << (Java20Parser.BANG - 65)) | (1 << (Java20Parser.TILDE - 65)) | (1 << (Java20Parser.INC - 65)) | (1 << (Java20Parser.DEC - 65)) | (1 << (Java20Parser.ADD - 65)) | (1 << (Java20Parser.SUB - 65)) | (1 << (Java20Parser.Identifier - 65)))) != 0):
                    self.state = 2177
                    self.argumentList()


                self.state = 2180
                self.match(Java20Parser.RPAREN)
                self.state = 2182
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,242,self._ctx)
                if la_ == 1:
                    self.state = 2181
                    self.pNNA()


                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 2184
                self.typeName()
                self.state = 2185
                self.match(Java20Parser.DOT)
                self.state = 2187
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Java20Parser.LT:
                    self.state = 2186
                    self.typeArguments()


                self.state = 2189
                self.identifier()
                self.state = 2190
                self.match(Java20Parser.LPAREN)
                self.state = 2192
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java20Parser.EXPORTS) | (1 << Java20Parser.MODULE) | (1 << Java20Parser.NONSEALED) | (1 << Java20Parser.OPEN) | (1 << Java20Parser.OPENS) | (1 << Java20Parser.PERMITS) | (1 << Java20Parser.PROVIDES) | (1 << Java20Parser.RECORD) | (1 << Java20Parser.REQUIRES) | (1 << Java20Parser.SEALED) | (1 << Java20Parser.TO) | (1 << Java20Parser.TRANSITIVE) | (1 << Java20Parser.USES) | (1 << Java20Parser.VAR) | (1 << Java20Parser.WITH) | (1 << Java20Parser.YIELD) | (1 << Java20Parser.BOOLEAN) | (1 << Java20Parser.BYTE) | (1 << Java20Parser.CHAR) | (1 << Java20Parser.DOUBLE) | (1 << Java20Parser.FLOAT) | (1 << Java20Parser.INT) | (1 << Java20Parser.LONG) | (1 << Java20Parser.NEW) | (1 << Java20Parser.SHORT) | (1 << Java20Parser.SUPER) | (1 << Java20Parser.SWITCH) | (1 << Java20Parser.THIS))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (Java20Parser.VOID - 65)) | (1 << (Java20Parser.IntegerLiteral - 65)) | (1 << (Java20Parser.FloatingPointLiteral - 65)) | (1 << (Java20Parser.BooleanLiteral - 65)) | (1 << (Java20Parser.CharacterLiteral - 65)) | (1 << (Java20Parser.StringLiteral - 65)) | (1 << (Java20Parser.TextBlock - 65)) | (1 << (Java20Parser.NullLiteral - 65)) | (1 << (Java20Parser.LPAREN - 65)) | (1 << (Java20Parser.AT - 65)) | (1 << (Java20Parser.BANG - 65)) | (1 << (Java20Parser.TILDE - 65)) | (1 << (Java20Parser.INC - 65)) | (1 << (Java20Parser.DEC - 65)) | (1 << (Java20Parser.ADD - 65)) | (1 << (Java20Parser.SUB - 65)) | (1 << (Java20Parser.Identifier - 65)))) != 0):
                    self.state = 2191
                    self.argumentList()


                self.state = 2194
                self.match(Java20Parser.RPAREN)
                self.state = 2196
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,245,self._ctx)
                if la_ == 1:
                    self.state = 2195
                    self.pNNA()


                pass

            elif la_ == 16:
                self.enterOuterAlt(localctx, 16)
                self.state = 2198
                self.expressionName()
                self.state = 2199
                self.match(Java20Parser.DOT)
                self.state = 2201
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Java20Parser.LT:
                    self.state = 2200
                    self.typeArguments()


                self.state = 2203
                self.identifier()
                self.state = 2204
                self.match(Java20Parser.LPAREN)
                self.state = 2206
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java20Parser.EXPORTS) | (1 << Java20Parser.MODULE) | (1 << Java20Parser.NONSEALED) | (1 << Java20Parser.OPEN) | (1 << Java20Parser.OPENS) | (1 << Java20Parser.PERMITS) | (1 << Java20Parser.PROVIDES) | (1 << Java20Parser.RECORD) | (1 << Java20Parser.REQUIRES) | (1 << Java20Parser.SEALED) | (1 << Java20Parser.TO) | (1 << Java20Parser.TRANSITIVE) | (1 << Java20Parser.USES) | (1 << Java20Parser.VAR) | (1 << Java20Parser.WITH) | (1 << Java20Parser.YIELD) | (1 << Java20Parser.BOOLEAN) | (1 << Java20Parser.BYTE) | (1 << Java20Parser.CHAR) | (1 << Java20Parser.DOUBLE) | (1 << Java20Parser.FLOAT) | (1 << Java20Parser.INT) | (1 << Java20Parser.LONG) | (1 << Java20Parser.NEW) | (1 << Java20Parser.SHORT) | (1 << Java20Parser.SUPER) | (1 << Java20Parser.SWITCH) | (1 << Java20Parser.THIS))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (Java20Parser.VOID - 65)) | (1 << (Java20Parser.IntegerLiteral - 65)) | (1 << (Java20Parser.FloatingPointLiteral - 65)) | (1 << (Java20Parser.BooleanLiteral - 65)) | (1 << (Java20Parser.CharacterLiteral - 65)) | (1 << (Java20Parser.StringLiteral - 65)) | (1 << (Java20Parser.TextBlock - 65)) | (1 << (Java20Parser.NullLiteral - 65)) | (1 << (Java20Parser.LPAREN - 65)) | (1 << (Java20Parser.AT - 65)) | (1 << (Java20Parser.BANG - 65)) | (1 << (Java20Parser.TILDE - 65)) | (1 << (Java20Parser.INC - 65)) | (1 << (Java20Parser.DEC - 65)) | (1 << (Java20Parser.ADD - 65)) | (1 << (Java20Parser.SUB - 65)) | (1 << (Java20Parser.Identifier - 65)))) != 0):
                    self.state = 2205
                    self.argumentList()


                self.state = 2208
                self.match(Java20Parser.RPAREN)
                self.state = 2210
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,248,self._ctx)
                if la_ == 1:
                    self.state = 2209
                    self.pNNA()


                pass

            elif la_ == 17:
                self.enterOuterAlt(localctx, 17)
                self.state = 2212
                self.arrayCreationExpression()
                self.state = 2213
                self.match(Java20Parser.DOT)
                self.state = 2215
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Java20Parser.LT:
                    self.state = 2214
                    self.typeArguments()


                self.state = 2217
                self.identifier()
                self.state = 2218
                self.match(Java20Parser.LPAREN)
                self.state = 2220
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java20Parser.EXPORTS) | (1 << Java20Parser.MODULE) | (1 << Java20Parser.NONSEALED) | (1 << Java20Parser.OPEN) | (1 << Java20Parser.OPENS) | (1 << Java20Parser.PERMITS) | (1 << Java20Parser.PROVIDES) | (1 << Java20Parser.RECORD) | (1 << Java20Parser.REQUIRES) | (1 << Java20Parser.SEALED) | (1 << Java20Parser.TO) | (1 << Java20Parser.TRANSITIVE) | (1 << Java20Parser.USES) | (1 << Java20Parser.VAR) | (1 << Java20Parser.WITH) | (1 << Java20Parser.YIELD) | (1 << Java20Parser.BOOLEAN) | (1 << Java20Parser.BYTE) | (1 << Java20Parser.CHAR) | (1 << Java20Parser.DOUBLE) | (1 << Java20Parser.FLOAT) | (1 << Java20Parser.INT) | (1 << Java20Parser.LONG) | (1 << Java20Parser.NEW) | (1 << Java20Parser.SHORT) | (1 << Java20Parser.SUPER) | (1 << Java20Parser.SWITCH) | (1 << Java20Parser.THIS))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (Java20Parser.VOID - 65)) | (1 << (Java20Parser.IntegerLiteral - 65)) | (1 << (Java20Parser.FloatingPointLiteral - 65)) | (1 << (Java20Parser.BooleanLiteral - 65)) | (1 << (Java20Parser.CharacterLiteral - 65)) | (1 << (Java20Parser.StringLiteral - 65)) | (1 << (Java20Parser.TextBlock - 65)) | (1 << (Java20Parser.NullLiteral - 65)) | (1 << (Java20Parser.LPAREN - 65)) | (1 << (Java20Parser.AT - 65)) | (1 << (Java20Parser.BANG - 65)) | (1 << (Java20Parser.TILDE - 65)) | (1 << (Java20Parser.INC - 65)) | (1 << (Java20Parser.DEC - 65)) | (1 << (Java20Parser.ADD - 65)) | (1 << (Java20Parser.SUB - 65)) | (1 << (Java20Parser.Identifier - 65)))) != 0):
                    self.state = 2219
                    self.argumentList()


                self.state = 2222
                self.match(Java20Parser.RPAREN)
                self.state = 2224
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,251,self._ctx)
                if la_ == 1:
                    self.state = 2223
                    self.pNNA()


                pass

            elif la_ == 18:
                self.enterOuterAlt(localctx, 18)
                self.state = 2226
                self.match(Java20Parser.SUPER)
                self.state = 2227
                self.match(Java20Parser.DOT)
                self.state = 2229
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Java20Parser.LT:
                    self.state = 2228
                    self.typeArguments()


                self.state = 2231
                self.identifier()
                self.state = 2232
                self.match(Java20Parser.LPAREN)
                self.state = 2234
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java20Parser.EXPORTS) | (1 << Java20Parser.MODULE) | (1 << Java20Parser.NONSEALED) | (1 << Java20Parser.OPEN) | (1 << Java20Parser.OPENS) | (1 << Java20Parser.PERMITS) | (1 << Java20Parser.PROVIDES) | (1 << Java20Parser.RECORD) | (1 << Java20Parser.REQUIRES) | (1 << Java20Parser.SEALED) | (1 << Java20Parser.TO) | (1 << Java20Parser.TRANSITIVE) | (1 << Java20Parser.USES) | (1 << Java20Parser.VAR) | (1 << Java20Parser.WITH) | (1 << Java20Parser.YIELD) | (1 << Java20Parser.BOOLEAN) | (1 << Java20Parser.BYTE) | (1 << Java20Parser.CHAR) | (1 << Java20Parser.DOUBLE) | (1 << Java20Parser.FLOAT) | (1 << Java20Parser.INT) | (1 << Java20Parser.LONG) | (1 << Java20Parser.NEW) | (1 << Java20Parser.SHORT) | (1 << Java20Parser.SUPER) | (1 << Java20Parser.SWITCH) | (1 << Java20Parser.THIS))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (Java20Parser.VOID - 65)) | (1 << (Java20Parser.IntegerLiteral - 65)) | (1 << (Java20Parser.FloatingPointLiteral - 65)) | (1 << (Java20Parser.BooleanLiteral - 65)) | (1 << (Java20Parser.CharacterLiteral - 65)) | (1 << (Java20Parser.StringLiteral - 65)) | (1 << (Java20Parser.TextBlock - 65)) | (1 << (Java20Parser.NullLiteral - 65)) | (1 << (Java20Parser.LPAREN - 65)) | (1 << (Java20Parser.AT - 65)) | (1 << (Java20Parser.BANG - 65)) | (1 << (Java20Parser.TILDE - 65)) | (1 << (Java20Parser.INC - 65)) | (1 << (Java20Parser.DEC - 65)) | (1 << (Java20Parser.ADD - 65)) | (1 << (Java20Parser.SUB - 65)) | (1 << (Java20Parser.Identifier - 65)))) != 0):
                    self.state = 2233
                    self.argumentList()


                self.state = 2236
                self.match(Java20Parser.RPAREN)
                self.state = 2238
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,254,self._ctx)
                if la_ == 1:
                    self.state = 2237
                    self.pNNA()


                pass

            elif la_ == 19:
                self.enterOuterAlt(localctx, 19)
                self.state = 2240
                self.typeName()
                self.state = 2241
                self.match(Java20Parser.DOT)
                self.state = 2242
                self.match(Java20Parser.SUPER)
                self.state = 2243
                self.match(Java20Parser.DOT)
                self.state = 2245
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Java20Parser.LT:
                    self.state = 2244
                    self.typeArguments()


                self.state = 2247
                self.identifier()
                self.state = 2248
                self.match(Java20Parser.LPAREN)
                self.state = 2250
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java20Parser.EXPORTS) | (1 << Java20Parser.MODULE) | (1 << Java20Parser.NONSEALED) | (1 << Java20Parser.OPEN) | (1 << Java20Parser.OPENS) | (1 << Java20Parser.PERMITS) | (1 << Java20Parser.PROVIDES) | (1 << Java20Parser.RECORD) | (1 << Java20Parser.REQUIRES) | (1 << Java20Parser.SEALED) | (1 << Java20Parser.TO) | (1 << Java20Parser.TRANSITIVE) | (1 << Java20Parser.USES) | (1 << Java20Parser.VAR) | (1 << Java20Parser.WITH) | (1 << Java20Parser.YIELD) | (1 << Java20Parser.BOOLEAN) | (1 << Java20Parser.BYTE) | (1 << Java20Parser.CHAR) | (1 << Java20Parser.DOUBLE) | (1 << Java20Parser.FLOAT) | (1 << Java20Parser.INT) | (1 << Java20Parser.LONG) | (1 << Java20Parser.NEW) | (1 << Java20Parser.SHORT) | (1 << Java20Parser.SUPER) | (1 << Java20Parser.SWITCH) | (1 << Java20Parser.THIS))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (Java20Parser.VOID - 65)) | (1 << (Java20Parser.IntegerLiteral - 65)) | (1 << (Java20Parser.FloatingPointLiteral - 65)) | (1 << (Java20Parser.BooleanLiteral - 65)) | (1 << (Java20Parser.CharacterLiteral - 65)) | (1 << (Java20Parser.StringLiteral - 65)) | (1 << (Java20Parser.TextBlock - 65)) | (1 << (Java20Parser.NullLiteral - 65)) | (1 << (Java20Parser.LPAREN - 65)) | (1 << (Java20Parser.AT - 65)) | (1 << (Java20Parser.BANG - 65)) | (1 << (Java20Parser.TILDE - 65)) | (1 << (Java20Parser.INC - 65)) | (1 << (Java20Parser.DEC - 65)) | (1 << (Java20Parser.ADD - 65)) | (1 << (Java20Parser.SUB - 65)) | (1 << (Java20Parser.Identifier - 65)))) != 0):
                    self.state = 2249
                    self.argumentList()


                self.state = 2252
                self.match(Java20Parser.RPAREN)
                self.state = 2254
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,257,self._ctx)
                if la_ == 1:
                    self.state = 2253
                    self.pNNA()


                pass

            elif la_ == 20:
                self.enterOuterAlt(localctx, 20)
                self.state = 2256
                self.expressionName()
                self.state = 2257
                self.match(Java20Parser.COLONCOLON)
                self.state = 2259
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Java20Parser.LT:
                    self.state = 2258
                    self.typeArguments()


                self.state = 2261
                self.identifier()
                self.state = 2263
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,259,self._ctx)
                if la_ == 1:
                    self.state = 2262
                    self.pNNA()


                pass

            elif la_ == 21:
                self.enterOuterAlt(localctx, 21)
                self.state = 2265
                self.arrayCreationExpression()
                self.state = 2266
                self.match(Java20Parser.COLONCOLON)
                self.state = 2268
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Java20Parser.LT:
                    self.state = 2267
                    self.typeArguments()


                self.state = 2270
                self.identifier()
                self.state = 2272
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,261,self._ctx)
                if la_ == 1:
                    self.state = 2271
                    self.pNNA()


                pass

            elif la_ == 22:
                self.enterOuterAlt(localctx, 22)
                self.state = 2274
                self.referenceType()
                self.state = 2275
                self.match(Java20Parser.COLONCOLON)
                self.state = 2277
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Java20Parser.LT:
                    self.state = 2276
                    self.typeArguments()


                self.state = 2279
                self.identifier()
                self.state = 2281
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,263,self._ctx)
                if la_ == 1:
                    self.state = 2280
                    self.pNNA()


                pass

            elif la_ == 23:
                self.enterOuterAlt(localctx, 23)
                self.state = 2283
                self.match(Java20Parser.SUPER)
                self.state = 2284
                self.match(Java20Parser.COLONCOLON)
                self.state = 2286
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Java20Parser.LT:
                    self.state = 2285
                    self.typeArguments()


                self.state = 2288
                self.identifier()
                self.state = 2290
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,265,self._ctx)
                if la_ == 1:
                    self.state = 2289
                    self.pNNA()


                pass

            elif la_ == 24:
                self.enterOuterAlt(localctx, 24)
                self.state = 2292
                self.typeName()
                self.state = 2293
                self.match(Java20Parser.DOT)
                self.state = 2294
                self.match(Java20Parser.SUPER)
                self.state = 2295
                self.match(Java20Parser.COLONCOLON)
                self.state = 2297
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Java20Parser.LT:
                    self.state = 2296
                    self.typeArguments()


                self.state = 2299
                self.identifier()
                self.state = 2301
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,267,self._ctx)
                if la_ == 1:
                    self.state = 2300
                    self.pNNA()


                pass

            elif la_ == 25:
                self.enterOuterAlt(localctx, 25)
                self.state = 2303
                self.classType()
                self.state = 2304
                self.match(Java20Parser.COLONCOLON)
                self.state = 2306
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Java20Parser.LT:
                    self.state = 2305
                    self.typeArguments()


                self.state = 2308
                self.match(Java20Parser.NEW)
                self.state = 2310
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,269,self._ctx)
                if la_ == 1:
                    self.state = 2309
                    self.pNNA()


                pass

            elif la_ == 26:
                self.enterOuterAlt(localctx, 26)
                self.state = 2312
                self.arrayType()
                self.state = 2313
                self.match(Java20Parser.COLONCOLON)
                self.state = 2314
                self.match(Java20Parser.NEW)
                self.state = 2316
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,270,self._ctx)
                if la_ == 1:
                    self.state = 2315
                    self.pNNA()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PNNAContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self):
            return self.getToken(Java20Parser.DOT, 0)

        def unqualifiedClassInstanceCreationExpression(self):
            return self.getTypedRuleContext(Java20Parser.UnqualifiedClassInstanceCreationExpressionContext,0)


        def pNNA(self):
            return self.getTypedRuleContext(Java20Parser.PNNAContext,0)


        def identifier(self):
            return self.getTypedRuleContext(Java20Parser.IdentifierContext,0)


        def LBRACK(self):
            return self.getToken(Java20Parser.LBRACK, 0)

        def expression(self):
            return self.getTypedRuleContext(Java20Parser.ExpressionContext,0)


        def RBRACK(self):
            return self.getToken(Java20Parser.RBRACK, 0)

        def LPAREN(self):
            return self.getToken(Java20Parser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(Java20Parser.RPAREN, 0)

        def typeArguments(self):
            return self.getTypedRuleContext(Java20Parser.TypeArgumentsContext,0)


        def argumentList(self):
            return self.getTypedRuleContext(Java20Parser.ArgumentListContext,0)


        def COLONCOLON(self):
            return self.getToken(Java20Parser.COLONCOLON, 0)

        def getRuleIndex(self):
            return Java20Parser.RULE_pNNA

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPNNA" ):
                listener.enterPNNA(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPNNA" ):
                listener.exitPNNA(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPNNA" ):
                return visitor.visitPNNA(self)
            else:
                return visitor.visitChildren(self)




    def pNNA(self):

        localctx = Java20Parser.PNNAContext(self, self._ctx, self.state)
        self.enterRule(localctx, 402, self.RULE_pNNA)
        self._la = 0 # Token type
        try:
            self.state = 2357
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,280,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2320
                self.match(Java20Parser.DOT)
                self.state = 2321
                self.unqualifiedClassInstanceCreationExpression()
                self.state = 2323
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,272,self._ctx)
                if la_ == 1:
                    self.state = 2322
                    self.pNNA()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2325
                self.match(Java20Parser.DOT)
                self.state = 2326
                self.identifier()
                self.state = 2328
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,273,self._ctx)
                if la_ == 1:
                    self.state = 2327
                    self.pNNA()


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2330
                self.match(Java20Parser.LBRACK)
                self.state = 2331
                self.expression()
                self.state = 2332
                self.match(Java20Parser.RBRACK)
                self.state = 2334
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,274,self._ctx)
                if la_ == 1:
                    self.state = 2333
                    self.pNNA()


                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 2336
                self.match(Java20Parser.DOT)
                self.state = 2338
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Java20Parser.LT:
                    self.state = 2337
                    self.typeArguments()


                self.state = 2340
                self.identifier()
                self.state = 2341
                self.match(Java20Parser.LPAREN)
                self.state = 2343
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java20Parser.EXPORTS) | (1 << Java20Parser.MODULE) | (1 << Java20Parser.NONSEALED) | (1 << Java20Parser.OPEN) | (1 << Java20Parser.OPENS) | (1 << Java20Parser.PERMITS) | (1 << Java20Parser.PROVIDES) | (1 << Java20Parser.RECORD) | (1 << Java20Parser.REQUIRES) | (1 << Java20Parser.SEALED) | (1 << Java20Parser.TO) | (1 << Java20Parser.TRANSITIVE) | (1 << Java20Parser.USES) | (1 << Java20Parser.VAR) | (1 << Java20Parser.WITH) | (1 << Java20Parser.YIELD) | (1 << Java20Parser.BOOLEAN) | (1 << Java20Parser.BYTE) | (1 << Java20Parser.CHAR) | (1 << Java20Parser.DOUBLE) | (1 << Java20Parser.FLOAT) | (1 << Java20Parser.INT) | (1 << Java20Parser.LONG) | (1 << Java20Parser.NEW) | (1 << Java20Parser.SHORT) | (1 << Java20Parser.SUPER) | (1 << Java20Parser.SWITCH) | (1 << Java20Parser.THIS))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (Java20Parser.VOID - 65)) | (1 << (Java20Parser.IntegerLiteral - 65)) | (1 << (Java20Parser.FloatingPointLiteral - 65)) | (1 << (Java20Parser.BooleanLiteral - 65)) | (1 << (Java20Parser.CharacterLiteral - 65)) | (1 << (Java20Parser.StringLiteral - 65)) | (1 << (Java20Parser.TextBlock - 65)) | (1 << (Java20Parser.NullLiteral - 65)) | (1 << (Java20Parser.LPAREN - 65)) | (1 << (Java20Parser.AT - 65)) | (1 << (Java20Parser.BANG - 65)) | (1 << (Java20Parser.TILDE - 65)) | (1 << (Java20Parser.INC - 65)) | (1 << (Java20Parser.DEC - 65)) | (1 << (Java20Parser.ADD - 65)) | (1 << (Java20Parser.SUB - 65)) | (1 << (Java20Parser.Identifier - 65)))) != 0):
                    self.state = 2342
                    self.argumentList()


                self.state = 2345
                self.match(Java20Parser.RPAREN)
                self.state = 2347
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,277,self._ctx)
                if la_ == 1:
                    self.state = 2346
                    self.pNNA()


                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 2349
                self.match(Java20Parser.COLONCOLON)
                self.state = 2351
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Java20Parser.LT:
                    self.state = 2350
                    self.typeArguments()


                self.state = 2353
                self.identifier()
                self.state = 2355
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,279,self._ctx)
                if la_ == 1:
                    self.state = 2354
                    self.pNNA()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeName(self):
            return self.getTypedRuleContext(Java20Parser.TypeNameContext,0)


        def DOT(self):
            return self.getToken(Java20Parser.DOT, 0)

        def CLASS(self):
            return self.getToken(Java20Parser.CLASS, 0)

        def LBRACK(self, i:int=None):
            if i is None:
                return self.getTokens(Java20Parser.LBRACK)
            else:
                return self.getToken(Java20Parser.LBRACK, i)

        def RBRACK(self, i:int=None):
            if i is None:
                return self.getTokens(Java20Parser.RBRACK)
            else:
                return self.getToken(Java20Parser.RBRACK, i)

        def numericType(self):
            return self.getTypedRuleContext(Java20Parser.NumericTypeContext,0)


        def BOOLEAN(self):
            return self.getToken(Java20Parser.BOOLEAN, 0)

        def VOID(self):
            return self.getToken(Java20Parser.VOID, 0)

        def getRuleIndex(self):
            return Java20Parser.RULE_classLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassLiteral" ):
                listener.enterClassLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassLiteral" ):
                listener.exitClassLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassLiteral" ):
                return visitor.visitClassLiteral(self)
            else:
                return visitor.visitChildren(self)




    def classLiteral(self):

        localctx = Java20Parser.ClassLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 404, self.RULE_classLiteral)
        self._la = 0 # Token type
        try:
            self.state = 2394
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Java20Parser.EXPORTS, Java20Parser.MODULE, Java20Parser.NONSEALED, Java20Parser.OPEN, Java20Parser.OPENS, Java20Parser.PERMITS, Java20Parser.PROVIDES, Java20Parser.RECORD, Java20Parser.REQUIRES, Java20Parser.SEALED, Java20Parser.TO, Java20Parser.TRANSITIVE, Java20Parser.USES, Java20Parser.VAR, Java20Parser.WITH, Java20Parser.YIELD, Java20Parser.Identifier]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2359
                self.typeName()
                self.state = 2364
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==Java20Parser.LBRACK:
                    self.state = 2360
                    self.match(Java20Parser.LBRACK)
                    self.state = 2361
                    self.match(Java20Parser.RBRACK)
                    self.state = 2366
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 2367
                self.match(Java20Parser.DOT)
                self.state = 2368
                self.match(Java20Parser.CLASS)
                pass
            elif token in [Java20Parser.BYTE, Java20Parser.CHAR, Java20Parser.DOUBLE, Java20Parser.FLOAT, Java20Parser.INT, Java20Parser.LONG, Java20Parser.SHORT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2370
                self.numericType()
                self.state = 2375
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==Java20Parser.LBRACK:
                    self.state = 2371
                    self.match(Java20Parser.LBRACK)
                    self.state = 2372
                    self.match(Java20Parser.RBRACK)
                    self.state = 2377
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 2378
                self.match(Java20Parser.DOT)
                self.state = 2379
                self.match(Java20Parser.CLASS)
                pass
            elif token in [Java20Parser.BOOLEAN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 2381
                self.match(Java20Parser.BOOLEAN)
                self.state = 2386
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==Java20Parser.LBRACK:
                    self.state = 2382
                    self.match(Java20Parser.LBRACK)
                    self.state = 2383
                    self.match(Java20Parser.RBRACK)
                    self.state = 2388
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 2389
                self.match(Java20Parser.DOT)
                self.state = 2390
                self.match(Java20Parser.CLASS)
                pass
            elif token in [Java20Parser.VOID]:
                self.enterOuterAlt(localctx, 4)
                self.state = 2391
                self.match(Java20Parser.VOID)
                self.state = 2392
                self.match(Java20Parser.DOT)
                self.state = 2393
                self.match(Java20Parser.CLASS)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassInstanceCreationExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unqualifiedClassInstanceCreationExpression(self):
            return self.getTypedRuleContext(Java20Parser.UnqualifiedClassInstanceCreationExpressionContext,0)


        def expressionName(self):
            return self.getTypedRuleContext(Java20Parser.ExpressionNameContext,0)


        def DOT(self):
            return self.getToken(Java20Parser.DOT, 0)

        def primary(self):
            return self.getTypedRuleContext(Java20Parser.PrimaryContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_classInstanceCreationExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassInstanceCreationExpression" ):
                listener.enterClassInstanceCreationExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassInstanceCreationExpression" ):
                listener.exitClassInstanceCreationExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassInstanceCreationExpression" ):
                return visitor.visitClassInstanceCreationExpression(self)
            else:
                return visitor.visitChildren(self)




    def classInstanceCreationExpression(self):

        localctx = Java20Parser.ClassInstanceCreationExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 406, self.RULE_classInstanceCreationExpression)
        try:
            self.state = 2405
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,285,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2396
                self.unqualifiedClassInstanceCreationExpression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2397
                self.expressionName()
                self.state = 2398
                self.match(Java20Parser.DOT)
                self.state = 2399
                self.unqualifiedClassInstanceCreationExpression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2401
                self.primary()
                self.state = 2402
                self.match(Java20Parser.DOT)
                self.state = 2403
                self.unqualifiedClassInstanceCreationExpression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnqualifiedClassInstanceCreationExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(Java20Parser.NEW, 0)

        def classOrInterfaceTypeToInstantiate(self):
            return self.getTypedRuleContext(Java20Parser.ClassOrInterfaceTypeToInstantiateContext,0)


        def LPAREN(self):
            return self.getToken(Java20Parser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(Java20Parser.RPAREN, 0)

        def typeArguments(self):
            return self.getTypedRuleContext(Java20Parser.TypeArgumentsContext,0)


        def argumentList(self):
            return self.getTypedRuleContext(Java20Parser.ArgumentListContext,0)


        def classBody(self):
            return self.getTypedRuleContext(Java20Parser.ClassBodyContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_unqualifiedClassInstanceCreationExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnqualifiedClassInstanceCreationExpression" ):
                listener.enterUnqualifiedClassInstanceCreationExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnqualifiedClassInstanceCreationExpression" ):
                listener.exitUnqualifiedClassInstanceCreationExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnqualifiedClassInstanceCreationExpression" ):
                return visitor.visitUnqualifiedClassInstanceCreationExpression(self)
            else:
                return visitor.visitChildren(self)




    def unqualifiedClassInstanceCreationExpression(self):

        localctx = Java20Parser.UnqualifiedClassInstanceCreationExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 408, self.RULE_unqualifiedClassInstanceCreationExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2407
            self.match(Java20Parser.NEW)
            self.state = 2409
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Java20Parser.LT:
                self.state = 2408
                self.typeArguments()


            self.state = 2411
            self.classOrInterfaceTypeToInstantiate()
            self.state = 2412
            self.match(Java20Parser.LPAREN)
            self.state = 2414
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java20Parser.EXPORTS) | (1 << Java20Parser.MODULE) | (1 << Java20Parser.NONSEALED) | (1 << Java20Parser.OPEN) | (1 << Java20Parser.OPENS) | (1 << Java20Parser.PERMITS) | (1 << Java20Parser.PROVIDES) | (1 << Java20Parser.RECORD) | (1 << Java20Parser.REQUIRES) | (1 << Java20Parser.SEALED) | (1 << Java20Parser.TO) | (1 << Java20Parser.TRANSITIVE) | (1 << Java20Parser.USES) | (1 << Java20Parser.VAR) | (1 << Java20Parser.WITH) | (1 << Java20Parser.YIELD) | (1 << Java20Parser.BOOLEAN) | (1 << Java20Parser.BYTE) | (1 << Java20Parser.CHAR) | (1 << Java20Parser.DOUBLE) | (1 << Java20Parser.FLOAT) | (1 << Java20Parser.INT) | (1 << Java20Parser.LONG) | (1 << Java20Parser.NEW) | (1 << Java20Parser.SHORT) | (1 << Java20Parser.SUPER) | (1 << Java20Parser.SWITCH) | (1 << Java20Parser.THIS))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (Java20Parser.VOID - 65)) | (1 << (Java20Parser.IntegerLiteral - 65)) | (1 << (Java20Parser.FloatingPointLiteral - 65)) | (1 << (Java20Parser.BooleanLiteral - 65)) | (1 << (Java20Parser.CharacterLiteral - 65)) | (1 << (Java20Parser.StringLiteral - 65)) | (1 << (Java20Parser.TextBlock - 65)) | (1 << (Java20Parser.NullLiteral - 65)) | (1 << (Java20Parser.LPAREN - 65)) | (1 << (Java20Parser.AT - 65)) | (1 << (Java20Parser.BANG - 65)) | (1 << (Java20Parser.TILDE - 65)) | (1 << (Java20Parser.INC - 65)) | (1 << (Java20Parser.DEC - 65)) | (1 << (Java20Parser.ADD - 65)) | (1 << (Java20Parser.SUB - 65)) | (1 << (Java20Parser.Identifier - 65)))) != 0):
                self.state = 2413
                self.argumentList()


            self.state = 2416
            self.match(Java20Parser.RPAREN)
            self.state = 2418
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,288,self._ctx)
            if la_ == 1:
                self.state = 2417
                self.classBody()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassOrInterfaceTypeToInstantiateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.IdentifierContext)
            else:
                return self.getTypedRuleContext(Java20Parser.IdentifierContext,i)


        def annotation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.AnnotationContext)
            else:
                return self.getTypedRuleContext(Java20Parser.AnnotationContext,i)


        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(Java20Parser.DOT)
            else:
                return self.getToken(Java20Parser.DOT, i)

        def typeArgumentsOrDiamond(self):
            return self.getTypedRuleContext(Java20Parser.TypeArgumentsOrDiamondContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_classOrInterfaceTypeToInstantiate

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassOrInterfaceTypeToInstantiate" ):
                listener.enterClassOrInterfaceTypeToInstantiate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassOrInterfaceTypeToInstantiate" ):
                listener.exitClassOrInterfaceTypeToInstantiate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassOrInterfaceTypeToInstantiate" ):
                return visitor.visitClassOrInterfaceTypeToInstantiate(self)
            else:
                return visitor.visitChildren(self)




    def classOrInterfaceTypeToInstantiate(self):

        localctx = Java20Parser.ClassOrInterfaceTypeToInstantiateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 410, self.RULE_classOrInterfaceTypeToInstantiate)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2423
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Java20Parser.AT:
                self.state = 2420
                self.annotation()
                self.state = 2425
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 2426
            self.identifier()
            self.state = 2437
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Java20Parser.DOT:
                self.state = 2427
                self.match(Java20Parser.DOT)
                self.state = 2431
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==Java20Parser.AT:
                    self.state = 2428
                    self.annotation()
                    self.state = 2433
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 2434
                self.identifier()
                self.state = 2439
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 2441
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Java20Parser.OACA or _la==Java20Parser.LT:
                self.state = 2440
                self.typeArgumentsOrDiamond()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeArgumentsOrDiamondContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeArguments(self):
            return self.getTypedRuleContext(Java20Parser.TypeArgumentsContext,0)


        def OACA(self):
            return self.getToken(Java20Parser.OACA, 0)

        def getRuleIndex(self):
            return Java20Parser.RULE_typeArgumentsOrDiamond

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeArgumentsOrDiamond" ):
                listener.enterTypeArgumentsOrDiamond(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeArgumentsOrDiamond" ):
                listener.exitTypeArgumentsOrDiamond(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeArgumentsOrDiamond" ):
                return visitor.visitTypeArgumentsOrDiamond(self)
            else:
                return visitor.visitChildren(self)




    def typeArgumentsOrDiamond(self):

        localctx = Java20Parser.TypeArgumentsOrDiamondContext(self, self._ctx, self.state)
        self.enterRule(localctx, 412, self.RULE_typeArgumentsOrDiamond)
        try:
            self.state = 2445
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Java20Parser.LT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2443
                self.typeArguments()
                pass
            elif token in [Java20Parser.OACA]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2444
                self.match(Java20Parser.OACA)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayCreationExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arrayCreationExpressionWithoutInitializer(self):
            return self.getTypedRuleContext(Java20Parser.ArrayCreationExpressionWithoutInitializerContext,0)


        def arrayCreationExpressionWithInitializer(self):
            return self.getTypedRuleContext(Java20Parser.ArrayCreationExpressionWithInitializerContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_arrayCreationExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayCreationExpression" ):
                listener.enterArrayCreationExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayCreationExpression" ):
                listener.exitArrayCreationExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayCreationExpression" ):
                return visitor.visitArrayCreationExpression(self)
            else:
                return visitor.visitChildren(self)




    def arrayCreationExpression(self):

        localctx = Java20Parser.ArrayCreationExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 414, self.RULE_arrayCreationExpression)
        try:
            self.state = 2449
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,294,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2447
                self.arrayCreationExpressionWithoutInitializer()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2448
                self.arrayCreationExpressionWithInitializer()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayCreationExpressionWithoutInitializerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(Java20Parser.NEW, 0)

        def primitiveType(self):
            return self.getTypedRuleContext(Java20Parser.PrimitiveTypeContext,0)


        def dimExprs(self):
            return self.getTypedRuleContext(Java20Parser.DimExprsContext,0)


        def dims(self):
            return self.getTypedRuleContext(Java20Parser.DimsContext,0)


        def classType(self):
            return self.getTypedRuleContext(Java20Parser.ClassTypeContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_arrayCreationExpressionWithoutInitializer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayCreationExpressionWithoutInitializer" ):
                listener.enterArrayCreationExpressionWithoutInitializer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayCreationExpressionWithoutInitializer" ):
                listener.exitArrayCreationExpressionWithoutInitializer(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayCreationExpressionWithoutInitializer" ):
                return visitor.visitArrayCreationExpressionWithoutInitializer(self)
            else:
                return visitor.visitChildren(self)




    def arrayCreationExpressionWithoutInitializer(self):

        localctx = Java20Parser.ArrayCreationExpressionWithoutInitializerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 416, self.RULE_arrayCreationExpressionWithoutInitializer)
        try:
            self.state = 2463
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,297,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2451
                self.match(Java20Parser.NEW)
                self.state = 2452
                self.primitiveType()
                self.state = 2453
                self.dimExprs()
                self.state = 2455
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,295,self._ctx)
                if la_ == 1:
                    self.state = 2454
                    self.dims()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2457
                self.match(Java20Parser.NEW)
                self.state = 2458
                self.classType()
                self.state = 2459
                self.dimExprs()
                self.state = 2461
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,296,self._ctx)
                if la_ == 1:
                    self.state = 2460
                    self.dims()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayCreationExpressionWithInitializerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(Java20Parser.NEW, 0)

        def primitiveType(self):
            return self.getTypedRuleContext(Java20Parser.PrimitiveTypeContext,0)


        def dims(self):
            return self.getTypedRuleContext(Java20Parser.DimsContext,0)


        def arrayInitializer(self):
            return self.getTypedRuleContext(Java20Parser.ArrayInitializerContext,0)


        def classOrInterfaceType(self):
            return self.getTypedRuleContext(Java20Parser.ClassOrInterfaceTypeContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_arrayCreationExpressionWithInitializer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayCreationExpressionWithInitializer" ):
                listener.enterArrayCreationExpressionWithInitializer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayCreationExpressionWithInitializer" ):
                listener.exitArrayCreationExpressionWithInitializer(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayCreationExpressionWithInitializer" ):
                return visitor.visitArrayCreationExpressionWithInitializer(self)
            else:
                return visitor.visitChildren(self)




    def arrayCreationExpressionWithInitializer(self):

        localctx = Java20Parser.ArrayCreationExpressionWithInitializerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 418, self.RULE_arrayCreationExpressionWithInitializer)
        try:
            self.state = 2475
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,298,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2465
                self.match(Java20Parser.NEW)
                self.state = 2466
                self.primitiveType()
                self.state = 2467
                self.dims()
                self.state = 2468
                self.arrayInitializer()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2470
                self.match(Java20Parser.NEW)
                self.state = 2471
                self.classOrInterfaceType()
                self.state = 2472
                self.dims()
                self.state = 2473
                self.arrayInitializer()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DimExprsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dimExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.DimExprContext)
            else:
                return self.getTypedRuleContext(Java20Parser.DimExprContext,i)


        def getRuleIndex(self):
            return Java20Parser.RULE_dimExprs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDimExprs" ):
                listener.enterDimExprs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDimExprs" ):
                listener.exitDimExprs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimExprs" ):
                return visitor.visitDimExprs(self)
            else:
                return visitor.visitChildren(self)




    def dimExprs(self):

        localctx = Java20Parser.DimExprsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 420, self.RULE_dimExprs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2477
            self.dimExpr()
            self.state = 2481
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,299,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 2478
                    self.dimExpr() 
                self.state = 2483
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,299,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DimExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACK(self):
            return self.getToken(Java20Parser.LBRACK, 0)

        def expression(self):
            return self.getTypedRuleContext(Java20Parser.ExpressionContext,0)


        def RBRACK(self):
            return self.getToken(Java20Parser.RBRACK, 0)

        def annotation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.AnnotationContext)
            else:
                return self.getTypedRuleContext(Java20Parser.AnnotationContext,i)


        def getRuleIndex(self):
            return Java20Parser.RULE_dimExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDimExpr" ):
                listener.enterDimExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDimExpr" ):
                listener.exitDimExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimExpr" ):
                return visitor.visitDimExpr(self)
            else:
                return visitor.visitChildren(self)




    def dimExpr(self):

        localctx = Java20Parser.DimExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 422, self.RULE_dimExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2487
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Java20Parser.AT:
                self.state = 2484
                self.annotation()
                self.state = 2489
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 2490
            self.match(Java20Parser.LBRACK)
            self.state = 2491
            self.expression()
            self.state = 2492
            self.match(Java20Parser.RBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayAccessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressionName(self):
            return self.getTypedRuleContext(Java20Parser.ExpressionNameContext,0)


        def LBRACK(self):
            return self.getToken(Java20Parser.LBRACK, 0)

        def expression(self):
            return self.getTypedRuleContext(Java20Parser.ExpressionContext,0)


        def RBRACK(self):
            return self.getToken(Java20Parser.RBRACK, 0)

        def primaryNoNewArray(self):
            return self.getTypedRuleContext(Java20Parser.PrimaryNoNewArrayContext,0)


        def arrayCreationExpressionWithInitializer(self):
            return self.getTypedRuleContext(Java20Parser.ArrayCreationExpressionWithInitializerContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_arrayAccess

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayAccess" ):
                listener.enterArrayAccess(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayAccess" ):
                listener.exitArrayAccess(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayAccess" ):
                return visitor.visitArrayAccess(self)
            else:
                return visitor.visitChildren(self)




    def arrayAccess(self):

        localctx = Java20Parser.ArrayAccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 424, self.RULE_arrayAccess)
        try:
            self.state = 2509
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,301,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2494
                self.expressionName()
                self.state = 2495
                self.match(Java20Parser.LBRACK)
                self.state = 2496
                self.expression()
                self.state = 2497
                self.match(Java20Parser.RBRACK)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2499
                self.primaryNoNewArray()
                self.state = 2500
                self.match(Java20Parser.LBRACK)
                self.state = 2501
                self.expression()
                self.state = 2502
                self.match(Java20Parser.RBRACK)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2504
                self.arrayCreationExpressionWithInitializer()
                self.state = 2505
                self.match(Java20Parser.LBRACK)
                self.state = 2506
                self.expression()
                self.state = 2507
                self.match(Java20Parser.RBRACK)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldAccessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primary(self):
            return self.getTypedRuleContext(Java20Parser.PrimaryContext,0)


        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(Java20Parser.DOT)
            else:
                return self.getToken(Java20Parser.DOT, i)

        def identifier(self):
            return self.getTypedRuleContext(Java20Parser.IdentifierContext,0)


        def SUPER(self):
            return self.getToken(Java20Parser.SUPER, 0)

        def typeName(self):
            return self.getTypedRuleContext(Java20Parser.TypeNameContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_fieldAccess

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFieldAccess" ):
                listener.enterFieldAccess(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFieldAccess" ):
                listener.exitFieldAccess(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFieldAccess" ):
                return visitor.visitFieldAccess(self)
            else:
                return visitor.visitChildren(self)




    def fieldAccess(self):

        localctx = Java20Parser.FieldAccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 426, self.RULE_fieldAccess)
        try:
            self.state = 2524
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,302,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2511
                self.primary()
                self.state = 2512
                self.match(Java20Parser.DOT)
                self.state = 2513
                self.identifier()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2515
                self.match(Java20Parser.SUPER)
                self.state = 2516
                self.match(Java20Parser.DOT)
                self.state = 2517
                self.identifier()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2518
                self.typeName()
                self.state = 2519
                self.match(Java20Parser.DOT)
                self.state = 2520
                self.match(Java20Parser.SUPER)
                self.state = 2521
                self.match(Java20Parser.DOT)
                self.state = 2522
                self.identifier()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodInvocationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def methodName(self):
            return self.getTypedRuleContext(Java20Parser.MethodNameContext,0)


        def LPAREN(self):
            return self.getToken(Java20Parser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(Java20Parser.RPAREN, 0)

        def argumentList(self):
            return self.getTypedRuleContext(Java20Parser.ArgumentListContext,0)


        def typeName(self):
            return self.getTypedRuleContext(Java20Parser.TypeNameContext,0)


        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(Java20Parser.DOT)
            else:
                return self.getToken(Java20Parser.DOT, i)

        def identifier(self):
            return self.getTypedRuleContext(Java20Parser.IdentifierContext,0)


        def typeArguments(self):
            return self.getTypedRuleContext(Java20Parser.TypeArgumentsContext,0)


        def expressionName(self):
            return self.getTypedRuleContext(Java20Parser.ExpressionNameContext,0)


        def primary(self):
            return self.getTypedRuleContext(Java20Parser.PrimaryContext,0)


        def SUPER(self):
            return self.getToken(Java20Parser.SUPER, 0)

        def getRuleIndex(self):
            return Java20Parser.RULE_methodInvocation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodInvocation" ):
                listener.enterMethodInvocation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodInvocation" ):
                listener.exitMethodInvocation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodInvocation" ):
                return visitor.visitMethodInvocation(self)
            else:
                return visitor.visitChildren(self)




    def methodInvocation(self):

        localctx = Java20Parser.MethodInvocationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 428, self.RULE_methodInvocation)
        self._la = 0 # Token type
        try:
            self.state = 2595
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,314,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2526
                self.methodName()
                self.state = 2527
                self.match(Java20Parser.LPAREN)
                self.state = 2529
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java20Parser.EXPORTS) | (1 << Java20Parser.MODULE) | (1 << Java20Parser.NONSEALED) | (1 << Java20Parser.OPEN) | (1 << Java20Parser.OPENS) | (1 << Java20Parser.PERMITS) | (1 << Java20Parser.PROVIDES) | (1 << Java20Parser.RECORD) | (1 << Java20Parser.REQUIRES) | (1 << Java20Parser.SEALED) | (1 << Java20Parser.TO) | (1 << Java20Parser.TRANSITIVE) | (1 << Java20Parser.USES) | (1 << Java20Parser.VAR) | (1 << Java20Parser.WITH) | (1 << Java20Parser.YIELD) | (1 << Java20Parser.BOOLEAN) | (1 << Java20Parser.BYTE) | (1 << Java20Parser.CHAR) | (1 << Java20Parser.DOUBLE) | (1 << Java20Parser.FLOAT) | (1 << Java20Parser.INT) | (1 << Java20Parser.LONG) | (1 << Java20Parser.NEW) | (1 << Java20Parser.SHORT) | (1 << Java20Parser.SUPER) | (1 << Java20Parser.SWITCH) | (1 << Java20Parser.THIS))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (Java20Parser.VOID - 65)) | (1 << (Java20Parser.IntegerLiteral - 65)) | (1 << (Java20Parser.FloatingPointLiteral - 65)) | (1 << (Java20Parser.BooleanLiteral - 65)) | (1 << (Java20Parser.CharacterLiteral - 65)) | (1 << (Java20Parser.StringLiteral - 65)) | (1 << (Java20Parser.TextBlock - 65)) | (1 << (Java20Parser.NullLiteral - 65)) | (1 << (Java20Parser.LPAREN - 65)) | (1 << (Java20Parser.AT - 65)) | (1 << (Java20Parser.BANG - 65)) | (1 << (Java20Parser.TILDE - 65)) | (1 << (Java20Parser.INC - 65)) | (1 << (Java20Parser.DEC - 65)) | (1 << (Java20Parser.ADD - 65)) | (1 << (Java20Parser.SUB - 65)) | (1 << (Java20Parser.Identifier - 65)))) != 0):
                    self.state = 2528
                    self.argumentList()


                self.state = 2531
                self.match(Java20Parser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2533
                self.typeName()
                self.state = 2534
                self.match(Java20Parser.DOT)
                self.state = 2536
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Java20Parser.LT:
                    self.state = 2535
                    self.typeArguments()


                self.state = 2538
                self.identifier()
                self.state = 2539
                self.match(Java20Parser.LPAREN)
                self.state = 2541
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java20Parser.EXPORTS) | (1 << Java20Parser.MODULE) | (1 << Java20Parser.NONSEALED) | (1 << Java20Parser.OPEN) | (1 << Java20Parser.OPENS) | (1 << Java20Parser.PERMITS) | (1 << Java20Parser.PROVIDES) | (1 << Java20Parser.RECORD) | (1 << Java20Parser.REQUIRES) | (1 << Java20Parser.SEALED) | (1 << Java20Parser.TO) | (1 << Java20Parser.TRANSITIVE) | (1 << Java20Parser.USES) | (1 << Java20Parser.VAR) | (1 << Java20Parser.WITH) | (1 << Java20Parser.YIELD) | (1 << Java20Parser.BOOLEAN) | (1 << Java20Parser.BYTE) | (1 << Java20Parser.CHAR) | (1 << Java20Parser.DOUBLE) | (1 << Java20Parser.FLOAT) | (1 << Java20Parser.INT) | (1 << Java20Parser.LONG) | (1 << Java20Parser.NEW) | (1 << Java20Parser.SHORT) | (1 << Java20Parser.SUPER) | (1 << Java20Parser.SWITCH) | (1 << Java20Parser.THIS))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (Java20Parser.VOID - 65)) | (1 << (Java20Parser.IntegerLiteral - 65)) | (1 << (Java20Parser.FloatingPointLiteral - 65)) | (1 << (Java20Parser.BooleanLiteral - 65)) | (1 << (Java20Parser.CharacterLiteral - 65)) | (1 << (Java20Parser.StringLiteral - 65)) | (1 << (Java20Parser.TextBlock - 65)) | (1 << (Java20Parser.NullLiteral - 65)) | (1 << (Java20Parser.LPAREN - 65)) | (1 << (Java20Parser.AT - 65)) | (1 << (Java20Parser.BANG - 65)) | (1 << (Java20Parser.TILDE - 65)) | (1 << (Java20Parser.INC - 65)) | (1 << (Java20Parser.DEC - 65)) | (1 << (Java20Parser.ADD - 65)) | (1 << (Java20Parser.SUB - 65)) | (1 << (Java20Parser.Identifier - 65)))) != 0):
                    self.state = 2540
                    self.argumentList()


                self.state = 2543
                self.match(Java20Parser.RPAREN)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2545
                self.expressionName()
                self.state = 2546
                self.match(Java20Parser.DOT)
                self.state = 2548
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Java20Parser.LT:
                    self.state = 2547
                    self.typeArguments()


                self.state = 2550
                self.identifier()
                self.state = 2551
                self.match(Java20Parser.LPAREN)
                self.state = 2553
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java20Parser.EXPORTS) | (1 << Java20Parser.MODULE) | (1 << Java20Parser.NONSEALED) | (1 << Java20Parser.OPEN) | (1 << Java20Parser.OPENS) | (1 << Java20Parser.PERMITS) | (1 << Java20Parser.PROVIDES) | (1 << Java20Parser.RECORD) | (1 << Java20Parser.REQUIRES) | (1 << Java20Parser.SEALED) | (1 << Java20Parser.TO) | (1 << Java20Parser.TRANSITIVE) | (1 << Java20Parser.USES) | (1 << Java20Parser.VAR) | (1 << Java20Parser.WITH) | (1 << Java20Parser.YIELD) | (1 << Java20Parser.BOOLEAN) | (1 << Java20Parser.BYTE) | (1 << Java20Parser.CHAR) | (1 << Java20Parser.DOUBLE) | (1 << Java20Parser.FLOAT) | (1 << Java20Parser.INT) | (1 << Java20Parser.LONG) | (1 << Java20Parser.NEW) | (1 << Java20Parser.SHORT) | (1 << Java20Parser.SUPER) | (1 << Java20Parser.SWITCH) | (1 << Java20Parser.THIS))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (Java20Parser.VOID - 65)) | (1 << (Java20Parser.IntegerLiteral - 65)) | (1 << (Java20Parser.FloatingPointLiteral - 65)) | (1 << (Java20Parser.BooleanLiteral - 65)) | (1 << (Java20Parser.CharacterLiteral - 65)) | (1 << (Java20Parser.StringLiteral - 65)) | (1 << (Java20Parser.TextBlock - 65)) | (1 << (Java20Parser.NullLiteral - 65)) | (1 << (Java20Parser.LPAREN - 65)) | (1 << (Java20Parser.AT - 65)) | (1 << (Java20Parser.BANG - 65)) | (1 << (Java20Parser.TILDE - 65)) | (1 << (Java20Parser.INC - 65)) | (1 << (Java20Parser.DEC - 65)) | (1 << (Java20Parser.ADD - 65)) | (1 << (Java20Parser.SUB - 65)) | (1 << (Java20Parser.Identifier - 65)))) != 0):
                    self.state = 2552
                    self.argumentList()


                self.state = 2555
                self.match(Java20Parser.RPAREN)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 2557
                self.primary()
                self.state = 2558
                self.match(Java20Parser.DOT)
                self.state = 2560
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Java20Parser.LT:
                    self.state = 2559
                    self.typeArguments()


                self.state = 2562
                self.identifier()
                self.state = 2563
                self.match(Java20Parser.LPAREN)
                self.state = 2565
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java20Parser.EXPORTS) | (1 << Java20Parser.MODULE) | (1 << Java20Parser.NONSEALED) | (1 << Java20Parser.OPEN) | (1 << Java20Parser.OPENS) | (1 << Java20Parser.PERMITS) | (1 << Java20Parser.PROVIDES) | (1 << Java20Parser.RECORD) | (1 << Java20Parser.REQUIRES) | (1 << Java20Parser.SEALED) | (1 << Java20Parser.TO) | (1 << Java20Parser.TRANSITIVE) | (1 << Java20Parser.USES) | (1 << Java20Parser.VAR) | (1 << Java20Parser.WITH) | (1 << Java20Parser.YIELD) | (1 << Java20Parser.BOOLEAN) | (1 << Java20Parser.BYTE) | (1 << Java20Parser.CHAR) | (1 << Java20Parser.DOUBLE) | (1 << Java20Parser.FLOAT) | (1 << Java20Parser.INT) | (1 << Java20Parser.LONG) | (1 << Java20Parser.NEW) | (1 << Java20Parser.SHORT) | (1 << Java20Parser.SUPER) | (1 << Java20Parser.SWITCH) | (1 << Java20Parser.THIS))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (Java20Parser.VOID - 65)) | (1 << (Java20Parser.IntegerLiteral - 65)) | (1 << (Java20Parser.FloatingPointLiteral - 65)) | (1 << (Java20Parser.BooleanLiteral - 65)) | (1 << (Java20Parser.CharacterLiteral - 65)) | (1 << (Java20Parser.StringLiteral - 65)) | (1 << (Java20Parser.TextBlock - 65)) | (1 << (Java20Parser.NullLiteral - 65)) | (1 << (Java20Parser.LPAREN - 65)) | (1 << (Java20Parser.AT - 65)) | (1 << (Java20Parser.BANG - 65)) | (1 << (Java20Parser.TILDE - 65)) | (1 << (Java20Parser.INC - 65)) | (1 << (Java20Parser.DEC - 65)) | (1 << (Java20Parser.ADD - 65)) | (1 << (Java20Parser.SUB - 65)) | (1 << (Java20Parser.Identifier - 65)))) != 0):
                    self.state = 2564
                    self.argumentList()


                self.state = 2567
                self.match(Java20Parser.RPAREN)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 2569
                self.match(Java20Parser.SUPER)
                self.state = 2570
                self.match(Java20Parser.DOT)
                self.state = 2572
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Java20Parser.LT:
                    self.state = 2571
                    self.typeArguments()


                self.state = 2574
                self.identifier()
                self.state = 2575
                self.match(Java20Parser.LPAREN)
                self.state = 2577
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java20Parser.EXPORTS) | (1 << Java20Parser.MODULE) | (1 << Java20Parser.NONSEALED) | (1 << Java20Parser.OPEN) | (1 << Java20Parser.OPENS) | (1 << Java20Parser.PERMITS) | (1 << Java20Parser.PROVIDES) | (1 << Java20Parser.RECORD) | (1 << Java20Parser.REQUIRES) | (1 << Java20Parser.SEALED) | (1 << Java20Parser.TO) | (1 << Java20Parser.TRANSITIVE) | (1 << Java20Parser.USES) | (1 << Java20Parser.VAR) | (1 << Java20Parser.WITH) | (1 << Java20Parser.YIELD) | (1 << Java20Parser.BOOLEAN) | (1 << Java20Parser.BYTE) | (1 << Java20Parser.CHAR) | (1 << Java20Parser.DOUBLE) | (1 << Java20Parser.FLOAT) | (1 << Java20Parser.INT) | (1 << Java20Parser.LONG) | (1 << Java20Parser.NEW) | (1 << Java20Parser.SHORT) | (1 << Java20Parser.SUPER) | (1 << Java20Parser.SWITCH) | (1 << Java20Parser.THIS))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (Java20Parser.VOID - 65)) | (1 << (Java20Parser.IntegerLiteral - 65)) | (1 << (Java20Parser.FloatingPointLiteral - 65)) | (1 << (Java20Parser.BooleanLiteral - 65)) | (1 << (Java20Parser.CharacterLiteral - 65)) | (1 << (Java20Parser.StringLiteral - 65)) | (1 << (Java20Parser.TextBlock - 65)) | (1 << (Java20Parser.NullLiteral - 65)) | (1 << (Java20Parser.LPAREN - 65)) | (1 << (Java20Parser.AT - 65)) | (1 << (Java20Parser.BANG - 65)) | (1 << (Java20Parser.TILDE - 65)) | (1 << (Java20Parser.INC - 65)) | (1 << (Java20Parser.DEC - 65)) | (1 << (Java20Parser.ADD - 65)) | (1 << (Java20Parser.SUB - 65)) | (1 << (Java20Parser.Identifier - 65)))) != 0):
                    self.state = 2576
                    self.argumentList()


                self.state = 2579
                self.match(Java20Parser.RPAREN)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 2581
                self.typeName()
                self.state = 2582
                self.match(Java20Parser.DOT)
                self.state = 2583
                self.match(Java20Parser.SUPER)
                self.state = 2584
                self.match(Java20Parser.DOT)
                self.state = 2586
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Java20Parser.LT:
                    self.state = 2585
                    self.typeArguments()


                self.state = 2588
                self.identifier()
                self.state = 2589
                self.match(Java20Parser.LPAREN)
                self.state = 2591
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java20Parser.EXPORTS) | (1 << Java20Parser.MODULE) | (1 << Java20Parser.NONSEALED) | (1 << Java20Parser.OPEN) | (1 << Java20Parser.OPENS) | (1 << Java20Parser.PERMITS) | (1 << Java20Parser.PROVIDES) | (1 << Java20Parser.RECORD) | (1 << Java20Parser.REQUIRES) | (1 << Java20Parser.SEALED) | (1 << Java20Parser.TO) | (1 << Java20Parser.TRANSITIVE) | (1 << Java20Parser.USES) | (1 << Java20Parser.VAR) | (1 << Java20Parser.WITH) | (1 << Java20Parser.YIELD) | (1 << Java20Parser.BOOLEAN) | (1 << Java20Parser.BYTE) | (1 << Java20Parser.CHAR) | (1 << Java20Parser.DOUBLE) | (1 << Java20Parser.FLOAT) | (1 << Java20Parser.INT) | (1 << Java20Parser.LONG) | (1 << Java20Parser.NEW) | (1 << Java20Parser.SHORT) | (1 << Java20Parser.SUPER) | (1 << Java20Parser.SWITCH) | (1 << Java20Parser.THIS))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (Java20Parser.VOID - 65)) | (1 << (Java20Parser.IntegerLiteral - 65)) | (1 << (Java20Parser.FloatingPointLiteral - 65)) | (1 << (Java20Parser.BooleanLiteral - 65)) | (1 << (Java20Parser.CharacterLiteral - 65)) | (1 << (Java20Parser.StringLiteral - 65)) | (1 << (Java20Parser.TextBlock - 65)) | (1 << (Java20Parser.NullLiteral - 65)) | (1 << (Java20Parser.LPAREN - 65)) | (1 << (Java20Parser.AT - 65)) | (1 << (Java20Parser.BANG - 65)) | (1 << (Java20Parser.TILDE - 65)) | (1 << (Java20Parser.INC - 65)) | (1 << (Java20Parser.DEC - 65)) | (1 << (Java20Parser.ADD - 65)) | (1 << (Java20Parser.SUB - 65)) | (1 << (Java20Parser.Identifier - 65)))) != 0):
                    self.state = 2590
                    self.argumentList()


                self.state = 2593
                self.match(Java20Parser.RPAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(Java20Parser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(Java20Parser.COMMA)
            else:
                return self.getToken(Java20Parser.COMMA, i)

        def getRuleIndex(self):
            return Java20Parser.RULE_argumentList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumentList" ):
                listener.enterArgumentList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumentList" ):
                listener.exitArgumentList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentList" ):
                return visitor.visitArgumentList(self)
            else:
                return visitor.visitChildren(self)




    def argumentList(self):

        localctx = Java20Parser.ArgumentListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 430, self.RULE_argumentList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2597
            self.expression()
            self.state = 2602
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Java20Parser.COMMA:
                self.state = 2598
                self.match(Java20Parser.COMMA)
                self.state = 2599
                self.expression()
                self.state = 2604
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodReferenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressionName(self):
            return self.getTypedRuleContext(Java20Parser.ExpressionNameContext,0)


        def COLONCOLON(self):
            return self.getToken(Java20Parser.COLONCOLON, 0)

        def identifier(self):
            return self.getTypedRuleContext(Java20Parser.IdentifierContext,0)


        def typeArguments(self):
            return self.getTypedRuleContext(Java20Parser.TypeArgumentsContext,0)


        def primary(self):
            return self.getTypedRuleContext(Java20Parser.PrimaryContext,0)


        def referenceType(self):
            return self.getTypedRuleContext(Java20Parser.ReferenceTypeContext,0)


        def SUPER(self):
            return self.getToken(Java20Parser.SUPER, 0)

        def typeName(self):
            return self.getTypedRuleContext(Java20Parser.TypeNameContext,0)


        def DOT(self):
            return self.getToken(Java20Parser.DOT, 0)

        def classType(self):
            return self.getTypedRuleContext(Java20Parser.ClassTypeContext,0)


        def NEW(self):
            return self.getToken(Java20Parser.NEW, 0)

        def arrayType(self):
            return self.getTypedRuleContext(Java20Parser.ArrayTypeContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_methodReference

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodReference" ):
                listener.enterMethodReference(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodReference" ):
                listener.exitMethodReference(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodReference" ):
                return visitor.visitMethodReference(self)
            else:
                return visitor.visitChildren(self)




    def methodReference(self):

        localctx = Java20Parser.MethodReferenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 432, self.RULE_methodReference)
        self._la = 0 # Token type
        try:
            self.state = 2652
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,322,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2605
                self.expressionName()
                self.state = 2606
                self.match(Java20Parser.COLONCOLON)
                self.state = 2608
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Java20Parser.LT:
                    self.state = 2607
                    self.typeArguments()


                self.state = 2610
                self.identifier()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2612
                self.primary()
                self.state = 2613
                self.match(Java20Parser.COLONCOLON)
                self.state = 2615
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Java20Parser.LT:
                    self.state = 2614
                    self.typeArguments()


                self.state = 2617
                self.identifier()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2619
                self.referenceType()
                self.state = 2620
                self.match(Java20Parser.COLONCOLON)
                self.state = 2622
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Java20Parser.LT:
                    self.state = 2621
                    self.typeArguments()


                self.state = 2624
                self.identifier()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 2626
                self.match(Java20Parser.SUPER)
                self.state = 2627
                self.match(Java20Parser.COLONCOLON)
                self.state = 2629
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Java20Parser.LT:
                    self.state = 2628
                    self.typeArguments()


                self.state = 2631
                self.identifier()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 2632
                self.typeName()
                self.state = 2633
                self.match(Java20Parser.DOT)
                self.state = 2634
                self.match(Java20Parser.SUPER)
                self.state = 2635
                self.match(Java20Parser.COLONCOLON)
                self.state = 2637
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Java20Parser.LT:
                    self.state = 2636
                    self.typeArguments()


                self.state = 2639
                self.identifier()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 2641
                self.classType()
                self.state = 2642
                self.match(Java20Parser.COLONCOLON)
                self.state = 2644
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Java20Parser.LT:
                    self.state = 2643
                    self.typeArguments()


                self.state = 2646
                self.match(Java20Parser.NEW)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 2648
                self.arrayType()
                self.state = 2649
                self.match(Java20Parser.COLONCOLON)
                self.state = 2650
                self.match(Java20Parser.NEW)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PostfixExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primary(self):
            return self.getTypedRuleContext(Java20Parser.PrimaryContext,0)


        def pfE(self):
            return self.getTypedRuleContext(Java20Parser.PfEContext,0)


        def expressionName(self):
            return self.getTypedRuleContext(Java20Parser.ExpressionNameContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_postfixExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPostfixExpression" ):
                listener.enterPostfixExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPostfixExpression" ):
                listener.exitPostfixExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPostfixExpression" ):
                return visitor.visitPostfixExpression(self)
            else:
                return visitor.visitChildren(self)




    def postfixExpression(self):

        localctx = Java20Parser.PostfixExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 434, self.RULE_postfixExpression)
        try:
            self.state = 2662
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,325,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2654
                self.primary()
                self.state = 2656
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,323,self._ctx)
                if la_ == 1:
                    self.state = 2655
                    self.pfE()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2658
                self.expressionName()
                self.state = 2660
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,324,self._ctx)
                if la_ == 1:
                    self.state = 2659
                    self.pfE()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PfEContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INC(self):
            return self.getToken(Java20Parser.INC, 0)

        def pfE(self):
            return self.getTypedRuleContext(Java20Parser.PfEContext,0)


        def DEC(self):
            return self.getToken(Java20Parser.DEC, 0)

        def getRuleIndex(self):
            return Java20Parser.RULE_pfE

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPfE" ):
                listener.enterPfE(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPfE" ):
                listener.exitPfE(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPfE" ):
                return visitor.visitPfE(self)
            else:
                return visitor.visitChildren(self)




    def pfE(self):

        localctx = Java20Parser.PfEContext(self, self._ctx, self.state)
        self.enterRule(localctx, 436, self.RULE_pfE)
        try:
            self.state = 2672
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Java20Parser.INC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2664
                self.match(Java20Parser.INC)
                self.state = 2666
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,326,self._ctx)
                if la_ == 1:
                    self.state = 2665
                    self.pfE()


                pass
            elif token in [Java20Parser.DEC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2668
                self.match(Java20Parser.DEC)
                self.state = 2670
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,327,self._ctx)
                if la_ == 1:
                    self.state = 2669
                    self.pfE()


                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PostIncrementExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def postfixExpression(self):
            return self.getTypedRuleContext(Java20Parser.PostfixExpressionContext,0)


        def INC(self):
            return self.getToken(Java20Parser.INC, 0)

        def getRuleIndex(self):
            return Java20Parser.RULE_postIncrementExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPostIncrementExpression" ):
                listener.enterPostIncrementExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPostIncrementExpression" ):
                listener.exitPostIncrementExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPostIncrementExpression" ):
                return visitor.visitPostIncrementExpression(self)
            else:
                return visitor.visitChildren(self)




    def postIncrementExpression(self):

        localctx = Java20Parser.PostIncrementExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 438, self.RULE_postIncrementExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2674
            self.postfixExpression()
            self.state = 2675
            self.match(Java20Parser.INC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PostDecrementExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def postfixExpression(self):
            return self.getTypedRuleContext(Java20Parser.PostfixExpressionContext,0)


        def DEC(self):
            return self.getToken(Java20Parser.DEC, 0)

        def getRuleIndex(self):
            return Java20Parser.RULE_postDecrementExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPostDecrementExpression" ):
                listener.enterPostDecrementExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPostDecrementExpression" ):
                listener.exitPostDecrementExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPostDecrementExpression" ):
                return visitor.visitPostDecrementExpression(self)
            else:
                return visitor.visitChildren(self)




    def postDecrementExpression(self):

        localctx = Java20Parser.PostDecrementExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 440, self.RULE_postDecrementExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2677
            self.postfixExpression()
            self.state = 2678
            self.match(Java20Parser.DEC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def preIncrementExpression(self):
            return self.getTypedRuleContext(Java20Parser.PreIncrementExpressionContext,0)


        def preDecrementExpression(self):
            return self.getTypedRuleContext(Java20Parser.PreDecrementExpressionContext,0)


        def ADD(self):
            return self.getToken(Java20Parser.ADD, 0)

        def unaryExpression(self):
            return self.getTypedRuleContext(Java20Parser.UnaryExpressionContext,0)


        def SUB(self):
            return self.getToken(Java20Parser.SUB, 0)

        def unaryExpressionNotPlusMinus(self):
            return self.getTypedRuleContext(Java20Parser.UnaryExpressionNotPlusMinusContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_unaryExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryExpression" ):
                listener.enterUnaryExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryExpression" ):
                listener.exitUnaryExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryExpression" ):
                return visitor.visitUnaryExpression(self)
            else:
                return visitor.visitChildren(self)




    def unaryExpression(self):

        localctx = Java20Parser.UnaryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 442, self.RULE_unaryExpression)
        try:
            self.state = 2687
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Java20Parser.INC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2680
                self.preIncrementExpression()
                pass
            elif token in [Java20Parser.DEC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2681
                self.preDecrementExpression()
                pass
            elif token in [Java20Parser.ADD]:
                self.enterOuterAlt(localctx, 3)
                self.state = 2682
                self.match(Java20Parser.ADD)
                self.state = 2683
                self.unaryExpression()
                pass
            elif token in [Java20Parser.SUB]:
                self.enterOuterAlt(localctx, 4)
                self.state = 2684
                self.match(Java20Parser.SUB)
                self.state = 2685
                self.unaryExpression()
                pass
            elif token in [Java20Parser.EXPORTS, Java20Parser.MODULE, Java20Parser.NONSEALED, Java20Parser.OPEN, Java20Parser.OPENS, Java20Parser.PERMITS, Java20Parser.PROVIDES, Java20Parser.RECORD, Java20Parser.REQUIRES, Java20Parser.SEALED, Java20Parser.TO, Java20Parser.TRANSITIVE, Java20Parser.USES, Java20Parser.VAR, Java20Parser.WITH, Java20Parser.YIELD, Java20Parser.BOOLEAN, Java20Parser.BYTE, Java20Parser.CHAR, Java20Parser.DOUBLE, Java20Parser.FLOAT, Java20Parser.INT, Java20Parser.LONG, Java20Parser.NEW, Java20Parser.SHORT, Java20Parser.SUPER, Java20Parser.SWITCH, Java20Parser.THIS, Java20Parser.VOID, Java20Parser.IntegerLiteral, Java20Parser.FloatingPointLiteral, Java20Parser.BooleanLiteral, Java20Parser.CharacterLiteral, Java20Parser.StringLiteral, Java20Parser.TextBlock, Java20Parser.NullLiteral, Java20Parser.LPAREN, Java20Parser.AT, Java20Parser.BANG, Java20Parser.TILDE, Java20Parser.Identifier]:
                self.enterOuterAlt(localctx, 5)
                self.state = 2686
                self.unaryExpressionNotPlusMinus()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PreIncrementExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INC(self):
            return self.getToken(Java20Parser.INC, 0)

        def unaryExpression(self):
            return self.getTypedRuleContext(Java20Parser.UnaryExpressionContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_preIncrementExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPreIncrementExpression" ):
                listener.enterPreIncrementExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPreIncrementExpression" ):
                listener.exitPreIncrementExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPreIncrementExpression" ):
                return visitor.visitPreIncrementExpression(self)
            else:
                return visitor.visitChildren(self)




    def preIncrementExpression(self):

        localctx = Java20Parser.PreIncrementExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 444, self.RULE_preIncrementExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2689
            self.match(Java20Parser.INC)
            self.state = 2690
            self.unaryExpression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PreDecrementExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEC(self):
            return self.getToken(Java20Parser.DEC, 0)

        def unaryExpression(self):
            return self.getTypedRuleContext(Java20Parser.UnaryExpressionContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_preDecrementExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPreDecrementExpression" ):
                listener.enterPreDecrementExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPreDecrementExpression" ):
                listener.exitPreDecrementExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPreDecrementExpression" ):
                return visitor.visitPreDecrementExpression(self)
            else:
                return visitor.visitChildren(self)




    def preDecrementExpression(self):

        localctx = Java20Parser.PreDecrementExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 446, self.RULE_preDecrementExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2692
            self.match(Java20Parser.DEC)
            self.state = 2693
            self.unaryExpression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryExpressionNotPlusMinusContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def postfixExpression(self):
            return self.getTypedRuleContext(Java20Parser.PostfixExpressionContext,0)


        def TILDE(self):
            return self.getToken(Java20Parser.TILDE, 0)

        def unaryExpression(self):
            return self.getTypedRuleContext(Java20Parser.UnaryExpressionContext,0)


        def BANG(self):
            return self.getToken(Java20Parser.BANG, 0)

        def castExpression(self):
            return self.getTypedRuleContext(Java20Parser.CastExpressionContext,0)


        def switchExpression(self):
            return self.getTypedRuleContext(Java20Parser.SwitchExpressionContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_unaryExpressionNotPlusMinus

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryExpressionNotPlusMinus" ):
                listener.enterUnaryExpressionNotPlusMinus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryExpressionNotPlusMinus" ):
                listener.exitUnaryExpressionNotPlusMinus(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryExpressionNotPlusMinus" ):
                return visitor.visitUnaryExpressionNotPlusMinus(self)
            else:
                return visitor.visitChildren(self)




    def unaryExpressionNotPlusMinus(self):

        localctx = Java20Parser.UnaryExpressionNotPlusMinusContext(self, self._ctx, self.state)
        self.enterRule(localctx, 448, self.RULE_unaryExpressionNotPlusMinus)
        try:
            self.state = 2702
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,330,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2695
                self.postfixExpression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2696
                self.match(Java20Parser.TILDE)
                self.state = 2697
                self.unaryExpression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2698
                self.match(Java20Parser.BANG)
                self.state = 2699
                self.unaryExpression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 2700
                self.castExpression()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 2701
                self.switchExpression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CastExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(Java20Parser.LPAREN, 0)

        def primitiveType(self):
            return self.getTypedRuleContext(Java20Parser.PrimitiveTypeContext,0)


        def RPAREN(self):
            return self.getToken(Java20Parser.RPAREN, 0)

        def unaryExpression(self):
            return self.getTypedRuleContext(Java20Parser.UnaryExpressionContext,0)


        def referenceType(self):
            return self.getTypedRuleContext(Java20Parser.ReferenceTypeContext,0)


        def unaryExpressionNotPlusMinus(self):
            return self.getTypedRuleContext(Java20Parser.UnaryExpressionNotPlusMinusContext,0)


        def additionalBound(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.AdditionalBoundContext)
            else:
                return self.getTypedRuleContext(Java20Parser.AdditionalBoundContext,i)


        def lambdaExpression(self):
            return self.getTypedRuleContext(Java20Parser.LambdaExpressionContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_castExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCastExpression" ):
                listener.enterCastExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCastExpression" ):
                listener.exitCastExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCastExpression" ):
                return visitor.visitCastExpression(self)
            else:
                return visitor.visitChildren(self)




    def castExpression(self):

        localctx = Java20Parser.CastExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 450, self.RULE_castExpression)
        self._la = 0 # Token type
        try:
            self.state = 2731
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,333,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2704
                self.match(Java20Parser.LPAREN)
                self.state = 2705
                self.primitiveType()
                self.state = 2706
                self.match(Java20Parser.RPAREN)
                self.state = 2707
                self.unaryExpression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2709
                self.match(Java20Parser.LPAREN)
                self.state = 2710
                self.referenceType()
                self.state = 2714
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==Java20Parser.BITAND:
                    self.state = 2711
                    self.additionalBound()
                    self.state = 2716
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 2717
                self.match(Java20Parser.RPAREN)
                self.state = 2718
                self.unaryExpressionNotPlusMinus()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2720
                self.match(Java20Parser.LPAREN)
                self.state = 2721
                self.referenceType()
                self.state = 2725
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==Java20Parser.BITAND:
                    self.state = 2722
                    self.additionalBound()
                    self.state = 2727
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 2728
                self.match(Java20Parser.RPAREN)
                self.state = 2729
                self.lambdaExpression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplicativeExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryExpression(self):
            return self.getTypedRuleContext(Java20Parser.UnaryExpressionContext,0)


        def multiplicativeExpression(self):
            return self.getTypedRuleContext(Java20Parser.MultiplicativeExpressionContext,0)


        def MUL(self):
            return self.getToken(Java20Parser.MUL, 0)

        def DIV(self):
            return self.getToken(Java20Parser.DIV, 0)

        def MOD(self):
            return self.getToken(Java20Parser.MOD, 0)

        def getRuleIndex(self):
            return Java20Parser.RULE_multiplicativeExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicativeExpression" ):
                listener.enterMultiplicativeExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicativeExpression" ):
                listener.exitMultiplicativeExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicativeExpression" ):
                return visitor.visitMultiplicativeExpression(self)
            else:
                return visitor.visitChildren(self)



    def multiplicativeExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = Java20Parser.MultiplicativeExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 452
        self.enterRecursionRule(localctx, 452, self.RULE_multiplicativeExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2734
            self.unaryExpression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 2747
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,335,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 2745
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,334,self._ctx)
                    if la_ == 1:
                        localctx = Java20Parser.MultiplicativeExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplicativeExpression)
                        self.state = 2736
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 2737
                        self.match(Java20Parser.MUL)
                        self.state = 2738
                        self.unaryExpression()
                        pass

                    elif la_ == 2:
                        localctx = Java20Parser.MultiplicativeExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplicativeExpression)
                        self.state = 2739
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 2740
                        self.match(Java20Parser.DIV)
                        self.state = 2741
                        self.unaryExpression()
                        pass

                    elif la_ == 3:
                        localctx = Java20Parser.MultiplicativeExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplicativeExpression)
                        self.state = 2742
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 2743
                        self.match(Java20Parser.MOD)
                        self.state = 2744
                        self.unaryExpression()
                        pass

             
                self.state = 2749
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,335,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AdditiveExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicativeExpression(self):
            return self.getTypedRuleContext(Java20Parser.MultiplicativeExpressionContext,0)


        def additiveExpression(self):
            return self.getTypedRuleContext(Java20Parser.AdditiveExpressionContext,0)


        def ADD(self):
            return self.getToken(Java20Parser.ADD, 0)

        def SUB(self):
            return self.getToken(Java20Parser.SUB, 0)

        def getRuleIndex(self):
            return Java20Parser.RULE_additiveExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditiveExpression" ):
                listener.enterAdditiveExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditiveExpression" ):
                listener.exitAdditiveExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditiveExpression" ):
                return visitor.visitAdditiveExpression(self)
            else:
                return visitor.visitChildren(self)



    def additiveExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = Java20Parser.AdditiveExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 454
        self.enterRecursionRule(localctx, 454, self.RULE_additiveExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2751
            self.multiplicativeExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2761
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,337,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 2759
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,336,self._ctx)
                    if la_ == 1:
                        localctx = Java20Parser.AdditiveExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_additiveExpression)
                        self.state = 2753
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 2754
                        self.match(Java20Parser.ADD)
                        self.state = 2755
                        self.multiplicativeExpression(0)
                        pass

                    elif la_ == 2:
                        localctx = Java20Parser.AdditiveExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_additiveExpression)
                        self.state = 2756
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 2757
                        self.match(Java20Parser.SUB)
                        self.state = 2758
                        self.multiplicativeExpression(0)
                        pass

             
                self.state = 2763
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,337,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ShiftExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additiveExpression(self):
            return self.getTypedRuleContext(Java20Parser.AdditiveExpressionContext,0)


        def shiftExpression(self):
            return self.getTypedRuleContext(Java20Parser.ShiftExpressionContext,0)


        def LT(self, i:int=None):
            if i is None:
                return self.getTokens(Java20Parser.LT)
            else:
                return self.getToken(Java20Parser.LT, i)

        def GT(self, i:int=None):
            if i is None:
                return self.getTokens(Java20Parser.GT)
            else:
                return self.getToken(Java20Parser.GT, i)

        def getRuleIndex(self):
            return Java20Parser.RULE_shiftExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterShiftExpression" ):
                listener.enterShiftExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitShiftExpression" ):
                listener.exitShiftExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitShiftExpression" ):
                return visitor.visitShiftExpression(self)
            else:
                return visitor.visitChildren(self)



    def shiftExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = Java20Parser.ShiftExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 456
        self.enterRecursionRule(localctx, 456, self.RULE_shiftExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2765
            self.additiveExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2782
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,339,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 2780
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,338,self._ctx)
                    if la_ == 1:
                        localctx = Java20Parser.ShiftExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_shiftExpression)
                        self.state = 2767
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 2768
                        self.match(Java20Parser.LT)
                        self.state = 2769
                        self.match(Java20Parser.LT)
                        self.state = 2770
                        self.additiveExpression(0)
                        pass

                    elif la_ == 2:
                        localctx = Java20Parser.ShiftExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_shiftExpression)
                        self.state = 2771
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 2772
                        self.match(Java20Parser.GT)
                        self.state = 2773
                        self.match(Java20Parser.GT)
                        self.state = 2774
                        self.additiveExpression(0)
                        pass

                    elif la_ == 3:
                        localctx = Java20Parser.ShiftExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_shiftExpression)
                        self.state = 2775
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 2776
                        self.match(Java20Parser.GT)
                        self.state = 2777
                        self.match(Java20Parser.GT)
                        self.state = 2778
                        self.match(Java20Parser.GT)
                        self.state = 2779
                        self.additiveExpression(0)
                        pass

             
                self.state = 2784
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,339,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class RelationalExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def shiftExpression(self):
            return self.getTypedRuleContext(Java20Parser.ShiftExpressionContext,0)


        def relationalExpression(self):
            return self.getTypedRuleContext(Java20Parser.RelationalExpressionContext,0)


        def LT(self):
            return self.getToken(Java20Parser.LT, 0)

        def GT(self):
            return self.getToken(Java20Parser.GT, 0)

        def LE(self):
            return self.getToken(Java20Parser.LE, 0)

        def GE(self):
            return self.getToken(Java20Parser.GE, 0)

        def INSTANCEOF(self):
            return self.getToken(Java20Parser.INSTANCEOF, 0)

        def referenceType(self):
            return self.getTypedRuleContext(Java20Parser.ReferenceTypeContext,0)


        def pattern(self):
            return self.getTypedRuleContext(Java20Parser.PatternContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_relationalExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelationalExpression" ):
                listener.enterRelationalExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelationalExpression" ):
                listener.exitRelationalExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelationalExpression" ):
                return visitor.visitRelationalExpression(self)
            else:
                return visitor.visitChildren(self)



    def relationalExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = Java20Parser.RelationalExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 458
        self.enterRecursionRule(localctx, 458, self.RULE_relationalExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2786
            self.shiftExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2808
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,342,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 2806
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,341,self._ctx)
                    if la_ == 1:
                        localctx = Java20Parser.RelationalExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_relationalExpression)
                        self.state = 2788
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 2789
                        self.match(Java20Parser.LT)
                        self.state = 2790
                        self.shiftExpression(0)
                        pass

                    elif la_ == 2:
                        localctx = Java20Parser.RelationalExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_relationalExpression)
                        self.state = 2791
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 2792
                        self.match(Java20Parser.GT)
                        self.state = 2793
                        self.shiftExpression(0)
                        pass

                    elif la_ == 3:
                        localctx = Java20Parser.RelationalExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_relationalExpression)
                        self.state = 2794
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 2795
                        self.match(Java20Parser.LE)
                        self.state = 2796
                        self.shiftExpression(0)
                        pass

                    elif la_ == 4:
                        localctx = Java20Parser.RelationalExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_relationalExpression)
                        self.state = 2797
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 2798
                        self.match(Java20Parser.GE)
                        self.state = 2799
                        self.shiftExpression(0)
                        pass

                    elif la_ == 5:
                        localctx = Java20Parser.RelationalExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_relationalExpression)
                        self.state = 2800
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 2801
                        self.match(Java20Parser.INSTANCEOF)
                        self.state = 2804
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,340,self._ctx)
                        if la_ == 1:
                            self.state = 2802
                            self.referenceType()
                            pass

                        elif la_ == 2:
                            self.state = 2803
                            self.pattern()
                            pass


                        pass

             
                self.state = 2810
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,342,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class EqualityExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relationalExpression(self):
            return self.getTypedRuleContext(Java20Parser.RelationalExpressionContext,0)


        def equalityExpression(self):
            return self.getTypedRuleContext(Java20Parser.EqualityExpressionContext,0)


        def EQUAL(self):
            return self.getToken(Java20Parser.EQUAL, 0)

        def NOTEQUAL(self):
            return self.getToken(Java20Parser.NOTEQUAL, 0)

        def getRuleIndex(self):
            return Java20Parser.RULE_equalityExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqualityExpression" ):
                listener.enterEqualityExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqualityExpression" ):
                listener.exitEqualityExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqualityExpression" ):
                return visitor.visitEqualityExpression(self)
            else:
                return visitor.visitChildren(self)



    def equalityExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = Java20Parser.EqualityExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 460
        self.enterRecursionRule(localctx, 460, self.RULE_equalityExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2812
            self.relationalExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2822
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,344,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 2820
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,343,self._ctx)
                    if la_ == 1:
                        localctx = Java20Parser.EqualityExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_equalityExpression)
                        self.state = 2814
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 2815
                        self.match(Java20Parser.EQUAL)
                        self.state = 2816
                        self.relationalExpression(0)
                        pass

                    elif la_ == 2:
                        localctx = Java20Parser.EqualityExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_equalityExpression)
                        self.state = 2817
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 2818
                        self.match(Java20Parser.NOTEQUAL)
                        self.state = 2819
                        self.relationalExpression(0)
                        pass

             
                self.state = 2824
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,344,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AndExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def equalityExpression(self):
            return self.getTypedRuleContext(Java20Parser.EqualityExpressionContext,0)


        def andExpression(self):
            return self.getTypedRuleContext(Java20Parser.AndExpressionContext,0)


        def BITAND(self):
            return self.getToken(Java20Parser.BITAND, 0)

        def getRuleIndex(self):
            return Java20Parser.RULE_andExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndExpression" ):
                listener.enterAndExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndExpression" ):
                listener.exitAndExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAndExpression" ):
                return visitor.visitAndExpression(self)
            else:
                return visitor.visitChildren(self)



    def andExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = Java20Parser.AndExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 462
        self.enterRecursionRule(localctx, 462, self.RULE_andExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2826
            self.equalityExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2833
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,345,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = Java20Parser.AndExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_andExpression)
                    self.state = 2828
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2829
                    self.match(Java20Parser.BITAND)
                    self.state = 2830
                    self.equalityExpression(0) 
                self.state = 2835
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,345,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ExclusiveOrExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def andExpression(self):
            return self.getTypedRuleContext(Java20Parser.AndExpressionContext,0)


        def exclusiveOrExpression(self):
            return self.getTypedRuleContext(Java20Parser.ExclusiveOrExpressionContext,0)


        def CARET(self):
            return self.getToken(Java20Parser.CARET, 0)

        def getRuleIndex(self):
            return Java20Parser.RULE_exclusiveOrExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExclusiveOrExpression" ):
                listener.enterExclusiveOrExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExclusiveOrExpression" ):
                listener.exitExclusiveOrExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExclusiveOrExpression" ):
                return visitor.visitExclusiveOrExpression(self)
            else:
                return visitor.visitChildren(self)



    def exclusiveOrExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = Java20Parser.ExclusiveOrExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 464
        self.enterRecursionRule(localctx, 464, self.RULE_exclusiveOrExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2837
            self.andExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2844
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,346,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = Java20Parser.ExclusiveOrExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exclusiveOrExpression)
                    self.state = 2839
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2840
                    self.match(Java20Parser.CARET)
                    self.state = 2841
                    self.andExpression(0) 
                self.state = 2846
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,346,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class InclusiveOrExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exclusiveOrExpression(self):
            return self.getTypedRuleContext(Java20Parser.ExclusiveOrExpressionContext,0)


        def inclusiveOrExpression(self):
            return self.getTypedRuleContext(Java20Parser.InclusiveOrExpressionContext,0)


        def BITOR(self):
            return self.getToken(Java20Parser.BITOR, 0)

        def getRuleIndex(self):
            return Java20Parser.RULE_inclusiveOrExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInclusiveOrExpression" ):
                listener.enterInclusiveOrExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInclusiveOrExpression" ):
                listener.exitInclusiveOrExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInclusiveOrExpression" ):
                return visitor.visitInclusiveOrExpression(self)
            else:
                return visitor.visitChildren(self)



    def inclusiveOrExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = Java20Parser.InclusiveOrExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 466
        self.enterRecursionRule(localctx, 466, self.RULE_inclusiveOrExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2848
            self.exclusiveOrExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2855
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,347,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = Java20Parser.InclusiveOrExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_inclusiveOrExpression)
                    self.state = 2850
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2851
                    self.match(Java20Parser.BITOR)
                    self.state = 2852
                    self.exclusiveOrExpression(0) 
                self.state = 2857
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,347,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ConditionalAndExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def inclusiveOrExpression(self):
            return self.getTypedRuleContext(Java20Parser.InclusiveOrExpressionContext,0)


        def conditionalAndExpression(self):
            return self.getTypedRuleContext(Java20Parser.ConditionalAndExpressionContext,0)


        def AND(self):
            return self.getToken(Java20Parser.AND, 0)

        def getRuleIndex(self):
            return Java20Parser.RULE_conditionalAndExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditionalAndExpression" ):
                listener.enterConditionalAndExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditionalAndExpression" ):
                listener.exitConditionalAndExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditionalAndExpression" ):
                return visitor.visitConditionalAndExpression(self)
            else:
                return visitor.visitChildren(self)



    def conditionalAndExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = Java20Parser.ConditionalAndExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 468
        self.enterRecursionRule(localctx, 468, self.RULE_conditionalAndExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2859
            self.inclusiveOrExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2866
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,348,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = Java20Parser.ConditionalAndExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_conditionalAndExpression)
                    self.state = 2861
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2862
                    self.match(Java20Parser.AND)
                    self.state = 2863
                    self.inclusiveOrExpression(0) 
                self.state = 2868
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,348,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ConditionalOrExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conditionalAndExpression(self):
            return self.getTypedRuleContext(Java20Parser.ConditionalAndExpressionContext,0)


        def conditionalOrExpression(self):
            return self.getTypedRuleContext(Java20Parser.ConditionalOrExpressionContext,0)


        def OR(self):
            return self.getToken(Java20Parser.OR, 0)

        def getRuleIndex(self):
            return Java20Parser.RULE_conditionalOrExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditionalOrExpression" ):
                listener.enterConditionalOrExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditionalOrExpression" ):
                listener.exitConditionalOrExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditionalOrExpression" ):
                return visitor.visitConditionalOrExpression(self)
            else:
                return visitor.visitChildren(self)



    def conditionalOrExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = Java20Parser.ConditionalOrExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 470
        self.enterRecursionRule(localctx, 470, self.RULE_conditionalOrExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2870
            self.conditionalAndExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 2877
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,349,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = Java20Parser.ConditionalOrExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_conditionalOrExpression)
                    self.state = 2872
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 2873
                    self.match(Java20Parser.OR)
                    self.state = 2874
                    self.conditionalAndExpression(0) 
                self.state = 2879
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,349,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ConditionalExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conditionalOrExpression(self):
            return self.getTypedRuleContext(Java20Parser.ConditionalOrExpressionContext,0)


        def QUESTION(self):
            return self.getToken(Java20Parser.QUESTION, 0)

        def expression(self):
            return self.getTypedRuleContext(Java20Parser.ExpressionContext,0)


        def COLON(self):
            return self.getToken(Java20Parser.COLON, 0)

        def conditionalExpression(self):
            return self.getTypedRuleContext(Java20Parser.ConditionalExpressionContext,0)


        def lambdaExpression(self):
            return self.getTypedRuleContext(Java20Parser.LambdaExpressionContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_conditionalExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditionalExpression" ):
                listener.enterConditionalExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditionalExpression" ):
                listener.exitConditionalExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditionalExpression" ):
                return visitor.visitConditionalExpression(self)
            else:
                return visitor.visitChildren(self)




    def conditionalExpression(self):

        localctx = Java20Parser.ConditionalExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 472, self.RULE_conditionalExpression)
        try:
            self.state = 2893
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,350,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2880
                self.conditionalOrExpression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2881
                self.conditionalOrExpression(0)
                self.state = 2882
                self.match(Java20Parser.QUESTION)
                self.state = 2883
                self.expression()
                self.state = 2884
                self.match(Java20Parser.COLON)
                self.state = 2885
                self.conditionalExpression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2887
                self.conditionalOrExpression(0)
                self.state = 2888
                self.match(Java20Parser.QUESTION)
                self.state = 2889
                self.expression()
                self.state = 2890
                self.match(Java20Parser.COLON)
                self.state = 2891
                self.lambdaExpression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conditionalExpression(self):
            return self.getTypedRuleContext(Java20Parser.ConditionalExpressionContext,0)


        def assignment(self):
            return self.getTypedRuleContext(Java20Parser.AssignmentContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_assignmentExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentExpression" ):
                listener.enterAssignmentExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentExpression" ):
                listener.exitAssignmentExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentExpression" ):
                return visitor.visitAssignmentExpression(self)
            else:
                return visitor.visitChildren(self)




    def assignmentExpression(self):

        localctx = Java20Parser.AssignmentExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 474, self.RULE_assignmentExpression)
        try:
            self.state = 2897
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,351,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2895
                self.conditionalExpression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2896
                self.assignment()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def leftHandSide(self):
            return self.getTypedRuleContext(Java20Parser.LeftHandSideContext,0)


        def assignmentOperator(self):
            return self.getTypedRuleContext(Java20Parser.AssignmentOperatorContext,0)


        def expression(self):
            return self.getTypedRuleContext(Java20Parser.ExpressionContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = Java20Parser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 476, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2899
            self.leftHandSide()
            self.state = 2900
            self.assignmentOperator()
            self.state = 2901
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LeftHandSideContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressionName(self):
            return self.getTypedRuleContext(Java20Parser.ExpressionNameContext,0)


        def fieldAccess(self):
            return self.getTypedRuleContext(Java20Parser.FieldAccessContext,0)


        def arrayAccess(self):
            return self.getTypedRuleContext(Java20Parser.ArrayAccessContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_leftHandSide

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLeftHandSide" ):
                listener.enterLeftHandSide(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLeftHandSide" ):
                listener.exitLeftHandSide(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLeftHandSide" ):
                return visitor.visitLeftHandSide(self)
            else:
                return visitor.visitChildren(self)




    def leftHandSide(self):

        localctx = Java20Parser.LeftHandSideContext(self, self._ctx, self.state)
        self.enterRule(localctx, 478, self.RULE_leftHandSide)
        try:
            self.state = 2906
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,352,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2903
                self.expressionName()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2904
                self.fieldAccess()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2905
                self.arrayAccess()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(Java20Parser.ASSIGN, 0)

        def MUL_ASSIGN(self):
            return self.getToken(Java20Parser.MUL_ASSIGN, 0)

        def DIV_ASSIGN(self):
            return self.getToken(Java20Parser.DIV_ASSIGN, 0)

        def MOD_ASSIGN(self):
            return self.getToken(Java20Parser.MOD_ASSIGN, 0)

        def ADD_ASSIGN(self):
            return self.getToken(Java20Parser.ADD_ASSIGN, 0)

        def SUB_ASSIGN(self):
            return self.getToken(Java20Parser.SUB_ASSIGN, 0)

        def LSHIFT_ASSIGN(self):
            return self.getToken(Java20Parser.LSHIFT_ASSIGN, 0)

        def RSHIFT_ASSIGN(self):
            return self.getToken(Java20Parser.RSHIFT_ASSIGN, 0)

        def URSHIFT_ASSIGN(self):
            return self.getToken(Java20Parser.URSHIFT_ASSIGN, 0)

        def AND_ASSIGN(self):
            return self.getToken(Java20Parser.AND_ASSIGN, 0)

        def XOR_ASSIGN(self):
            return self.getToken(Java20Parser.XOR_ASSIGN, 0)

        def OR_ASSIGN(self):
            return self.getToken(Java20Parser.OR_ASSIGN, 0)

        def getRuleIndex(self):
            return Java20Parser.RULE_assignmentOperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentOperator" ):
                listener.enterAssignmentOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentOperator" ):
                listener.exitAssignmentOperator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentOperator" ):
                return visitor.visitAssignmentOperator(self)
            else:
                return visitor.visitChildren(self)




    def assignmentOperator(self):

        localctx = Java20Parser.AssignmentOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 480, self.RULE_assignmentOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2908
            _la = self._input.LA(1)
            if not(((((_la - 88)) & ~0x3f) == 0 and ((1 << (_la - 88)) & ((1 << (Java20Parser.ASSIGN - 88)) | (1 << (Java20Parser.ADD_ASSIGN - 88)) | (1 << (Java20Parser.SUB_ASSIGN - 88)) | (1 << (Java20Parser.MUL_ASSIGN - 88)) | (1 << (Java20Parser.DIV_ASSIGN - 88)) | (1 << (Java20Parser.AND_ASSIGN - 88)) | (1 << (Java20Parser.OR_ASSIGN - 88)) | (1 << (Java20Parser.XOR_ASSIGN - 88)) | (1 << (Java20Parser.MOD_ASSIGN - 88)) | (1 << (Java20Parser.LSHIFT_ASSIGN - 88)) | (1 << (Java20Parser.RSHIFT_ASSIGN - 88)) | (1 << (Java20Parser.URSHIFT_ASSIGN - 88)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LambdaExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lambdaParameters(self):
            return self.getTypedRuleContext(Java20Parser.LambdaParametersContext,0)


        def ARROW(self):
            return self.getToken(Java20Parser.ARROW, 0)

        def lambdaBody(self):
            return self.getTypedRuleContext(Java20Parser.LambdaBodyContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_lambdaExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLambdaExpression" ):
                listener.enterLambdaExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLambdaExpression" ):
                listener.exitLambdaExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLambdaExpression" ):
                return visitor.visitLambdaExpression(self)
            else:
                return visitor.visitChildren(self)




    def lambdaExpression(self):

        localctx = Java20Parser.LambdaExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 482, self.RULE_lambdaExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2910
            self.lambdaParameters()
            self.state = 2911
            self.match(Java20Parser.ARROW)
            self.state = 2912
            self.lambdaBody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LambdaParametersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(Java20Parser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(Java20Parser.RPAREN, 0)

        def lambdaParameterList(self):
            return self.getTypedRuleContext(Java20Parser.LambdaParameterListContext,0)


        def identifier(self):
            return self.getTypedRuleContext(Java20Parser.IdentifierContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_lambdaParameters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLambdaParameters" ):
                listener.enterLambdaParameters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLambdaParameters" ):
                listener.exitLambdaParameters(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLambdaParameters" ):
                return visitor.visitLambdaParameters(self)
            else:
                return visitor.visitChildren(self)




    def lambdaParameters(self):

        localctx = Java20Parser.LambdaParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 484, self.RULE_lambdaParameters)
        self._la = 0 # Token type
        try:
            self.state = 2920
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Java20Parser.LPAREN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2914
                self.match(Java20Parser.LPAREN)
                self.state = 2916
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Java20Parser.EXPORTS) | (1 << Java20Parser.MODULE) | (1 << Java20Parser.NONSEALED) | (1 << Java20Parser.OPEN) | (1 << Java20Parser.OPENS) | (1 << Java20Parser.PERMITS) | (1 << Java20Parser.PROVIDES) | (1 << Java20Parser.RECORD) | (1 << Java20Parser.REQUIRES) | (1 << Java20Parser.SEALED) | (1 << Java20Parser.TO) | (1 << Java20Parser.TRANSITIVE) | (1 << Java20Parser.USES) | (1 << Java20Parser.VAR) | (1 << Java20Parser.WITH) | (1 << Java20Parser.YIELD) | (1 << Java20Parser.BOOLEAN) | (1 << Java20Parser.BYTE) | (1 << Java20Parser.CHAR) | (1 << Java20Parser.DOUBLE) | (1 << Java20Parser.FINAL) | (1 << Java20Parser.FLOAT) | (1 << Java20Parser.INT) | (1 << Java20Parser.LONG) | (1 << Java20Parser.SHORT))) != 0) or _la==Java20Parser.AT or _la==Java20Parser.Identifier:
                    self.state = 2915
                    self.lambdaParameterList()


                self.state = 2918
                self.match(Java20Parser.RPAREN)
                pass
            elif token in [Java20Parser.EXPORTS, Java20Parser.MODULE, Java20Parser.NONSEALED, Java20Parser.OPEN, Java20Parser.OPENS, Java20Parser.PERMITS, Java20Parser.PROVIDES, Java20Parser.RECORD, Java20Parser.REQUIRES, Java20Parser.SEALED, Java20Parser.TO, Java20Parser.TRANSITIVE, Java20Parser.USES, Java20Parser.VAR, Java20Parser.WITH, Java20Parser.YIELD, Java20Parser.Identifier]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2919
                self.identifier()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LambdaParameterListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lambdaParameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.LambdaParameterContext)
            else:
                return self.getTypedRuleContext(Java20Parser.LambdaParameterContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(Java20Parser.COMMA)
            else:
                return self.getToken(Java20Parser.COMMA, i)

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.IdentifierContext)
            else:
                return self.getTypedRuleContext(Java20Parser.IdentifierContext,i)


        def getRuleIndex(self):
            return Java20Parser.RULE_lambdaParameterList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLambdaParameterList" ):
                listener.enterLambdaParameterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLambdaParameterList" ):
                listener.exitLambdaParameterList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLambdaParameterList" ):
                return visitor.visitLambdaParameterList(self)
            else:
                return visitor.visitChildren(self)




    def lambdaParameterList(self):

        localctx = Java20Parser.LambdaParameterListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 486, self.RULE_lambdaParameterList)
        self._la = 0 # Token type
        try:
            self.state = 2938
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,357,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2922
                self.lambdaParameter()
                self.state = 2927
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==Java20Parser.COMMA:
                    self.state = 2923
                    self.match(Java20Parser.COMMA)
                    self.state = 2924
                    self.lambdaParameter()
                    self.state = 2929
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2930
                self.identifier()
                self.state = 2935
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==Java20Parser.COMMA:
                    self.state = 2931
                    self.match(Java20Parser.COMMA)
                    self.state = 2932
                    self.identifier()
                    self.state = 2937
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LambdaParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lambdaParameterType(self):
            return self.getTypedRuleContext(Java20Parser.LambdaParameterTypeContext,0)


        def variableDeclaratorId(self):
            return self.getTypedRuleContext(Java20Parser.VariableDeclaratorIdContext,0)


        def variableModifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Java20Parser.VariableModifierContext)
            else:
                return self.getTypedRuleContext(Java20Parser.VariableModifierContext,i)


        def variableArityParameter(self):
            return self.getTypedRuleContext(Java20Parser.VariableArityParameterContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_lambdaParameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLambdaParameter" ):
                listener.enterLambdaParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLambdaParameter" ):
                listener.exitLambdaParameter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLambdaParameter" ):
                return visitor.visitLambdaParameter(self)
            else:
                return visitor.visitChildren(self)




    def lambdaParameter(self):

        localctx = Java20Parser.LambdaParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 488, self.RULE_lambdaParameter)
        self._la = 0 # Token type
        try:
            self.state = 2950
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,359,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2943
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==Java20Parser.FINAL or _la==Java20Parser.AT:
                    self.state = 2940
                    self.variableModifier()
                    self.state = 2945
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 2946
                self.lambdaParameterType()
                self.state = 2947
                self.variableDeclaratorId()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2949
                self.variableArityParameter()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LambdaParameterTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unannType(self):
            return self.getTypedRuleContext(Java20Parser.UnannTypeContext,0)


        def VAR(self):
            return self.getToken(Java20Parser.VAR, 0)

        def getRuleIndex(self):
            return Java20Parser.RULE_lambdaParameterType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLambdaParameterType" ):
                listener.enterLambdaParameterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLambdaParameterType" ):
                listener.exitLambdaParameterType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLambdaParameterType" ):
                return visitor.visitLambdaParameterType(self)
            else:
                return visitor.visitChildren(self)




    def lambdaParameterType(self):

        localctx = Java20Parser.LambdaParameterTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 490, self.RULE_lambdaParameterType)
        try:
            self.state = 2954
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,360,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2952
                self.unannType()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2953
                self.match(Java20Parser.VAR)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LambdaBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(Java20Parser.ExpressionContext,0)


        def block(self):
            return self.getTypedRuleContext(Java20Parser.BlockContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_lambdaBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLambdaBody" ):
                listener.enterLambdaBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLambdaBody" ):
                listener.exitLambdaBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLambdaBody" ):
                return visitor.visitLambdaBody(self)
            else:
                return visitor.visitChildren(self)




    def lambdaBody(self):

        localctx = Java20Parser.LambdaBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 492, self.RULE_lambdaBody)
        try:
            self.state = 2958
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Java20Parser.EXPORTS, Java20Parser.MODULE, Java20Parser.NONSEALED, Java20Parser.OPEN, Java20Parser.OPENS, Java20Parser.PERMITS, Java20Parser.PROVIDES, Java20Parser.RECORD, Java20Parser.REQUIRES, Java20Parser.SEALED, Java20Parser.TO, Java20Parser.TRANSITIVE, Java20Parser.USES, Java20Parser.VAR, Java20Parser.WITH, Java20Parser.YIELD, Java20Parser.BOOLEAN, Java20Parser.BYTE, Java20Parser.CHAR, Java20Parser.DOUBLE, Java20Parser.FLOAT, Java20Parser.INT, Java20Parser.LONG, Java20Parser.NEW, Java20Parser.SHORT, Java20Parser.SUPER, Java20Parser.SWITCH, Java20Parser.THIS, Java20Parser.VOID, Java20Parser.IntegerLiteral, Java20Parser.FloatingPointLiteral, Java20Parser.BooleanLiteral, Java20Parser.CharacterLiteral, Java20Parser.StringLiteral, Java20Parser.TextBlock, Java20Parser.NullLiteral, Java20Parser.LPAREN, Java20Parser.AT, Java20Parser.BANG, Java20Parser.TILDE, Java20Parser.INC, Java20Parser.DEC, Java20Parser.ADD, Java20Parser.SUB, Java20Parser.Identifier]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2956
                self.expression()
                pass
            elif token in [Java20Parser.LBRACE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2957
                self.block()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SwitchExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SWITCH(self):
            return self.getToken(Java20Parser.SWITCH, 0)

        def LPAREN(self):
            return self.getToken(Java20Parser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(Java20Parser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(Java20Parser.RPAREN, 0)

        def switchBlock(self):
            return self.getTypedRuleContext(Java20Parser.SwitchBlockContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_switchExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitchExpression" ):
                listener.enterSwitchExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitchExpression" ):
                listener.exitSwitchExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSwitchExpression" ):
                return visitor.visitSwitchExpression(self)
            else:
                return visitor.visitChildren(self)




    def switchExpression(self):

        localctx = Java20Parser.SwitchExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 494, self.RULE_switchExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2960
            self.match(Java20Parser.SWITCH)
            self.state = 2961
            self.match(Java20Parser.LPAREN)
            self.state = 2962
            self.expression()
            self.state = 2963
            self.match(Java20Parser.RPAREN)
            self.state = 2964
            self.switchBlock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstantExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(Java20Parser.ExpressionContext,0)


        def getRuleIndex(self):
            return Java20Parser.RULE_constantExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstantExpression" ):
                listener.enterConstantExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstantExpression" ):
                listener.exitConstantExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstantExpression" ):
                return visitor.visitConstantExpression(self)
            else:
                return visitor.visitChildren(self)




    def constantExpression(self):

        localctx = Java20Parser.ConstantExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 496, self.RULE_constantExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2966
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[226] = self.multiplicativeExpression_sempred
        self._predicates[227] = self.additiveExpression_sempred
        self._predicates[228] = self.shiftExpression_sempred
        self._predicates[229] = self.relationalExpression_sempred
        self._predicates[230] = self.equalityExpression_sempred
        self._predicates[231] = self.andExpression_sempred
        self._predicates[232] = self.exclusiveOrExpression_sempred
        self._predicates[233] = self.inclusiveOrExpression_sempred
        self._predicates[234] = self.conditionalAndExpression_sempred
        self._predicates[235] = self.conditionalOrExpression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def multiplicativeExpression_sempred(self, localctx:MultiplicativeExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 1)
         

    def additiveExpression_sempred(self, localctx:AdditiveExpressionContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 1)
         

    def shiftExpression_sempred(self, localctx:ShiftExpressionContext, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 1)
         

    def relationalExpression_sempred(self, localctx:RelationalExpressionContext, predIndex:int):
            if predIndex == 8:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 12:
                return self.precpred(self._ctx, 1)
         

    def equalityExpression_sempred(self, localctx:EqualityExpressionContext, predIndex:int):
            if predIndex == 13:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 14:
                return self.precpred(self._ctx, 1)
         

    def andExpression_sempred(self, localctx:AndExpressionContext, predIndex:int):
            if predIndex == 15:
                return self.precpred(self._ctx, 1)
         

    def exclusiveOrExpression_sempred(self, localctx:ExclusiveOrExpressionContext, predIndex:int):
            if predIndex == 16:
                return self.precpred(self._ctx, 1)
         

    def inclusiveOrExpression_sempred(self, localctx:InclusiveOrExpressionContext, predIndex:int):
            if predIndex == 17:
                return self.precpred(self._ctx, 1)
         

    def conditionalAndExpression_sempred(self, localctx:ConditionalAndExpressionContext, predIndex:int):
            if predIndex == 18:
                return self.precpred(self._ctx, 1)
         

    def conditionalOrExpression_sempred(self, localctx:ConditionalOrExpressionContext, predIndex:int):
            if predIndex == 19:
                return self.precpred(self._ctx, 1)
         




