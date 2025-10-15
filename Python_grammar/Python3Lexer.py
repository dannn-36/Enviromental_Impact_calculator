# Generated from Python3Lexer.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


if __name__ is not None and "." in __name__:
    from .Python3LexerBase import Python3LexerBase
else:
    from Python3LexerBase import Python3LexerBase


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2h")
        buf.write("\u0390\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\t")
        buf.write("U\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\4]\t]\4")
        buf.write("^\t^\4_\t_\4`\t`\4a\ta\4b\tb\4c\tc\4d\td\4e\te\4f\tf\4")
        buf.write("g\tg\4h\th\4i\ti\4j\tj\4k\tk\4l\tl\4m\tm\4n\tn\4o\to\4")
        buf.write("p\tp\4q\tq\4r\tr\4s\ts\4t\tt\4u\tu\4v\tv\4w\tw\4x\tx\4")
        buf.write("y\ty\4z\tz\4{\t{\4|\t|\4}\t}\4~\t~\4\177\t\177\4\u0080")
        buf.write("\t\u0080\4\u0081\t\u0081\4\u0082\t\u0082\3\2\3\2\5\2\u0108")
        buf.write("\n\2\3\3\3\3\3\3\5\3\u010d\n\3\3\4\3\4\3\4\3\4\5\4\u0113")
        buf.write("\n\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\20\3\20\3")
        buf.write("\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\32\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3 \3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#")
        buf.write("\3#\3#\3$\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3&\3&\3&\3")
        buf.write("&\3\'\3\'\3(\3(\3(\3(\3(\3(\3)\3)\3)\3)\3)\3*\3*\3*\3")
        buf.write("*\3*\3*\3+\3+\3+\5+\u01e3\n+\3+\3+\5+\u01e7\n+\3+\5+\u01ea")
        buf.write("\n+\5+\u01ec\n+\3+\3+\3,\3,\7,\u01f2\n,\f,\16,\u01f5\13")
        buf.write(",\3-\3-\3-\3-\3-\5-\u01fc\n-\3-\3-\5-\u0200\n-\3.\3.\3")
        buf.write(".\3.\3.\5.\u0207\n.\3.\3.\5.\u020b\n.\3/\3/\7/\u020f\n")
        buf.write("/\f/\16/\u0212\13/\3/\6/\u0215\n/\r/\16/\u0216\5/\u0219")
        buf.write("\n/\3\60\3\60\3\60\6\60\u021e\n\60\r\60\16\60\u021f\3")
        buf.write("\61\3\61\3\61\6\61\u0225\n\61\r\61\16\61\u0226\3\62\3")
        buf.write("\62\3\62\6\62\u022c\n\62\r\62\16\62\u022d\3\63\3\63\5")
        buf.write("\63\u0232\n\63\3\64\3\64\5\64\u0236\n\64\3\64\3\64\3\65")
        buf.write("\3\65\3\66\3\66\3\66\3\66\3\67\3\67\38\38\38\39\39\39")
        buf.write("\3:\3:\3;\3;\3<\3<\3=\3=\3=\3>\3>\3?\3?\3?\3@\3@\3@\3")
        buf.write("A\3A\3B\3B\3C\3C\3D\3D\3D\3E\3E\3E\3F\3F\3G\3G\3H\3H\3")
        buf.write("I\3I\3J\3J\3J\3K\3K\3L\3L\3L\3M\3M\3M\3N\3N\3O\3O\3P\3")
        buf.write("P\3P\3Q\3Q\3Q\3R\3R\3R\3S\3S\3S\3T\3T\3T\3U\3U\3V\3V\3")
        buf.write("V\3W\3W\3W\3X\3X\3X\3Y\3Y\3Y\3Z\3Z\3Z\3[\3[\3[\3\\\3\\")
        buf.write("\3\\\3]\3]\3]\3^\3^\3^\3_\3_\3_\3`\3`\3`\3`\3a\3a\3a\3")
        buf.write("a\3b\3b\3b\3b\3c\3c\3c\3c\3d\3d\3d\5d\u02be\nd\3d\3d\3")
        buf.write("e\3e\3f\3f\3f\7f\u02c7\nf\ff\16f\u02ca\13f\3f\3f\3f\3")
        buf.write("f\7f\u02d0\nf\ff\16f\u02d3\13f\3f\5f\u02d6\nf\3g\3g\3")
        buf.write("g\3g\3g\7g\u02dd\ng\fg\16g\u02e0\13g\3g\3g\3g\3g\3g\3")
        buf.write("g\3g\3g\7g\u02ea\ng\fg\16g\u02ed\13g\3g\3g\3g\5g\u02f2")
        buf.write("\ng\3h\3h\5h\u02f6\nh\3i\3i\3j\3j\3j\3j\5j\u02fe\nj\3")
        buf.write("k\3k\3l\3l\3m\3m\3n\3n\3o\3o\3p\5p\u030b\np\3p\3p\3p\3")
        buf.write("p\5p\u0311\np\3q\3q\5q\u0315\nq\3q\3q\3r\6r\u031a\nr\r")
        buf.write("r\16r\u031b\3s\3s\6s\u0320\ns\rs\16s\u0321\3t\3t\5t\u0326")
        buf.write("\nt\3t\6t\u0329\nt\rt\16t\u032a\3u\3u\3u\7u\u0330\nu\f")
        buf.write("u\16u\u0333\13u\3u\3u\3u\3u\7u\u0339\nu\fu\16u\u033c\13")
        buf.write("u\3u\5u\u033f\nu\3v\3v\3v\3v\3v\7v\u0346\nv\fv\16v\u0349")
        buf.write("\13v\3v\3v\3v\3v\3v\3v\3v\3v\7v\u0353\nv\fv\16v\u0356")
        buf.write("\13v\3v\3v\3v\5v\u035b\nv\3w\3w\5w\u035f\nw\3x\5x\u0362")
        buf.write("\nx\3y\5y\u0365\ny\3z\5z\u0368\nz\3{\3{\3{\3|\6|\u036e")
        buf.write("\n|\r|\16|\u036f\3}\3}\7}\u0374\n}\f}\16}\u0377\13}\3")
        buf.write("~\3~\5~\u037b\n~\3~\5~\u037e\n~\3~\3~\5~\u0382\n~\3\177")
        buf.write("\3\177\3\u0080\3\u0080\3\u0081\3\u0081\5\u0081\u038a\n")
        buf.write("\u0081\3\u0082\3\u0082\3\u0082\5\u0082\u038f\n\u0082\6")
        buf.write("\u02de\u02eb\u0347\u0354\2\u0083\3\5\5\6\7\7\t\b\13\t")
        buf.write("\r\n\17\13\21\f\23\r\25\16\27\17\31\20\33\21\35\22\37")
        buf.write("\23!\24#\25%\26\'\27)\30+\31-\32/\33\61\34\63\35\65\36")
        buf.write("\67\379 ;!=\"?#A$C%E&G\'I(K)M*O+Q,S-U.W/Y\60[\61]\62_")
        buf.write("\63a\64c\65e\66g\67i8k9m:o;q<s=u>w?y@{A}B\177C\u0081D")
        buf.write("\u0083E\u0085F\u0087G\u0089H\u008bI\u008dJ\u008fK\u0091")
        buf.write("L\u0093M\u0095N\u0097O\u0099P\u009bQ\u009dR\u009fS\u00a1")
        buf.write("T\u00a3U\u00a5V\u00a7W\u00a9X\u00abY\u00adZ\u00af[\u00b1")
        buf.write("\\\u00b3]\u00b5^\u00b7_\u00b9`\u00bba\u00bdb\u00bfc\u00c1")
        buf.write("d\u00c3e\u00c5f\u00c7g\u00c9h\u00cb\2\u00cd\2\u00cf\2")
        buf.write("\u00d1\2\u00d3\2\u00d5\2\u00d7\2\u00d9\2\u00db\2\u00dd")
        buf.write("\2\u00df\2\u00e1\2\u00e3\2\u00e5\2\u00e7\2\u00e9\2\u00eb")
        buf.write("\2\u00ed\2\u00ef\2\u00f1\2\u00f3\2\u00f5\2\u00f7\2\u00f9")
        buf.write("\2\u00fb\2\u00fd\2\u00ff\2\u0101\2\u0103\2\3\2\33\b\2")
        buf.write("HHTTWWhhttww\4\2HHhh\4\2TTtt\4\2DDdd\4\2QQqq\4\2ZZzz\4")
        buf.write("\2LLll\6\2\f\f\16\17))^^\6\2\f\f\16\17$$^^\3\2^^\3\2\63")
        buf.write(";\3\2\62;\3\2\629\5\2\62;CHch\3\2\62\63\4\2GGgg\4\2--")
        buf.write("//\7\2\2\13\r\16\20(*]_\u0081\7\2\2\13\r\16\20#%]_\u0081")
        buf.write("\4\2\2]_\u0081\3\2\2\u0081\4\2\13\13\"\"\4\2\f\f\16\17")
        buf.write("\6\2\u1887\u1888\u211a\u211a\u2130\u2130\u309d\u309e\6")
        buf.write("\2\u00b9\u00b9\u0389\u0389\u136b\u1373\u19dc\u19dc\4\u024f")
        buf.write("\2C\2\\\2a\2a\2c\2|\2\u00ac\2\u00ac\2\u00b7\2\u00b7\2")
        buf.write("\u00bc\2\u00bc\2\u00c2\2\u00d8\2\u00da\2\u00f8\2\u00fa")
        buf.write("\2\u02c3\2\u02c8\2\u02d3\2\u02e2\2\u02e6\2\u02ee\2\u02ee")
        buf.write("\2\u02f0\2\u02f0\2\u0372\2\u0376\2\u0378\2\u0379\2\u037c")
        buf.write("\2\u037f\2\u0381\2\u0381\2\u0388\2\u0388\2\u038a\2\u038c")
        buf.write("\2\u038e\2\u038e\2\u0390\2\u03a3\2\u03a5\2\u03f7\2\u03f9")
        buf.write("\2\u0483\2\u048c\2\u0531\2\u0533\2\u0558\2\u055b\2\u055b")
        buf.write("\2\u0563\2\u0589\2\u05d2\2\u05ec\2\u05f2\2\u05f4\2\u0622")
        buf.write("\2\u064c\2\u0670\2\u0671\2\u0673\2\u06d5\2\u06d7\2\u06d7")
        buf.write("\2\u06e7\2\u06e8\2\u06f0\2\u06f1\2\u06fc\2\u06fe\2\u0701")
        buf.write("\2\u0701\2\u0712\2\u0712\2\u0714\2\u0731\2\u074f\2\u07a7")
        buf.write("\2\u07b3\2\u07b3\2\u07cc\2\u07ec\2\u07f6\2\u07f7\2\u07fc")
        buf.write("\2\u07fc\2\u0802\2\u0817\2\u081c\2\u081c\2\u0826\2\u0826")
        buf.write("\2\u082a\2\u082a\2\u0842\2\u085a\2\u0862\2\u086c\2\u08a2")
        buf.write("\2\u08b6\2\u08b8\2\u08bf\2\u0906\2\u093b\2\u093f\2\u093f")
        buf.write("\2\u0952\2\u0952\2\u095a\2\u0963\2\u0973\2\u0982\2\u0987")
        buf.write("\2\u098e\2\u0991\2\u0992\2\u0995\2\u09aa\2\u09ac\2\u09b2")
        buf.write("\2\u09b4\2\u09b4\2\u09b8\2\u09bb\2\u09bf\2\u09bf\2\u09d0")
        buf.write("\2\u09d0\2\u09de\2\u09df\2\u09e1\2\u09e3\2\u09f2\2\u09f3")
        buf.write("\2\u09fe\2\u09fe\2\u0a07\2\u0a0c\2\u0a11\2\u0a12\2\u0a15")
        buf.write("\2\u0a2a\2\u0a2c\2\u0a32\2\u0a34\2\u0a35\2\u0a37\2\u0a38")
        buf.write("\2\u0a3a\2\u0a3b\2\u0a5b\2\u0a5e\2\u0a60\2\u0a60\2\u0a74")
        buf.write("\2\u0a76\2\u0a87\2\u0a8f\2\u0a91\2\u0a93\2\u0a95\2\u0aaa")
        buf.write("\2\u0aac\2\u0ab2\2\u0ab4\2\u0ab5\2\u0ab7\2\u0abb\2\u0abf")
        buf.write("\2\u0abf\2\u0ad2\2\u0ad2\2\u0ae2\2\u0ae3\2\u0afb\2\u0afb")
        buf.write("\2\u0b07\2\u0b0e\2\u0b11\2\u0b12\2\u0b15\2\u0b2a\2\u0b2c")
        buf.write("\2\u0b32\2\u0b34\2\u0b35\2\u0b37\2\u0b3b\2\u0b3f\2\u0b3f")
        buf.write("\2\u0b5e\2\u0b5f\2\u0b61\2\u0b63\2\u0b73\2\u0b73\2\u0b85")
        buf.write("\2\u0b85\2\u0b87\2\u0b8c\2\u0b90\2\u0b92\2\u0b94\2\u0b97")
        buf.write("\2\u0b9b\2\u0b9c\2\u0b9e\2\u0b9e\2\u0ba0\2\u0ba1\2\u0ba5")
        buf.write("\2\u0ba6\2\u0baa\2\u0bac\2\u0bb0\2\u0bbb\2\u0bd2\2\u0bd2")
        buf.write("\2\u0c07\2\u0c0e\2\u0c10\2\u0c12\2\u0c14\2\u0c2a\2\u0c2c")
        buf.write("\2\u0c3b\2\u0c3f\2\u0c3f\2\u0c5a\2\u0c5c\2\u0c62\2\u0c63")
        buf.write("\2\u0c82\2\u0c82\2\u0c87\2\u0c8e\2\u0c90\2\u0c92\2\u0c94")
        buf.write("\2\u0caa\2\u0cac\2\u0cb5\2\u0cb7\2\u0cbb\2\u0cbf\2\u0cbf")
        buf.write("\2\u0ce0\2\u0ce0\2\u0ce2\2\u0ce3\2\u0cf3\2\u0cf4\2\u0d07")
        buf.write("\2\u0d0e\2\u0d10\2\u0d12\2\u0d14\2\u0d3c\2\u0d3f\2\u0d3f")
        buf.write("\2\u0d50\2\u0d50\2\u0d56\2\u0d58\2\u0d61\2\u0d63\2\u0d7c")
        buf.write("\2\u0d81\2\u0d87\2\u0d98\2\u0d9c\2\u0db3\2\u0db5\2\u0dbd")
        buf.write("\2\u0dbf\2\u0dbf\2\u0dc2\2\u0dc8\2\u0e03\2\u0e32\2\u0e34")
        buf.write("\2\u0e35\2\u0e42\2\u0e48\2\u0e83\2\u0e84\2\u0e86\2\u0e86")
        buf.write("\2\u0e89\2\u0e8a\2\u0e8c\2\u0e8c\2\u0e8f\2\u0e8f\2\u0e96")
        buf.write("\2\u0e99\2\u0e9b\2\u0ea1\2\u0ea3\2\u0ea5\2\u0ea7\2\u0ea7")
        buf.write("\2\u0ea9\2\u0ea9\2\u0eac\2\u0ead\2\u0eaf\2\u0eb2\2\u0eb4")
        buf.write("\2\u0eb5\2\u0ebf\2\u0ebf\2\u0ec2\2\u0ec6\2\u0ec8\2\u0ec8")
        buf.write("\2\u0ede\2\u0ee1\2\u0f02\2\u0f02\2\u0f42\2\u0f49\2\u0f4b")
        buf.write("\2\u0f6e\2\u0f8a\2\u0f8e\2\u1002\2\u102c\2\u1041\2\u1041")
        buf.write("\2\u1052\2\u1057\2\u105c\2\u105f\2\u1063\2\u1063\2\u1067")
        buf.write("\2\u1068\2\u1070\2\u1072\2\u1077\2\u1083\2\u1090\2\u1090")
        buf.write("\2\u10a2\2\u10c7\2\u10c9\2\u10c9\2\u10cf\2\u10cf\2\u10d2")
        buf.write("\2\u10fc\2\u10fe\2\u124a\2\u124c\2\u124f\2\u1252\2\u1258")
        buf.write("\2\u125a\2\u125a\2\u125c\2\u125f\2\u1262\2\u128a\2\u128c")
        buf.write("\2\u128f\2\u1292\2\u12b2\2\u12b4\2\u12b7\2\u12ba\2\u12c0")
        buf.write("\2\u12c2\2\u12c2\2\u12c4\2\u12c7\2\u12ca\2\u12d8\2\u12da")
        buf.write("\2\u1312\2\u1314\2\u1317\2\u131a\2\u135c\2\u1382\2\u1391")
        buf.write("\2\u13a2\2\u13f7\2\u13fa\2\u13ff\2\u1403\2\u166e\2\u1671")
        buf.write("\2\u1681\2\u1683\2\u169c\2\u16a2\2\u16ec\2\u16f0\2\u16fa")
        buf.write("\2\u1702\2\u170e\2\u1710\2\u1713\2\u1722\2\u1733\2\u1742")
        buf.write("\2\u1753\2\u1762\2\u176e\2\u1770\2\u1772\2\u1782\2\u17b5")
        buf.write("\2\u17d9\2\u17d9\2\u17de\2\u17de\2\u1822\2\u1879\2\u1882")
        buf.write("\2\u1886\2\u1889\2\u18aa\2\u18ac\2\u18ac\2\u18b2\2\u18f7")
        buf.write("\2\u1902\2\u1920\2\u1952\2\u196f\2\u1972\2\u1976\2\u1982")
        buf.write("\2\u19ad\2\u19b2\2\u19cb\2\u1a02\2\u1a18\2\u1a22\2\u1a56")
        buf.write("\2\u1aa9\2\u1aa9\2\u1b07\2\u1b35\2\u1b47\2\u1b4d\2\u1b85")
        buf.write("\2\u1ba2\2\u1bb0\2\u1bb1\2\u1bbc\2\u1be7\2\u1c02\2\u1c25")
        buf.write("\2\u1c4f\2\u1c51\2\u1c5c\2\u1c7f\2\u1c82\2\u1c8a\2\u1ceb")
        buf.write("\2\u1cee\2\u1cf0\2\u1cf3\2\u1cf7\2\u1cf8\2\u1d02\2\u1dc1")
        buf.write("\2\u1e02\2\u1f17\2\u1f1a\2\u1f1f\2\u1f22\2\u1f47\2\u1f4a")
        buf.write("\2\u1f4f\2\u1f52\2\u1f59\2\u1f5b\2\u1f5b\2\u1f5d\2\u1f5d")
        buf.write("\2\u1f5f\2\u1f5f\2\u1f61\2\u1f7f\2\u1f82\2\u1fb6\2\u1fb8")
        buf.write("\2\u1fbe\2\u1fc0\2\u1fc0\2\u1fc4\2\u1fc6\2\u1fc8\2\u1fce")
        buf.write("\2\u1fd2\2\u1fd5\2\u1fd8\2\u1fdd\2\u1fe2\2\u1fee\2\u1ff4")
        buf.write("\2\u1ff6\2\u1ff8\2\u1ffe\2\u2073\2\u2073\2\u2081\2\u2081")
        buf.write("\2\u2092\2\u209e\2\u2104\2\u2104\2\u2109\2\u2109\2\u210c")
        buf.write("\2\u2115\2\u2117\2\u2117\2\u211b\2\u211f\2\u2126\2\u2126")
        buf.write("\2\u2128\2\u2128\2\u212a\2\u212a\2\u212c\2\u212f\2\u2131")
        buf.write("\2\u213b\2\u213e\2\u2141\2\u2147\2\u214b\2\u2150\2\u2150")
        buf.write("\2\u2162\2\u218a\2\u2c02\2\u2c30\2\u2c32\2\u2c60\2\u2c62")
        buf.write("\2\u2ce6\2\u2ced\2\u2cf0\2\u2cf4\2\u2cf5\2\u2d02\2\u2d27")
        buf.write("\2\u2d29\2\u2d29\2\u2d2f\2\u2d2f\2\u2d32\2\u2d69\2\u2d71")
        buf.write("\2\u2d71\2\u2d82\2\u2d98\2\u2da2\2\u2da8\2\u2daa\2\u2db0")
        buf.write("\2\u2db2\2\u2db8\2\u2dba\2\u2dc0\2\u2dc2\2\u2dc8\2\u2dca")
        buf.write("\2\u2dd0\2\u2dd2\2\u2dd8\2\u2dda\2\u2de0\2\u2e31\2\u2e31")
        buf.write("\2\u3007\2\u3009\2\u3023\2\u302b\2\u3033\2\u3037\2\u303a")
        buf.write("\2\u303e\2\u3043\2\u3098\2\u309f\2\u30a1\2\u30a3\2\u30fc")
        buf.write("\2\u30fe\2\u3101\2\u3107\2\u3130\2\u3133\2\u3190\2\u31a2")
        buf.write("\2\u31bc\2\u31f2\2\u3201\2\u3402\2\u4db7\2\u4e02\2\u9fec")
        buf.write("\2\ua002\2\ua48e\2\ua4d2\2\ua4ff\2\ua502\2\ua60e\2\ua612")
        buf.write("\2\ua621\2\ua62c\2\ua62d\2\ua642\2\ua670\2\ua681\2\ua69f")
        buf.write("\2\ua6a2\2\ua6f1\2\ua719\2\ua721\2\ua724\2\ua78a\2\ua78d")
        buf.write("\2\ua7b0\2\ua7b2\2\ua7b9\2\ua7f9\2\ua803\2\ua805\2\ua807")
        buf.write("\2\ua809\2\ua80c\2\ua80e\2\ua824\2\ua842\2\ua875\2\ua884")
        buf.write("\2\ua8b5\2\ua8f4\2\ua8f9\2\ua8fd\2\ua8fd\2\ua8ff\2\ua8ff")
        buf.write("\2\ua90c\2\ua927\2\ua932\2\ua948\2\ua962\2\ua97e\2\ua986")
        buf.write("\2\ua9b4\2\ua9d1\2\ua9d1\2\ua9e2\2\ua9e6\2\ua9e8\2\ua9f1")
        buf.write("\2\ua9fc\2\uaa00\2\uaa02\2\uaa2a\2\uaa42\2\uaa44\2\uaa46")
        buf.write("\2\uaa4d\2\uaa62\2\uaa78\2\uaa7c\2\uaa7c\2\uaa80\2\uaab1")
        buf.write("\2\uaab3\2\uaab3\2\uaab7\2\uaab8\2\uaabb\2\uaabf\2\uaac2")
        buf.write("\2\uaac2\2\uaac4\2\uaac4\2\uaadd\2\uaadf\2\uaae2\2\uaaec")
        buf.write("\2\uaaf4\2\uaaf6\2\uab03\2\uab08\2\uab0b\2\uab10\2\uab13")
        buf.write("\2\uab18\2\uab22\2\uab28\2\uab2a\2\uab30\2\uab32\2\uab5c")
        buf.write("\2\uab5e\2\uab67\2\uab72\2\uabe4\2\uac02\2\ud7a5\2\ud7b2")
        buf.write("\2\ud7c8\2\ud7cd\2\ud7fd\2\uf902\2\ufa6f\2\ufa72\2\ufadb")
        buf.write("\2\ufb02\2\ufb08\2\ufb15\2\ufb19\2\ufb1f\2\ufb1f\2\ufb21")
        buf.write("\2\ufb2a\2\ufb2c\2\ufb38\2\ufb3a\2\ufb3e\2\ufb40\2\ufb40")
        buf.write("\2\ufb42\2\ufb43\2\ufb45\2\ufb46\2\ufb48\2\ufbb3\2\ufbd5")
        buf.write("\2\ufd3f\2\ufd52\2\ufd91\2\ufd94\2\ufdc9\2\ufdf2\2\ufdfd")
        buf.write("\2\ufe72\2\ufe76\2\ufe78\2\ufefe\2\uff23\2\uff3c\2\uff43")
        buf.write("\2\uff5c\2\uff68\2\uffc0\2\uffc4\2\uffc9\2\uffcc\2\uffd1")
        buf.write("\2\uffd4\2\uffd9\2\uffdc\2\uffde\2\2\3\r\3\17\3(\3*\3")
        buf.write("<\3>\3?\3A\3O\3R\3_\3\u0082\3\u00fc\3\u0142\3\u0176\3")
        buf.write("\u0282\3\u029e\3\u02a2\3\u02d2\3\u0302\3\u0321\3\u032f")
        buf.write("\3\u034c\3\u0352\3\u0377\3\u0382\3\u039f\3\u03a2\3\u03c5")
        buf.write("\3\u03ca\3\u03d1\3\u03d3\3\u03d7\3\u0402\3\u049f\3\u04b2")
        buf.write("\3\u04d5\3\u04da\3\u04fd\3\u0502\3\u0529\3\u0532\3\u0565")
        buf.write("\3\u0602\3\u0738\3\u0742\3\u0757\3\u0762\3\u0769\3\u0802")
        buf.write("\3\u0807\3\u080a\3\u080a\3\u080c\3\u0837\3\u0839\3\u083a")
        buf.write("\3\u083e\3\u083e\3\u0841\3\u0857\3\u0862\3\u0878\3\u0882")
        buf.write("\3\u08a0\3\u08e2\3\u08f4\3\u08f6\3\u08f7\3\u0902\3\u0917")
        buf.write("\3\u0922\3\u093b\3\u0982\3\u09b9\3\u09c0\3\u09c1\3\u0a02")
        buf.write("\3\u0a02\3\u0a12\3\u0a15\3\u0a17\3\u0a19\3\u0a1b\3\u0a35")
        buf.write("\3\u0a62\3\u0a7e\3\u0a82\3\u0a9e\3\u0ac2\3\u0ac9\3\u0acb")
        buf.write("\3\u0ae6\3\u0b02\3\u0b37\3\u0b42\3\u0b57\3\u0b62\3\u0b74")
        buf.write("\3\u0b82\3\u0b93\3\u0c02\3\u0c4a\3\u0c82\3\u0cb4\3\u0cc2")
        buf.write("\3\u0cf4\3\u1005\3\u1039\3\u1085\3\u10b1\3\u10d2\3\u10ea")
        buf.write("\3\u1105\3\u1128\3\u1152\3\u1174\3\u1178\3\u1178\3\u1185")
        buf.write("\3\u11b4\3\u11c3\3\u11c6\3\u11dc\3\u11dc\3\u11de\3\u11de")
        buf.write("\3\u1202\3\u1213\3\u1215\3\u122d\3\u1282\3\u1288\3\u128a")
        buf.write("\3\u128a\3\u128c\3\u128f\3\u1291\3\u129f\3\u12a1\3\u12aa")
        buf.write("\3\u12b2\3\u12e0\3\u1307\3\u130e\3\u1311\3\u1312\3\u1315")
        buf.write("\3\u132a\3\u132c\3\u1332\3\u1334\3\u1335\3\u1337\3\u133b")
        buf.write("\3\u133f\3\u133f\3\u1352\3\u1352\3\u135f\3\u1363\3\u1402")
        buf.write("\3\u1436\3\u1449\3\u144c\3\u1482\3\u14b1\3\u14c6\3\u14c7")
        buf.write("\3\u14c9\3\u14c9\3\u1582\3\u15b0\3\u15da\3\u15dd\3\u1602")
        buf.write("\3\u1631\3\u1646\3\u1646\3\u1682\3\u16ac\3\u1702\3\u171b")
        buf.write("\3\u18a2\3\u18e1\3\u1901\3\u1901\3\u1a02\3\u1a02\3\u1a0d")
        buf.write("\3\u1a34\3\u1a3c\3\u1a3c\3\u1a52\3\u1a52\3\u1a5e\3\u1a85")
        buf.write("\3\u1a88\3\u1a8b\3\u1ac2\3\u1afa\3\u1c02\3\u1c0a\3\u1c0c")
        buf.write("\3\u1c30\3\u1c42\3\u1c42\3\u1c74\3\u1c91\3\u1d02\3\u1d08")
        buf.write("\3\u1d0a\3\u1d0b\3\u1d0d\3\u1d32\3\u1d48\3\u1d48\3\u2002")
        buf.write("\3\u239b\3\u2402\3\u2470\3\u2482\3\u2545\3\u3002\3\u3430")
        buf.write("\3\u4402\3\u4648\3\u6802\3\u6a3a\3\u6a42\3\u6a60\3\u6ad2")
        buf.write("\3\u6aef\3\u6b02\3\u6b31\3\u6b42\3\u6b45\3\u6b65\3\u6b79")
        buf.write("\3\u6b7f\3\u6b91\3\u6f02\3\u6f46\3\u6f52\3\u6f52\3\u6f95")
        buf.write("\3\u6fa1\3\u6fe2\3\u6fe3\3\u7002\3\u87ee\3\u8802\3\u8af4")
        buf.write("\3\ub002\3\ub120\3\ub172\3\ub2fd\3\ubc02\3\ubc6c\3\ubc72")
        buf.write("\3\ubc7e\3\ubc82\3\ubc8a\3\ubc92\3\ubc9b\3\ud402\3\ud456")
        buf.write("\3\ud458\3\ud49e\3\ud4a0\3\ud4a1\3\ud4a4\3\ud4a4\3\ud4a7")
        buf.write("\3\ud4a8\3\ud4ab\3\ud4ae\3\ud4b0\3\ud4bb\3\ud4bd\3\ud4bd")
        buf.write("\3\ud4bf\3\ud4c5\3\ud4c7\3\ud507\3\ud509\3\ud50c\3\ud50f")
        buf.write("\3\ud516\3\ud518\3\ud51e\3\ud520\3\ud53b\3\ud53d\3\ud540")
        buf.write("\3\ud542\3\ud546\3\ud548\3\ud548\3\ud54c\3\ud552\3\ud554")
        buf.write("\3\ud6a7\3\ud6aa\3\ud6c2\3\ud6c4\3\ud6dc\3\ud6de\3\ud6fc")
        buf.write("\3\ud6fe\3\ud716\3\ud718\3\ud736\3\ud738\3\ud750\3\ud752")
        buf.write("\3\ud770\3\ud772\3\ud78a\3\ud78c\3\ud7aa\3\ud7ac\3\ud7c4")
        buf.write("\3\ud7c6\3\ud7cd\3\ue802\3\ue8c6\3\ue902\3\ue945\3\uee02")
        buf.write("\3\uee05\3\uee07\3\uee21\3\uee23\3\uee24\3\uee26\3\uee26")
        buf.write("\3\uee29\3\uee29\3\uee2b\3\uee34\3\uee36\3\uee39\3\uee3b")
        buf.write("\3\uee3b\3\uee3d\3\uee3d\3\uee44\3\uee44\3\uee49\3\uee49")
        buf.write("\3\uee4b\3\uee4b\3\uee4d\3\uee4d\3\uee4f\3\uee51\3\uee53")
        buf.write("\3\uee54\3\uee56\3\uee56\3\uee59\3\uee59\3\uee5b\3\uee5b")
        buf.write("\3\uee5d\3\uee5d\3\uee5f\3\uee5f\3\uee61\3\uee61\3\uee63")
        buf.write("\3\uee64\3\uee66\3\uee66\3\uee69\3\uee6c\3\uee6e\3\uee74")
        buf.write("\3\uee76\3\uee79\3\uee7b\3\uee7e\3\uee80\3\uee80\3\uee82")
        buf.write("\3\uee8b\3\uee8d\3\uee9d\3\ueea3\3\ueea5\3\ueea7\3\ueeab")
        buf.write("\3\ueead\3\ueebd\3\2\4\ua6d8\4\ua702\4\ub736\4\ub742\4")
        buf.write("\ub81f\4\ub822\4\ucea3\4\uceb2\4\uebe2\4\uf802\4\ufa1f")
        buf.write("\4\u0143\2\62\2;\2a\2a\2\u0302\2\u0371\2\u0485\2\u0489")
        buf.write("\2\u0593\2\u05bf\2\u05c1\2\u05c1\2\u05c3\2\u05c4\2\u05c6")
        buf.write("\2\u05c7\2\u05c9\2\u05c9\2\u0612\2\u061c\2\u064d\2\u066b")
        buf.write("\2\u0672\2\u0672\2\u06d8\2\u06de\2\u06e1\2\u06e6\2\u06e9")
        buf.write("\2\u06ea\2\u06ec\2\u06ef\2\u06f2\2\u06fb\2\u0713\2\u0713")
        buf.write("\2\u0732\2\u074c\2\u07a8\2\u07b2\2\u07c2\2\u07cb\2\u07ed")
        buf.write("\2\u07f5\2\u0818\2\u081b\2\u081d\2\u0825\2\u0827\2\u0829")
        buf.write("\2\u082b\2\u082f\2\u085b\2\u085d\2\u08d6\2\u08e3\2\u08e5")
        buf.write("\2\u0905\2\u093c\2\u093e\2\u0940\2\u0951\2\u0953\2\u0959")
        buf.write("\2\u0964\2\u0965\2\u0968\2\u0971\2\u0983\2\u0985\2\u09be")
        buf.write("\2\u09be\2\u09c0\2\u09c6\2\u09c9\2\u09ca\2\u09cd\2\u09cf")
        buf.write("\2\u09d9\2\u09d9\2\u09e4\2\u09e5\2\u09e8\2\u09f1\2\u0a03")
        buf.write("\2\u0a05\2\u0a3e\2\u0a3e\2\u0a40\2\u0a44\2\u0a49\2\u0a4a")
        buf.write("\2\u0a4d\2\u0a4f\2\u0a53\2\u0a53\2\u0a68\2\u0a73\2\u0a77")
        buf.write("\2\u0a77\2\u0a83\2\u0a85\2\u0abe\2\u0abe\2\u0ac0\2\u0ac7")
        buf.write("\2\u0ac9\2\u0acb\2\u0acd\2\u0acf\2\u0ae4\2\u0ae5\2\u0ae8")
        buf.write("\2\u0af1\2\u0afc\2\u0b01\2\u0b03\2\u0b05\2\u0b3e\2\u0b3e")
        buf.write("\2\u0b40\2\u0b46\2\u0b49\2\u0b4a\2\u0b4d\2\u0b4f\2\u0b58")
        buf.write("\2\u0b59\2\u0b64\2\u0b65\2\u0b68\2\u0b71\2\u0b84\2\u0b84")
        buf.write("\2\u0bc0\2\u0bc4\2\u0bc8\2\u0bca\2\u0bcc\2\u0bcf\2\u0bd9")
        buf.write("\2\u0bd9\2\u0be8\2\u0bf1\2\u0c02\2\u0c05\2\u0c40\2\u0c46")
        buf.write("\2\u0c48\2\u0c4a\2\u0c4c\2\u0c4f\2\u0c57\2\u0c58\2\u0c64")
        buf.write("\2\u0c65\2\u0c68\2\u0c71\2\u0c83\2\u0c85\2\u0cbe\2\u0cbe")
        buf.write("\2\u0cc0\2\u0cc6\2\u0cc8\2\u0cca\2\u0ccc\2\u0ccf\2\u0cd7")
        buf.write("\2\u0cd8\2\u0ce4\2\u0ce5\2\u0ce8\2\u0cf1\2\u0d02\2\u0d05")
        buf.write("\2\u0d3d\2\u0d3e\2\u0d40\2\u0d46\2\u0d48\2\u0d4a\2\u0d4c")
        buf.write("\2\u0d4f\2\u0d59\2\u0d59\2\u0d64\2\u0d65\2\u0d68\2\u0d71")
        buf.write("\2\u0d84\2\u0d85\2\u0dcc\2\u0dcc\2\u0dd1\2\u0dd6\2\u0dd8")
        buf.write("\2\u0dd8\2\u0dda\2\u0de1\2\u0de8\2\u0df1\2\u0df4\2\u0df5")
        buf.write("\2\u0e33\2\u0e33\2\u0e36\2\u0e3c\2\u0e49\2\u0e50\2\u0e52")
        buf.write("\2\u0e5b\2\u0eb3\2\u0eb3\2\u0eb6\2\u0ebb\2\u0ebd\2\u0ebe")
        buf.write("\2\u0eca\2\u0ecf\2\u0ed2\2\u0edb\2\u0f1a\2\u0f1b\2\u0f22")
        buf.write("\2\u0f2b\2\u0f37\2\u0f37\2\u0f39\2\u0f39\2\u0f3b\2\u0f3b")
        buf.write("\2\u0f40\2\u0f41\2\u0f73\2\u0f86\2\u0f88\2\u0f89\2\u0f8f")
        buf.write("\2\u0f99\2\u0f9b\2\u0fbe\2\u0fc8\2\u0fc8\2\u102d\2\u1040")
        buf.write("\2\u1042\2\u104b\2\u1058\2\u105b\2\u1060\2\u1062\2\u1064")
        buf.write("\2\u1066\2\u1069\2\u106f\2\u1073\2\u1076\2\u1084\2\u108f")
        buf.write("\2\u1091\2\u109f\2\u135f\2\u1361\2\u1714\2\u1716\2\u1734")
        buf.write("\2\u1736\2\u1754\2\u1755\2\u1774\2\u1775\2\u17b6\2\u17d5")
        buf.write("\2\u17df\2\u17df\2\u17e2\2\u17eb\2\u180d\2\u180f\2\u1812")
        buf.write("\2\u181b\2\u1887\2\u1888\2\u18ab\2\u18ab\2\u1922\2\u192d")
        buf.write("\2\u1932\2\u193d\2\u1948\2\u1951\2\u19d2\2\u19db\2\u1a19")
        buf.write("\2\u1a1d\2\u1a57\2\u1a60\2\u1a62\2\u1a7e\2\u1a81\2\u1a8b")
        buf.write("\2\u1a92\2\u1a9b\2\u1ab2\2\u1abf\2\u1b02\2\u1b06\2\u1b36")
        buf.write("\2\u1b46\2\u1b52\2\u1b5b\2\u1b6d\2\u1b75\2\u1b82\2\u1b84")
        buf.write("\2\u1ba3\2\u1baf\2\u1bb2\2\u1bbb\2\u1be8\2\u1bf5\2\u1c26")
        buf.write("\2\u1c39\2\u1c42\2\u1c4b\2\u1c52\2\u1c5b\2\u1cd2\2\u1cd4")
        buf.write("\2\u1cd6\2\u1cea\2\u1cef\2\u1cef\2\u1cf4\2\u1cf6\2\u1cf9")
        buf.write("\2\u1cfb\2\u1dc2\2\u1dfb\2\u1dfd\2\u1e01\2\u2041\2\u2042")
        buf.write("\2\u2056\2\u2056\2\u20d2\2\u20de\2\u20e3\2\u20e3\2\u20e7")
        buf.write("\2\u20f2\2\u2cf1\2\u2cf3\2\u2d81\2\u2d81\2\u2de2\2\u2e01")
        buf.write("\2\u302c\2\u3031\2\u309b\2\u309c\2\ua622\2\ua62b\2\ua671")
        buf.write("\2\ua671\2\ua676\2\ua67f\2\ua6a0\2\ua6a1\2\ua6f2\2\ua6f3")
        buf.write("\2\ua804\2\ua804\2\ua808\2\ua808\2\ua80d\2\ua80d\2\ua825")
        buf.write("\2\ua829\2\ua882\2\ua883\2\ua8b6\2\ua8c7\2\ua8d2\2\ua8db")
        buf.write("\2\ua8e2\2\ua8f3\2\ua902\2\ua90b\2\ua928\2\ua92f\2\ua949")
        buf.write("\2\ua955\2\ua982\2\ua985\2\ua9b5\2\ua9c2\2\ua9d2\2\ua9db")
        buf.write("\2\ua9e7\2\ua9e7\2\ua9f2\2\ua9fb\2\uaa2b\2\uaa38\2\uaa45")
        buf.write("\2\uaa45\2\uaa4e\2\uaa4f\2\uaa52\2\uaa5b\2\uaa7d\2\uaa7f")
        buf.write("\2\uaab2\2\uaab2\2\uaab4\2\uaab6\2\uaab9\2\uaaba\2\uaac0")
        buf.write("\2\uaac1\2\uaac3\2\uaac3\2\uaaed\2\uaaf1\2\uaaf7\2\uaaf8")
        buf.write("\2\uabe5\2\uabec\2\uabee\2\uabef\2\uabf2\2\uabfb\2\ufb20")
        buf.write("\2\ufb20\2\ufe02\2\ufe11\2\ufe22\2\ufe31\2\ufe35\2\ufe36")
        buf.write("\2\ufe4f\2\ufe51\2\uff12\2\uff1b\2\uff41\2\uff41\2\u01ff")
        buf.write("\3\u01ff\3\u02e2\3\u02e2\3\u0378\3\u037c\3\u04a2\3\u04ab")
        buf.write("\3\u0a03\3\u0a05\3\u0a07\3\u0a08\3\u0a0e\3\u0a11\3\u0a3a")
        buf.write("\3\u0a3c\3\u0a41\3\u0a41\3\u0ae7\3\u0ae8\3\u1002\3\u1004")
        buf.write("\3\u103a\3\u1048\3\u1068\3\u1071\3\u1081\3\u1084\3\u10b2")
        buf.write("\3\u10bc\3\u10f2\3\u10fb\3\u1102\3\u1104\3\u1129\3\u1136")
        buf.write("\3\u1138\3\u1141\3\u1175\3\u1175\3\u1182\3\u1184\3\u11b5")
        buf.write("\3\u11c2\3\u11cc\3\u11ce\3\u11d2\3\u11db\3\u122e\3\u1239")
        buf.write("\3\u1240\3\u1240\3\u12e1\3\u12ec\3\u12f2\3\u12fb\3\u1302")
        buf.write("\3\u1305\3\u133e\3\u133e\3\u1340\3\u1346\3\u1349\3\u134a")
        buf.write("\3\u134d\3\u134f\3\u1359\3\u1359\3\u1364\3\u1365\3\u1368")
        buf.write("\3\u136e\3\u1372\3\u1376\3\u1437\3\u1448\3\u1452\3\u145b")
        buf.write("\3\u14b2\3\u14c5\3\u14d2\3\u14db\3\u15b1\3\u15b7\3\u15ba")
        buf.write("\3\u15c2\3\u15de\3\u15df\3\u1632\3\u1642\3\u1652\3\u165b")
        buf.write("\3\u16ad\3\u16b9\3\u16c2\3\u16cb\3\u171f\3\u172d\3\u1732")
        buf.write("\3\u173b\3\u18e2\3\u18eb\3\u1a03\3\u1a0c\3\u1a35\3\u1a3b")
        buf.write("\3\u1a3d\3\u1a40\3\u1a49\3\u1a49\3\u1a53\3\u1a5d\3\u1a8c")
        buf.write("\3\u1a9b\3\u1c31\3\u1c38\3\u1c3a\3\u1c41\3\u1c52\3\u1c5b")
        buf.write("\3\u1c94\3\u1ca9\3\u1cab\3\u1cb8\3\u1d33\3\u1d38\3\u1d3c")
        buf.write("\3\u1d3c\3\u1d3e\3\u1d3f\3\u1d41\3\u1d47\3\u1d49\3\u1d49")
        buf.write("\3\u1d52\3\u1d5b\3\u6a62\3\u6a6b\3\u6af2\3\u6af6\3\u6b32")
        buf.write("\3\u6b38\3\u6b52\3\u6b5b\3\u6f53\3\u6f80\3\u6f91\3\u6f94")
        buf.write("\3\ubc9f\3\ubca0\3\ud167\3\ud16b\3\ud16f\3\ud174\3\ud17d")
        buf.write("\3\ud184\3\ud187\3\ud18d\3\ud1ac\3\ud1af\3\ud244\3\ud246")
        buf.write("\3\ud7d0\3\ud801\3\uda02\3\uda38\3\uda3d\3\uda6e\3\uda77")
        buf.write("\3\uda77\3\uda86\3\uda86\3\uda9d\3\udaa1\3\udaa3\3\udab1")
        buf.write("\3\ue002\3\ue008\3\ue00a\3\ue01a\3\ue01d\3\ue023\3\ue025")
        buf.write("\3\ue026\3\ue028\3\ue02c\3\ue8d2\3\ue8d8\3\ue946\3\ue94c")
        buf.write("\3\ue952\3\ue95b\3\u0102\20\u01f1\20\u03b0\2\3\3\2\2\2")
        buf.write("\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r")
        buf.write("\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3")
        buf.write("\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2")
        buf.write("\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'")
        buf.write("\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2")
        buf.write("\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29")
        buf.write("\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2")
        buf.write("C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2")
        buf.write("\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2")
        buf.write("\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2")
        buf.write("\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3")
        buf.write("\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s")
        buf.write("\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2")
        buf.write("}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2")
        buf.write("\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b")
        buf.write("\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2")
        buf.write("\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\2\u0099")
        buf.write("\3\2\2\2\2\u009b\3\2\2\2\2\u009d\3\2\2\2\2\u009f\3\2\2")
        buf.write("\2\2\u00a1\3\2\2\2\2\u00a3\3\2\2\2\2\u00a5\3\2\2\2\2\u00a7")
        buf.write("\3\2\2\2\2\u00a9\3\2\2\2\2\u00ab\3\2\2\2\2\u00ad\3\2\2")
        buf.write("\2\2\u00af\3\2\2\2\2\u00b1\3\2\2\2\2\u00b3\3\2\2\2\2\u00b5")
        buf.write("\3\2\2\2\2\u00b7\3\2\2\2\2\u00b9\3\2\2\2\2\u00bb\3\2\2")
        buf.write("\2\2\u00bd\3\2\2\2\2\u00bf\3\2\2\2\2\u00c1\3\2\2\2\2\u00c3")
        buf.write("\3\2\2\2\2\u00c5\3\2\2\2\2\u00c7\3\2\2\2\2\u00c9\3\2\2")
        buf.write("\2\3\u0107\3\2\2\2\5\u010c\3\2\2\2\7\u0112\3\2\2\2\t\u0114")
        buf.write("\3\2\2\2\13\u0118\3\2\2\2\r\u011b\3\2\2\2\17\u0122\3\2")
        buf.write("\2\2\21\u0128\3\2\2\2\23\u012e\3\2\2\2\25\u0134\3\2\2")
        buf.write("\2\27\u0139\3\2\2\2\31\u013f\3\2\2\2\33\u0148\3\2\2\2")
        buf.write("\35\u014c\3\2\2\2\37\u0150\3\2\2\2!\u0155\3\2\2\2#\u015a")
        buf.write("\3\2\2\2%\u0161\3\2\2\2\'\u0167\3\2\2\2)\u016f\3\2\2\2")
        buf.write("+\u0173\3\2\2\2-\u0178\3\2\2\2/\u017f\3\2\2\2\61\u0182")
        buf.write("\3\2\2\2\63\u0189\3\2\2\2\65\u018c\3\2\2\2\67\u018f\3")
        buf.write("\2\2\29\u0196\3\2\2\2;\u019c\3\2\2\2=\u01a1\3\2\2\2?\u01aa")
        buf.write("\3\2\2\2A\u01ae\3\2\2\2C\u01b1\3\2\2\2E\u01b6\3\2\2\2")
        buf.write("G\u01bc\3\2\2\2I\u01c3\3\2\2\2K\u01c8\3\2\2\2M\u01cc\3")
        buf.write("\2\2\2O\u01ce\3\2\2\2Q\u01d4\3\2\2\2S\u01d9\3\2\2\2U\u01eb")
        buf.write("\3\2\2\2W\u01ef\3\2\2\2Y\u01fb\3\2\2\2[\u0206\3\2\2\2")
        buf.write("]\u0218\3\2\2\2_\u021a\3\2\2\2a\u0221\3\2\2\2c\u0228\3")
        buf.write("\2\2\2e\u0231\3\2\2\2g\u0235\3\2\2\2i\u0239\3\2\2\2k\u023b")
        buf.write("\3\2\2\2m\u023f\3\2\2\2o\u0241\3\2\2\2q\u0244\3\2\2\2")
        buf.write("s\u0247\3\2\2\2u\u0249\3\2\2\2w\u024b\3\2\2\2y\u024d\3")
        buf.write("\2\2\2{\u0250\3\2\2\2}\u0252\3\2\2\2\177\u0255\3\2\2\2")
        buf.write("\u0081\u0258\3\2\2\2\u0083\u025a\3\2\2\2\u0085\u025c\3")
        buf.write("\2\2\2\u0087\u025e\3\2\2\2\u0089\u0261\3\2\2\2\u008b\u0264")
        buf.write("\3\2\2\2\u008d\u0266\3\2\2\2\u008f\u0268\3\2\2\2\u0091")
        buf.write("\u026a\3\2\2\2\u0093\u026c\3\2\2\2\u0095\u026f\3\2\2\2")
        buf.write("\u0097\u0271\3\2\2\2\u0099\u0274\3\2\2\2\u009b\u0277\3")
        buf.write("\2\2\2\u009d\u0279\3\2\2\2\u009f\u027b\3\2\2\2\u00a1\u027e")
        buf.write("\3\2\2\2\u00a3\u0281\3\2\2\2\u00a5\u0284\3\2\2\2\u00a7")
        buf.write("\u0287\3\2\2\2\u00a9\u028a\3\2\2\2\u00ab\u028c\3\2\2\2")
        buf.write("\u00ad\u028f\3\2\2\2\u00af\u0292\3\2\2\2\u00b1\u0295\3")
        buf.write("\2\2\2\u00b3\u0298\3\2\2\2\u00b5\u029b\3\2\2\2\u00b7\u029e")
        buf.write("\3\2\2\2\u00b9\u02a1\3\2\2\2\u00bb\u02a4\3\2\2\2\u00bd")
        buf.write("\u02a7\3\2\2\2\u00bf\u02aa\3\2\2\2\u00c1\u02ae\3\2\2\2")
        buf.write("\u00c3\u02b2\3\2\2\2\u00c5\u02b6\3\2\2\2\u00c7\u02bd\3")
        buf.write("\2\2\2\u00c9\u02c1\3\2\2\2\u00cb\u02d5\3\2\2\2\u00cd\u02f1")
        buf.write("\3\2\2\2\u00cf\u02f5\3\2\2\2\u00d1\u02f7\3\2\2\2\u00d3")
        buf.write("\u02fd\3\2\2\2\u00d5\u02ff\3\2\2\2\u00d7\u0301\3\2\2\2")
        buf.write("\u00d9\u0303\3\2\2\2\u00db\u0305\3\2\2\2\u00dd\u0307\3")
        buf.write("\2\2\2\u00df\u0310\3\2\2\2\u00e1\u0314\3\2\2\2\u00e3\u0319")
        buf.write("\3\2\2\2\u00e5\u031d\3\2\2\2\u00e7\u0323\3\2\2\2\u00e9")
        buf.write("\u033e\3\2\2\2\u00eb\u035a\3\2\2\2\u00ed\u035e\3\2\2\2")
        buf.write("\u00ef\u0361\3\2\2\2\u00f1\u0364\3\2\2\2\u00f3\u0367\3")
        buf.write("\2\2\2\u00f5\u0369\3\2\2\2\u00f7\u036d\3\2\2\2\u00f9\u0371")
        buf.write("\3\2\2\2\u00fb\u0378\3\2\2\2\u00fd\u0383\3\2\2\2\u00ff")
        buf.write("\u0385\3\2\2\2\u0101\u0389\3\2\2\2\u0103\u038e\3\2\2\2")
        buf.write("\u0105\u0108\5Y-\2\u0106\u0108\5[.\2\u0107\u0105\3\2\2")
        buf.write("\2\u0107\u0106\3\2\2\2\u0108\4\3\2\2\2\u0109\u010d\5\7")
        buf.write("\4\2\u010a\u010d\5e\63\2\u010b\u010d\5g\64\2\u010c\u0109")
        buf.write("\3\2\2\2\u010c\u010a\3\2\2\2\u010c\u010b\3\2\2\2\u010d")
        buf.write("\6\3\2\2\2\u010e\u0113\5]/\2\u010f\u0113\5_\60\2\u0110")
        buf.write("\u0113\5a\61\2\u0111\u0113\5c\62\2\u0112\u010e\3\2\2\2")
        buf.write("\u0112\u010f\3\2\2\2\u0112\u0110\3\2\2\2\u0112\u0111\3")
        buf.write("\2\2\2\u0113\b\3\2\2\2\u0114\u0115\7c\2\2\u0115\u0116")
        buf.write("\7p\2\2\u0116\u0117\7f\2\2\u0117\n\3\2\2\2\u0118\u0119")
        buf.write("\7c\2\2\u0119\u011a\7u\2\2\u011a\f\3\2\2\2\u011b\u011c")
        buf.write("\7c\2\2\u011c\u011d\7u\2\2\u011d\u011e\7u\2\2\u011e\u011f")
        buf.write("\7g\2\2\u011f\u0120\7t\2\2\u0120\u0121\7v\2\2\u0121\16")
        buf.write("\3\2\2\2\u0122\u0123\7c\2\2\u0123\u0124\7u\2\2\u0124\u0125")
        buf.write("\7{\2\2\u0125\u0126\7p\2\2\u0126\u0127\7e\2\2\u0127\20")
        buf.write("\3\2\2\2\u0128\u0129\7c\2\2\u0129\u012a\7y\2\2\u012a\u012b")
        buf.write("\7c\2\2\u012b\u012c\7k\2\2\u012c\u012d\7v\2\2\u012d\22")
        buf.write("\3\2\2\2\u012e\u012f\7d\2\2\u012f\u0130\7t\2\2\u0130\u0131")
        buf.write("\7g\2\2\u0131\u0132\7c\2\2\u0132\u0133\7m\2\2\u0133\24")
        buf.write("\3\2\2\2\u0134\u0135\7e\2\2\u0135\u0136\7c\2\2\u0136\u0137")
        buf.write("\7u\2\2\u0137\u0138\7g\2\2\u0138\26\3\2\2\2\u0139\u013a")
        buf.write("\7e\2\2\u013a\u013b\7n\2\2\u013b\u013c\7c\2\2\u013c\u013d")
        buf.write("\7u\2\2\u013d\u013e\7u\2\2\u013e\30\3\2\2\2\u013f\u0140")
        buf.write("\7e\2\2\u0140\u0141\7q\2\2\u0141\u0142\7p\2\2\u0142\u0143")
        buf.write("\7v\2\2\u0143\u0144\7k\2\2\u0144\u0145\7p\2\2\u0145\u0146")
        buf.write("\7w\2\2\u0146\u0147\7g\2\2\u0147\32\3\2\2\2\u0148\u0149")
        buf.write("\7f\2\2\u0149\u014a\7g\2\2\u014a\u014b\7h\2\2\u014b\34")
        buf.write("\3\2\2\2\u014c\u014d\7f\2\2\u014d\u014e\7g\2\2\u014e\u014f")
        buf.write("\7n\2\2\u014f\36\3\2\2\2\u0150\u0151\7g\2\2\u0151\u0152")
        buf.write("\7n\2\2\u0152\u0153\7k\2\2\u0153\u0154\7h\2\2\u0154 \3")
        buf.write("\2\2\2\u0155\u0156\7g\2\2\u0156\u0157\7n\2\2\u0157\u0158")
        buf.write("\7u\2\2\u0158\u0159\7g\2\2\u0159\"\3\2\2\2\u015a\u015b")
        buf.write("\7g\2\2\u015b\u015c\7z\2\2\u015c\u015d\7e\2\2\u015d\u015e")
        buf.write("\7g\2\2\u015e\u015f\7r\2\2\u015f\u0160\7v\2\2\u0160$\3")
        buf.write("\2\2\2\u0161\u0162\7H\2\2\u0162\u0163\7c\2\2\u0163\u0164")
        buf.write("\7n\2\2\u0164\u0165\7u\2\2\u0165\u0166\7g\2\2\u0166&\3")
        buf.write("\2\2\2\u0167\u0168\7h\2\2\u0168\u0169\7k\2\2\u0169\u016a")
        buf.write("\7p\2\2\u016a\u016b\7c\2\2\u016b\u016c\7n\2\2\u016c\u016d")
        buf.write("\7n\2\2\u016d\u016e\7{\2\2\u016e(\3\2\2\2\u016f\u0170")
        buf.write("\7h\2\2\u0170\u0171\7q\2\2\u0171\u0172\7t\2\2\u0172*\3")
        buf.write("\2\2\2\u0173\u0174\7h\2\2\u0174\u0175\7t\2\2\u0175\u0176")
        buf.write("\7q\2\2\u0176\u0177\7o\2\2\u0177,\3\2\2\2\u0178\u0179")
        buf.write("\7i\2\2\u0179\u017a\7n\2\2\u017a\u017b\7q\2\2\u017b\u017c")
        buf.write("\7d\2\2\u017c\u017d\7c\2\2\u017d\u017e\7n\2\2\u017e.\3")
        buf.write("\2\2\2\u017f\u0180\7k\2\2\u0180\u0181\7h\2\2\u0181\60")
        buf.write("\3\2\2\2\u0182\u0183\7k\2\2\u0183\u0184\7o\2\2\u0184\u0185")
        buf.write("\7r\2\2\u0185\u0186\7q\2\2\u0186\u0187\7t\2\2\u0187\u0188")
        buf.write("\7v\2\2\u0188\62\3\2\2\2\u0189\u018a\7k\2\2\u018a\u018b")
        buf.write("\7p\2\2\u018b\64\3\2\2\2\u018c\u018d\7k\2\2\u018d\u018e")
        buf.write("\7u\2\2\u018e\66\3\2\2\2\u018f\u0190\7n\2\2\u0190\u0191")
        buf.write("\7c\2\2\u0191\u0192\7o\2\2\u0192\u0193\7d\2\2\u0193\u0194")
        buf.write("\7f\2\2\u0194\u0195\7c\2\2\u01958\3\2\2\2\u0196\u0197")
        buf.write("\7o\2\2\u0197\u0198\7c\2\2\u0198\u0199\7v\2\2\u0199\u019a")
        buf.write("\7e\2\2\u019a\u019b\7j\2\2\u019b:\3\2\2\2\u019c\u019d")
        buf.write("\7P\2\2\u019d\u019e\7q\2\2\u019e\u019f\7p\2\2\u019f\u01a0")
        buf.write("\7g\2\2\u01a0<\3\2\2\2\u01a1\u01a2\7p\2\2\u01a2\u01a3")
        buf.write("\7q\2\2\u01a3\u01a4\7p\2\2\u01a4\u01a5\7n\2\2\u01a5\u01a6")
        buf.write("\7q\2\2\u01a6\u01a7\7e\2\2\u01a7\u01a8\7c\2\2\u01a8\u01a9")
        buf.write("\7n\2\2\u01a9>\3\2\2\2\u01aa\u01ab\7p\2\2\u01ab\u01ac")
        buf.write("\7q\2\2\u01ac\u01ad\7v\2\2\u01ad@\3\2\2\2\u01ae\u01af")
        buf.write("\7q\2\2\u01af\u01b0\7t\2\2\u01b0B\3\2\2\2\u01b1\u01b2")
        buf.write("\7r\2\2\u01b2\u01b3\7c\2\2\u01b3\u01b4\7u\2\2\u01b4\u01b5")
        buf.write("\7u\2\2\u01b5D\3\2\2\2\u01b6\u01b7\7t\2\2\u01b7\u01b8")
        buf.write("\7c\2\2\u01b8\u01b9\7k\2\2\u01b9\u01ba\7u\2\2\u01ba\u01bb")
        buf.write("\7g\2\2\u01bbF\3\2\2\2\u01bc\u01bd\7t\2\2\u01bd\u01be")
        buf.write("\7g\2\2\u01be\u01bf\7v\2\2\u01bf\u01c0\7w\2\2\u01c0\u01c1")
        buf.write("\7t\2\2\u01c1\u01c2\7p\2\2\u01c2H\3\2\2\2\u01c3\u01c4")
        buf.write("\7V\2\2\u01c4\u01c5\7t\2\2\u01c5\u01c6\7w\2\2\u01c6\u01c7")
        buf.write("\7g\2\2\u01c7J\3\2\2\2\u01c8\u01c9\7v\2\2\u01c9\u01ca")
        buf.write("\7t\2\2\u01ca\u01cb\7{\2\2\u01cbL\3\2\2\2\u01cc\u01cd")
        buf.write("\7a\2\2\u01cdN\3\2\2\2\u01ce\u01cf\7y\2\2\u01cf\u01d0")
        buf.write("\7j\2\2\u01d0\u01d1\7k\2\2\u01d1\u01d2\7n\2\2\u01d2\u01d3")
        buf.write("\7g\2\2\u01d3P\3\2\2\2\u01d4\u01d5\7y\2\2\u01d5\u01d6")
        buf.write("\7k\2\2\u01d6\u01d7\7v\2\2\u01d7\u01d8\7j\2\2\u01d8R\3")
        buf.write("\2\2\2\u01d9\u01da\7{\2\2\u01da\u01db\7k\2\2\u01db\u01dc")
        buf.write("\7g\2\2\u01dc\u01dd\7n\2\2\u01dd\u01de\7f\2\2\u01deT\3")
        buf.write("\2\2\2\u01df\u01e0\6+\2\2\u01e0\u01ec\5\u00f7|\2\u01e1")
        buf.write("\u01e3\7\17\2\2\u01e2\u01e1\3\2\2\2\u01e2\u01e3\3\2\2")
        buf.write("\2\u01e3\u01e4\3\2\2\2\u01e4\u01e7\7\f\2\2\u01e5\u01e7")
        buf.write("\4\16\17\2\u01e6\u01e2\3\2\2\2\u01e6\u01e5\3\2\2\2\u01e7")
        buf.write("\u01e9\3\2\2\2\u01e8\u01ea\5\u00f7|\2\u01e9\u01e8\3\2")
        buf.write("\2\2\u01e9\u01ea\3\2\2\2\u01ea\u01ec\3\2\2\2\u01eb\u01df")
        buf.write("\3\2\2\2\u01eb\u01e6\3\2\2\2\u01ec\u01ed\3\2\2\2\u01ed")
        buf.write("\u01ee\b+\2\2\u01eeV\3\2\2\2\u01ef\u01f3\5\u0101\u0081")
        buf.write("\2\u01f0\u01f2\5\u0103\u0082\2\u01f1\u01f0\3\2\2\2\u01f2")
        buf.write("\u01f5\3\2\2\2\u01f3\u01f1\3\2\2\2\u01f3\u01f4\3\2\2\2")
        buf.write("\u01f4X\3\2\2\2\u01f5\u01f3\3\2\2\2\u01f6\u01fc\t\2\2")
        buf.write("\2\u01f7\u01f8\t\3\2\2\u01f8\u01fc\t\4\2\2\u01f9\u01fa")
        buf.write("\t\4\2\2\u01fa\u01fc\t\3\2\2\u01fb\u01f6\3\2\2\2\u01fb")
        buf.write("\u01f7\3\2\2\2\u01fb\u01f9\3\2\2\2\u01fb\u01fc\3\2\2\2")
        buf.write("\u01fc\u01ff\3\2\2\2\u01fd\u0200\5\u00cbf\2\u01fe\u0200")
        buf.write("\5\u00cdg\2\u01ff\u01fd\3\2\2\2\u01ff\u01fe\3\2\2\2\u0200")
        buf.write("Z\3\2\2\2\u0201\u0207\t\5\2\2\u0202\u0203\t\5\2\2\u0203")
        buf.write("\u0207\t\4\2\2\u0204\u0205\t\4\2\2\u0205\u0207\t\5\2\2")
        buf.write("\u0206\u0201\3\2\2\2\u0206\u0202\3\2\2\2\u0206\u0204\3")
        buf.write("\2\2\2\u0207\u020a\3\2\2\2\u0208\u020b\5\u00e9u\2\u0209")
        buf.write("\u020b\5\u00ebv\2\u020a\u0208\3\2\2\2\u020a\u0209\3\2")
        buf.write("\2\2\u020b\\\3\2\2\2\u020c\u0210\5\u00d5k\2\u020d\u020f")
        buf.write("\5\u00d7l\2\u020e\u020d\3\2\2\2\u020f\u0212\3\2\2\2\u0210")
        buf.write("\u020e\3\2\2\2\u0210\u0211\3\2\2\2\u0211\u0219\3\2\2\2")
        buf.write("\u0212\u0210\3\2\2\2\u0213\u0215\7\62\2\2\u0214\u0213")
        buf.write("\3\2\2\2\u0215\u0216\3\2\2\2\u0216\u0214\3\2\2\2\u0216")
        buf.write("\u0217\3\2\2\2\u0217\u0219\3\2\2\2\u0218\u020c\3\2\2\2")
        buf.write("\u0218\u0214\3\2\2\2\u0219^\3\2\2\2\u021a\u021b\7\62\2")
        buf.write("\2\u021b\u021d\t\6\2\2\u021c\u021e\5\u00d9m\2\u021d\u021c")
        buf.write("\3\2\2\2\u021e\u021f\3\2\2\2\u021f\u021d\3\2\2\2\u021f")
        buf.write("\u0220\3\2\2\2\u0220`\3\2\2\2\u0221\u0222\7\62\2\2\u0222")
        buf.write("\u0224\t\7\2\2\u0223\u0225\5\u00dbn\2\u0224\u0223\3\2")
        buf.write("\2\2\u0225\u0226\3\2\2\2\u0226\u0224\3\2\2\2\u0226\u0227")
        buf.write("\3\2\2\2\u0227b\3\2\2\2\u0228\u0229\7\62\2\2\u0229\u022b")
        buf.write("\t\5\2\2\u022a\u022c\5\u00ddo\2\u022b\u022a\3\2\2\2\u022c")
        buf.write("\u022d\3\2\2\2\u022d\u022b\3\2\2\2\u022d\u022e\3\2\2\2")
        buf.write("\u022ed\3\2\2\2\u022f\u0232\5\u00dfp\2\u0230\u0232\5\u00e1")
        buf.write("q\2\u0231\u022f\3\2\2\2\u0231\u0230\3\2\2\2\u0232f\3\2")
        buf.write("\2\2\u0233\u0236\5e\63\2\u0234\u0236\5\u00e3r\2\u0235")
        buf.write("\u0233\3\2\2\2\u0235\u0234\3\2\2\2\u0236\u0237\3\2\2\2")
        buf.write("\u0237\u0238\t\b\2\2\u0238h\3\2\2\2\u0239\u023a\7\60\2")
        buf.write("\2\u023aj\3\2\2\2\u023b\u023c\7\60\2\2\u023c\u023d\7\60")
        buf.write("\2\2\u023d\u023e\7\60\2\2\u023el\3\2\2\2\u023f\u0240\7")
        buf.write(",\2\2\u0240n\3\2\2\2\u0241\u0242\7*\2\2\u0242\u0243\b")
        buf.write("8\3\2\u0243p\3\2\2\2\u0244\u0245\7+\2\2\u0245\u0246\b")
        buf.write("9\4\2\u0246r\3\2\2\2\u0247\u0248\7.\2\2\u0248t\3\2\2\2")
        buf.write("\u0249\u024a\7<\2\2\u024av\3\2\2\2\u024b\u024c\7=\2\2")
        buf.write("\u024cx\3\2\2\2\u024d\u024e\7,\2\2\u024e\u024f\7,\2\2")
        buf.write("\u024fz\3\2\2\2\u0250\u0251\7?\2\2\u0251|\3\2\2\2\u0252")
        buf.write("\u0253\7]\2\2\u0253\u0254\b?\5\2\u0254~\3\2\2\2\u0255")
        buf.write("\u0256\7_\2\2\u0256\u0257\b@\6\2\u0257\u0080\3\2\2\2\u0258")
        buf.write("\u0259\7~\2\2\u0259\u0082\3\2\2\2\u025a\u025b\7`\2\2\u025b")
        buf.write("\u0084\3\2\2\2\u025c\u025d\7(\2\2\u025d\u0086\3\2\2\2")
        buf.write("\u025e\u025f\7>\2\2\u025f\u0260\7>\2\2\u0260\u0088\3\2")
        buf.write("\2\2\u0261\u0262\7@\2\2\u0262\u0263\7@\2\2\u0263\u008a")
        buf.write("\3\2\2\2\u0264\u0265\7-\2\2\u0265\u008c\3\2\2\2\u0266")
        buf.write("\u0267\7/\2\2\u0267\u008e\3\2\2\2\u0268\u0269\7\61\2\2")
        buf.write("\u0269\u0090\3\2\2\2\u026a\u026b\7\'\2\2\u026b\u0092\3")
        buf.write("\2\2\2\u026c\u026d\7\61\2\2\u026d\u026e\7\61\2\2\u026e")
        buf.write("\u0094\3\2\2\2\u026f\u0270\7\u0080\2\2\u0270\u0096\3\2")
        buf.write("\2\2\u0271\u0272\7}\2\2\u0272\u0273\bL\7\2\u0273\u0098")
        buf.write("\3\2\2\2\u0274\u0275\7\177\2\2\u0275\u0276\bM\b\2\u0276")
        buf.write("\u009a\3\2\2\2\u0277\u0278\7>\2\2\u0278\u009c\3\2\2\2")
        buf.write("\u0279\u027a\7@\2\2\u027a\u009e\3\2\2\2\u027b\u027c\7")
        buf.write("?\2\2\u027c\u027d\7?\2\2\u027d\u00a0\3\2\2\2\u027e\u027f")
        buf.write("\7@\2\2\u027f\u0280\7?\2\2\u0280\u00a2\3\2\2\2\u0281\u0282")
        buf.write("\7>\2\2\u0282\u0283\7?\2\2\u0283\u00a4\3\2\2\2\u0284\u0285")
        buf.write("\7>\2\2\u0285\u0286\7@\2\2\u0286\u00a6\3\2\2\2\u0287\u0288")
        buf.write("\7#\2\2\u0288\u0289\7?\2\2\u0289\u00a8\3\2\2\2\u028a\u028b")
        buf.write("\7B\2\2\u028b\u00aa\3\2\2\2\u028c\u028d\7/\2\2\u028d\u028e")
        buf.write("\7@\2\2\u028e\u00ac\3\2\2\2\u028f\u0290\7-\2\2\u0290\u0291")
        buf.write("\7?\2\2\u0291\u00ae\3\2\2\2\u0292\u0293\7/\2\2\u0293\u0294")
        buf.write("\7?\2\2\u0294\u00b0\3\2\2\2\u0295\u0296\7,\2\2\u0296\u0297")
        buf.write("\7?\2\2\u0297\u00b2\3\2\2\2\u0298\u0299\7B\2\2\u0299\u029a")
        buf.write("\7?\2\2\u029a\u00b4\3\2\2\2\u029b\u029c\7\61\2\2\u029c")
        buf.write("\u029d\7?\2\2\u029d\u00b6\3\2\2\2\u029e\u029f\7\'\2\2")
        buf.write("\u029f\u02a0\7?\2\2\u02a0\u00b8\3\2\2\2\u02a1\u02a2\7")
        buf.write("(\2\2\u02a2\u02a3\7?\2\2\u02a3\u00ba\3\2\2\2\u02a4\u02a5")
        buf.write("\7~\2\2\u02a5\u02a6\7?\2\2\u02a6\u00bc\3\2\2\2\u02a7\u02a8")
        buf.write("\7`\2\2\u02a8\u02a9\7?\2\2\u02a9\u00be\3\2\2\2\u02aa\u02ab")
        buf.write("\7>\2\2\u02ab\u02ac\7>\2\2\u02ac\u02ad\7?\2\2\u02ad\u00c0")
        buf.write("\3\2\2\2\u02ae\u02af\7@\2\2\u02af\u02b0\7@\2\2\u02b0\u02b1")
        buf.write("\7?\2\2\u02b1\u00c2\3\2\2\2\u02b2\u02b3\7,\2\2\u02b3\u02b4")
        buf.write("\7,\2\2\u02b4\u02b5\7?\2\2\u02b5\u00c4\3\2\2\2\u02b6\u02b7")
        buf.write("\7\61\2\2\u02b7\u02b8\7\61\2\2\u02b8\u02b9\7?\2\2\u02b9")
        buf.write("\u00c6\3\2\2\2\u02ba\u02be\5\u00f7|\2\u02bb\u02be\5\u00f9")
        buf.write("}\2\u02bc\u02be\5\u00fb~\2\u02bd\u02ba\3\2\2\2\u02bd\u02bb")
        buf.write("\3\2\2\2\u02bd\u02bc\3\2\2\2\u02be\u02bf\3\2\2\2\u02bf")
        buf.write("\u02c0\bd\t\2\u02c0\u00c8\3\2\2\2\u02c1\u02c2\13\2\2\2")
        buf.write("\u02c2\u00ca\3\2\2\2\u02c3\u02c8\7)\2\2\u02c4\u02c7\5")
        buf.write("\u00d3j\2\u02c5\u02c7\n\t\2\2\u02c6\u02c4\3\2\2\2\u02c6")
        buf.write("\u02c5\3\2\2\2\u02c7\u02ca\3\2\2\2\u02c8\u02c6\3\2\2\2")
        buf.write("\u02c8\u02c9\3\2\2\2\u02c9\u02cb\3\2\2\2\u02ca\u02c8\3")
        buf.write("\2\2\2\u02cb\u02d6\7)\2\2\u02cc\u02d1\7$\2\2\u02cd\u02d0")
        buf.write("\5\u00d3j\2\u02ce\u02d0\n\n\2\2\u02cf\u02cd\3\2\2\2\u02cf")
        buf.write("\u02ce\3\2\2\2\u02d0\u02d3\3\2\2\2\u02d1\u02cf\3\2\2\2")
        buf.write("\u02d1\u02d2\3\2\2\2\u02d2\u02d4\3\2\2\2\u02d3\u02d1\3")
        buf.write("\2\2\2\u02d4\u02d6\7$\2\2\u02d5\u02c3\3\2\2\2\u02d5\u02cc")
        buf.write("\3\2\2\2\u02d6\u00cc\3\2\2\2\u02d7\u02d8\7)\2\2\u02d8")
        buf.write("\u02d9\7)\2\2\u02d9\u02da\7)\2\2\u02da\u02de\3\2\2\2\u02db")
        buf.write("\u02dd\5\u00cfh\2\u02dc\u02db\3\2\2\2\u02dd\u02e0\3\2")
        buf.write("\2\2\u02de\u02df\3\2\2\2\u02de\u02dc\3\2\2\2\u02df\u02e1")
        buf.write("\3\2\2\2\u02e0\u02de\3\2\2\2\u02e1\u02e2\7)\2\2\u02e2")
        buf.write("\u02e3\7)\2\2\u02e3\u02f2\7)\2\2\u02e4\u02e5\7$\2\2\u02e5")
        buf.write("\u02e6\7$\2\2\u02e6\u02e7\7$\2\2\u02e7\u02eb\3\2\2\2\u02e8")
        buf.write("\u02ea\5\u00cfh\2\u02e9\u02e8\3\2\2\2\u02ea\u02ed\3\2")
        buf.write("\2\2\u02eb\u02ec\3\2\2\2\u02eb\u02e9\3\2\2\2\u02ec\u02ee")
        buf.write("\3\2\2\2\u02ed\u02eb\3\2\2\2\u02ee\u02ef\7$\2\2\u02ef")
        buf.write("\u02f0\7$\2\2\u02f0\u02f2\7$\2\2\u02f1\u02d7\3\2\2\2\u02f1")
        buf.write("\u02e4\3\2\2\2\u02f2\u00ce\3\2\2\2\u02f3\u02f6\5\u00d1")
        buf.write("i\2\u02f4\u02f6\5\u00d3j\2\u02f5\u02f3\3\2\2\2\u02f5\u02f4")
        buf.write("\3\2\2\2\u02f6\u00d0\3\2\2\2\u02f7\u02f8\n\13\2\2\u02f8")
        buf.write("\u00d2\3\2\2\2\u02f9\u02fa\7^\2\2\u02fa\u02fe\13\2\2\2")
        buf.write("\u02fb\u02fc\7^\2\2\u02fc\u02fe\5U+\2\u02fd\u02f9\3\2")
        buf.write("\2\2\u02fd\u02fb\3\2\2\2\u02fe\u00d4\3\2\2\2\u02ff\u0300")
        buf.write("\t\f\2\2\u0300\u00d6\3\2\2\2\u0301\u0302\t\r\2\2\u0302")
        buf.write("\u00d8\3\2\2\2\u0303\u0304\t\16\2\2\u0304\u00da\3\2\2")
        buf.write("\2\u0305\u0306\t\17\2\2\u0306\u00dc\3\2\2\2\u0307\u0308")
        buf.write("\t\20\2\2\u0308\u00de\3\2\2\2\u0309\u030b\5\u00e3r\2\u030a")
        buf.write("\u0309\3\2\2\2\u030a\u030b\3\2\2\2\u030b\u030c\3\2\2\2")
        buf.write("\u030c\u0311\5\u00e5s\2\u030d\u030e\5\u00e3r\2\u030e\u030f")
        buf.write("\7\60\2\2\u030f\u0311\3\2\2\2\u0310\u030a\3\2\2\2\u0310")
        buf.write("\u030d\3\2\2\2\u0311\u00e0\3\2\2\2\u0312\u0315\5\u00e3")
        buf.write("r\2\u0313\u0315\5\u00dfp\2\u0314\u0312\3\2\2\2\u0314\u0313")
        buf.write("\3\2\2\2\u0315\u0316\3\2\2\2\u0316\u0317\5\u00e7t\2\u0317")
        buf.write("\u00e2\3\2\2\2\u0318\u031a\5\u00d7l\2\u0319\u0318\3\2")
        buf.write("\2\2\u031a\u031b\3\2\2\2\u031b\u0319\3\2\2\2\u031b\u031c")
        buf.write("\3\2\2\2\u031c\u00e4\3\2\2\2\u031d\u031f\7\60\2\2\u031e")
        buf.write("\u0320\5\u00d7l\2\u031f\u031e\3\2\2\2\u0320\u0321\3\2")
        buf.write("\2\2\u0321\u031f\3\2\2\2\u0321\u0322\3\2\2\2\u0322\u00e6")
        buf.write("\3\2\2\2\u0323\u0325\t\21\2\2\u0324\u0326\t\22\2\2\u0325")
        buf.write("\u0324\3\2\2\2\u0325\u0326\3\2\2\2\u0326\u0328\3\2\2\2")
        buf.write("\u0327\u0329\5\u00d7l\2\u0328\u0327\3\2\2\2\u0329\u032a")
        buf.write("\3\2\2\2\u032a\u0328\3\2\2\2\u032a\u032b\3\2\2\2\u032b")
        buf.write("\u00e8\3\2\2\2\u032c\u0331\7)\2\2\u032d\u0330\5\u00ef")
        buf.write("x\2\u032e\u0330\5\u00f5{\2\u032f\u032d\3\2\2\2\u032f\u032e")
        buf.write("\3\2\2\2\u0330\u0333\3\2\2\2\u0331\u032f\3\2\2\2\u0331")
        buf.write("\u0332\3\2\2\2\u0332\u0334\3\2\2\2\u0333\u0331\3\2\2\2")
        buf.write("\u0334\u033f\7)\2\2\u0335\u033a\7$\2\2\u0336\u0339\5\u00f1")
        buf.write("y\2\u0337\u0339\5\u00f5{\2\u0338\u0336\3\2\2\2\u0338\u0337")
        buf.write("\3\2\2\2\u0339\u033c\3\2\2\2\u033a\u0338\3\2\2\2\u033a")
        buf.write("\u033b\3\2\2\2\u033b\u033d\3\2\2\2\u033c\u033a\3\2\2\2")
        buf.write("\u033d\u033f\7$\2\2\u033e\u032c\3\2\2\2\u033e\u0335\3")
        buf.write("\2\2\2\u033f\u00ea\3\2\2\2\u0340\u0341\7)\2\2\u0341\u0342")
        buf.write("\7)\2\2\u0342\u0343\7)\2\2\u0343\u0347\3\2\2\2\u0344\u0346")
        buf.write("\5\u00edw\2\u0345\u0344\3\2\2\2\u0346\u0349\3\2\2\2\u0347")
        buf.write("\u0348\3\2\2\2\u0347\u0345\3\2\2\2\u0348\u034a\3\2\2\2")
        buf.write("\u0349\u0347\3\2\2\2\u034a\u034b\7)\2\2\u034b\u034c\7")
        buf.write(")\2\2\u034c\u035b\7)\2\2\u034d\u034e\7$\2\2\u034e\u034f")
        buf.write("\7$\2\2\u034f\u0350\7$\2\2\u0350\u0354\3\2\2\2\u0351\u0353")
        buf.write("\5\u00edw\2\u0352\u0351\3\2\2\2\u0353\u0356\3\2\2\2\u0354")
        buf.write("\u0355\3\2\2\2\u0354\u0352\3\2\2\2\u0355\u0357\3\2\2\2")
        buf.write("\u0356\u0354\3\2\2\2\u0357\u0358\7$\2\2\u0358\u0359\7")
        buf.write("$\2\2\u0359\u035b\7$\2\2\u035a\u0340\3\2\2\2\u035a\u034d")
        buf.write("\3\2\2\2\u035b\u00ec\3\2\2\2\u035c\u035f\5\u00f3z\2\u035d")
        buf.write("\u035f\5\u00f5{\2\u035e\u035c\3\2\2\2\u035e\u035d\3\2")
        buf.write("\2\2\u035f\u00ee\3\2\2\2\u0360\u0362\t\23\2\2\u0361\u0360")
        buf.write("\3\2\2\2\u0362\u00f0\3\2\2\2\u0363\u0365\t\24\2\2\u0364")
        buf.write("\u0363\3\2\2\2\u0365\u00f2\3\2\2\2\u0366\u0368\t\25\2")
        buf.write("\2\u0367\u0366\3\2\2\2\u0368\u00f4\3\2\2\2\u0369\u036a")
        buf.write("\7^\2\2\u036a\u036b\t\26\2\2\u036b\u00f6\3\2\2\2\u036c")
        buf.write("\u036e\t\27\2\2\u036d\u036c\3\2\2\2\u036e\u036f\3\2\2")
        buf.write("\2\u036f\u036d\3\2\2\2\u036f\u0370\3\2\2\2\u0370\u00f8")
        buf.write("\3\2\2\2\u0371\u0375\7%\2\2\u0372\u0374\n\30\2\2\u0373")
        buf.write("\u0372\3\2\2\2\u0374\u0377\3\2\2\2\u0375\u0373\3\2\2\2")
        buf.write("\u0375\u0376\3\2\2\2\u0376\u00fa\3\2\2\2\u0377\u0375\3")
        buf.write("\2\2\2\u0378\u037a\7^\2\2\u0379\u037b\5\u00f7|\2\u037a")
        buf.write("\u0379\3\2\2\2\u037a\u037b\3\2\2\2\u037b\u0381\3\2\2\2")
        buf.write("\u037c\u037e\7\17\2\2\u037d\u037c\3\2\2\2\u037d\u037e")
        buf.write("\3\2\2\2\u037e\u037f\3\2\2\2\u037f\u0382\7\f\2\2\u0380")
        buf.write("\u0382\4\16\17\2\u0381\u037d\3\2\2\2\u0381\u0380\3\2\2")
        buf.write("\2\u0382\u00fc\3\2\2\2\u0383\u0384\t\31\2\2\u0384\u00fe")
        buf.write("\3\2\2\2\u0385\u0386\t\32\2\2\u0386\u0100\3\2\2\2\u0387")
        buf.write("\u038a\t\33\2\2\u0388\u038a\5\u00fd\177\2\u0389\u0387")
        buf.write("\3\2\2\2\u0389\u0388\3\2\2\2\u038a\u0102\3\2\2\2\u038b")
        buf.write("\u038f\5\u0101\u0081\2\u038c\u038f\t\34\2\2\u038d\u038f")
        buf.write("\5\u00ff\u0080\2\u038e\u038b\3\2\2\2\u038e\u038c\3\2\2")
        buf.write("\2\u038e\u038d\3\2\2\2\u038f\u0104\3\2\2\2<\2\u0107\u010c")
        buf.write("\u0112\u01e2\u01e6\u01e9\u01eb\u01f3\u01fb\u01ff\u0206")
        buf.write("\u020a\u0210\u0216\u0218\u021f\u0226\u022d\u0231\u0235")
        buf.write("\u02bd\u02c6\u02c8\u02cf\u02d1\u02d5\u02de\u02eb\u02f1")
        buf.write("\u02f5\u02fd\u030a\u0310\u0314\u031b\u0321\u0325\u032a")
        buf.write("\u032f\u0331\u0338\u033a\u033e\u0347\u0354\u035a\u035e")
        buf.write("\u0361\u0364\u0367\u036f\u0375\u037a\u037d\u0381\u0389")
        buf.write("\u038e\n\3+\2\38\3\39\4\3?\5\3@\6\3L\7\3M\b\b\2\2")
        return buf.getvalue()


class Python3Lexer(Python3LexerBase):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INDENT = 1
    DEDENT = 2
    STRING = 3
    NUMBER = 4
    INTEGER = 5
    AND = 6
    AS = 7
    ASSERT = 8
    ASYNC = 9
    AWAIT = 10
    BREAK = 11
    CASE = 12
    CLASS = 13
    CONTINUE = 14
    DEF = 15
    DEL = 16
    ELIF = 17
    ELSE = 18
    EXCEPT = 19
    FALSE = 20
    FINALLY = 21
    FOR = 22
    FROM = 23
    GLOBAL = 24
    IF = 25
    IMPORT = 26
    IN = 27
    IS = 28
    LAMBDA = 29
    MATCH = 30
    NONE = 31
    NONLOCAL = 32
    NOT = 33
    OR = 34
    PASS = 35
    RAISE = 36
    RETURN = 37
    TRUE = 38
    TRY = 39
    UNDERSCORE = 40
    WHILE = 41
    WITH = 42
    YIELD = 43
    NEWLINE = 44
    NAME = 45
    STRING_LITERAL = 46
    BYTES_LITERAL = 47
    DECIMAL_INTEGER = 48
    OCT_INTEGER = 49
    HEX_INTEGER = 50
    BIN_INTEGER = 51
    FLOAT_NUMBER = 52
    IMAG_NUMBER = 53
    DOT = 54
    ELLIPSIS = 55
    STAR = 56
    OPEN_PAREN = 57
    CLOSE_PAREN = 58
    COMMA = 59
    COLON = 60
    SEMI_COLON = 61
    POWER = 62
    ASSIGN = 63
    OPEN_BRACK = 64
    CLOSE_BRACK = 65
    OR_OP = 66
    XOR = 67
    AND_OP = 68
    LEFT_SHIFT = 69
    RIGHT_SHIFT = 70
    ADD = 71
    MINUS = 72
    DIV = 73
    MOD = 74
    IDIV = 75
    NOT_OP = 76
    OPEN_BRACE = 77
    CLOSE_BRACE = 78
    LESS_THAN = 79
    GREATER_THAN = 80
    EQUALS = 81
    GT_EQ = 82
    LT_EQ = 83
    NOT_EQ_1 = 84
    NOT_EQ_2 = 85
    AT = 86
    ARROW = 87
    ADD_ASSIGN = 88
    SUB_ASSIGN = 89
    MULT_ASSIGN = 90
    AT_ASSIGN = 91
    DIV_ASSIGN = 92
    MOD_ASSIGN = 93
    AND_ASSIGN = 94
    OR_ASSIGN = 95
    XOR_ASSIGN = 96
    LEFT_SHIFT_ASSIGN = 97
    RIGHT_SHIFT_ASSIGN = 98
    POWER_ASSIGN = 99
    IDIV_ASSIGN = 100
    SKIP_ = 101
    UNKNOWN_CHAR = 102

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'and'", "'as'", "'assert'", "'async'", "'await'", "'break'", 
            "'case'", "'class'", "'continue'", "'def'", "'del'", "'elif'", 
            "'else'", "'except'", "'False'", "'finally'", "'for'", "'from'", 
            "'global'", "'if'", "'import'", "'in'", "'is'", "'lambda'", 
            "'match'", "'None'", "'nonlocal'", "'not'", "'or'", "'pass'", 
            "'raise'", "'return'", "'True'", "'try'", "'_'", "'while'", 
            "'with'", "'yield'", "'.'", "'...'", "'*'", "'('", "')'", "','", 
            "':'", "';'", "'**'", "'='", "'['", "']'", "'|'", "'^'", "'&'", 
            "'<<'", "'>>'", "'+'", "'-'", "'/'", "'%'", "'//'", "'~'", "'{'", 
            "'}'", "'<'", "'>'", "'=='", "'>='", "'<='", "'<>'", "'!='", 
            "'@'", "'->'", "'+='", "'-='", "'*='", "'@='", "'/='", "'%='", 
            "'&='", "'|='", "'^='", "'<<='", "'>>='", "'**='", "'//='" ]

    symbolicNames = [ "<INVALID>",
            "INDENT", "DEDENT", "STRING", "NUMBER", "INTEGER", "AND", "AS", 
            "ASSERT", "ASYNC", "AWAIT", "BREAK", "CASE", "CLASS", "CONTINUE", 
            "DEF", "DEL", "ELIF", "ELSE", "EXCEPT", "FALSE", "FINALLY", 
            "FOR", "FROM", "GLOBAL", "IF", "IMPORT", "IN", "IS", "LAMBDA", 
            "MATCH", "NONE", "NONLOCAL", "NOT", "OR", "PASS", "RAISE", "RETURN", 
            "TRUE", "TRY", "UNDERSCORE", "WHILE", "WITH", "YIELD", "NEWLINE", 
            "NAME", "STRING_LITERAL", "BYTES_LITERAL", "DECIMAL_INTEGER", 
            "OCT_INTEGER", "HEX_INTEGER", "BIN_INTEGER", "FLOAT_NUMBER", 
            "IMAG_NUMBER", "DOT", "ELLIPSIS", "STAR", "OPEN_PAREN", "CLOSE_PAREN", 
            "COMMA", "COLON", "SEMI_COLON", "POWER", "ASSIGN", "OPEN_BRACK", 
            "CLOSE_BRACK", "OR_OP", "XOR", "AND_OP", "LEFT_SHIFT", "RIGHT_SHIFT", 
            "ADD", "MINUS", "DIV", "MOD", "IDIV", "NOT_OP", "OPEN_BRACE", 
            "CLOSE_BRACE", "LESS_THAN", "GREATER_THAN", "EQUALS", "GT_EQ", 
            "LT_EQ", "NOT_EQ_1", "NOT_EQ_2", "AT", "ARROW", "ADD_ASSIGN", 
            "SUB_ASSIGN", "MULT_ASSIGN", "AT_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", 
            "AND_ASSIGN", "OR_ASSIGN", "XOR_ASSIGN", "LEFT_SHIFT_ASSIGN", 
            "RIGHT_SHIFT_ASSIGN", "POWER_ASSIGN", "IDIV_ASSIGN", "SKIP_", 
            "UNKNOWN_CHAR" ]

    ruleNames = [ "STRING", "NUMBER", "INTEGER", "AND", "AS", "ASSERT", 
                  "ASYNC", "AWAIT", "BREAK", "CASE", "CLASS", "CONTINUE", 
                  "DEF", "DEL", "ELIF", "ELSE", "EXCEPT", "FALSE", "FINALLY", 
                  "FOR", "FROM", "GLOBAL", "IF", "IMPORT", "IN", "IS", "LAMBDA", 
                  "MATCH", "NONE", "NONLOCAL", "NOT", "OR", "PASS", "RAISE", 
                  "RETURN", "TRUE", "TRY", "UNDERSCORE", "WHILE", "WITH", 
                  "YIELD", "NEWLINE", "NAME", "STRING_LITERAL", "BYTES_LITERAL", 
                  "DECIMAL_INTEGER", "OCT_INTEGER", "HEX_INTEGER", "BIN_INTEGER", 
                  "FLOAT_NUMBER", "IMAG_NUMBER", "DOT", "ELLIPSIS", "STAR", 
                  "OPEN_PAREN", "CLOSE_PAREN", "COMMA", "COLON", "SEMI_COLON", 
                  "POWER", "ASSIGN", "OPEN_BRACK", "CLOSE_BRACK", "OR_OP", 
                  "XOR", "AND_OP", "LEFT_SHIFT", "RIGHT_SHIFT", "ADD", "MINUS", 
                  "DIV", "MOD", "IDIV", "NOT_OP", "OPEN_BRACE", "CLOSE_BRACE", 
                  "LESS_THAN", "GREATER_THAN", "EQUALS", "GT_EQ", "LT_EQ", 
                  "NOT_EQ_1", "NOT_EQ_2", "AT", "ARROW", "ADD_ASSIGN", "SUB_ASSIGN", 
                  "MULT_ASSIGN", "AT_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", 
                  "AND_ASSIGN", "OR_ASSIGN", "XOR_ASSIGN", "LEFT_SHIFT_ASSIGN", 
                  "RIGHT_SHIFT_ASSIGN", "POWER_ASSIGN", "IDIV_ASSIGN", "SKIP_", 
                  "UNKNOWN_CHAR", "SHORT_STRING", "LONG_STRING", "LONG_STRING_ITEM", 
                  "LONG_STRING_CHAR", "STRING_ESCAPE_SEQ", "NON_ZERO_DIGIT", 
                  "DIGIT", "OCT_DIGIT", "HEX_DIGIT", "BIN_DIGIT", "POINT_FLOAT", 
                  "EXPONENT_FLOAT", "INT_PART", "FRACTION", "EXPONENT", 
                  "SHORT_BYTES", "LONG_BYTES", "LONG_BYTES_ITEM", "SHORT_BYTES_CHAR_NO_SINGLE_QUOTE", 
                  "SHORT_BYTES_CHAR_NO_DOUBLE_QUOTE", "LONG_BYTES_CHAR", 
                  "BYTES_ESCAPE_SEQ", "SPACES", "COMMENT", "LINE_JOINING", 
                  "UNICODE_OIDS", "UNICODE_OIDC", "ID_START", "ID_CONTINUE" ]

    grammarFileName = "Python3Lexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[41] = self.NEWLINE_action 
            actions[54] = self.OPEN_PAREN_action 
            actions[55] = self.CLOSE_PAREN_action 
            actions[61] = self.OPEN_BRACK_action 
            actions[62] = self.CLOSE_BRACK_action 
            actions[74] = self.OPEN_BRACE_action 
            actions[75] = self.CLOSE_BRACE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def NEWLINE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            this.onNewLine();
     

    def OPEN_PAREN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            this.openBrace();
     

    def CLOSE_PAREN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            this.closeBrace();
     

    def OPEN_BRACK_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            this.openBrace();
     

    def CLOSE_BRACK_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            this.closeBrace();
     

    def OPEN_BRACE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            this.openBrace();
     

    def CLOSE_BRACE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:
            this.closeBrace();
     

    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates is None:
            preds = dict()
            preds[41] = self.NEWLINE_sempred
            self._predicates = preds
        pred = self._predicates.get(ruleIndex, None)
        if pred is not None:
            return pred(localctx, predIndex)
        else:
            raise Exception("No registered predicate for:" + str(ruleIndex))

    def NEWLINE_sempred(self, localctx:RuleContext, predIndex:int):
            if predIndex == 0:
                return this.atStartOfInput()
         


