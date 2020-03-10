import com.altairix.adf.root.batch.BatchCommand;
import com.altairix.adf.root.command.HasRemoteCommand;
import com.altairix.comm.adf.qnaire.obj.qnaire.QnaireLong;
import com.altairix.comm.adf.root.log.fields.Lobj;
import com.altairix.comm.adf.root.trace.Trace;
import com.altairix.comm.adf.root.util.ArgSet;

public class Load~@{Template} extends BatchCommand implements HasRemoteCommand {

   public static final String USAGE =
      "Usage: Load~@{Template} version=? [VERBOSE]";

  public static final String ARG_VERSION = "version";
  public static final String ARG_VERBOSE = "VERBOSE";

  public static void main(String[] args) {
    new Load~@{Template}().innerMain(args, true);
  }

  @Override
  public void runBatchCommand(String[] args) {

    initLoggerTracer();

    Lobj lobj = new Lobj(new Lobj("Usage", USAGE), new Lobj("Args", args));

    ArgSet argSet = new ArgSet(args);

    // Resolve help version
    String version = argSet.pullValue(ARG_VERSION);
    if (version == null) {
      tracer.trace("Syntax error: {}", getRequestSyntax(args));
      tracer.trace(USAGE);
      throw new RuntimeException(logger.error(lobj,
          "Missing required Parameter({})", ARG_VERSION));
    }

    // Resolve other options
    boolean verboseFg = argSet.pullOption(ARG_VERBOSE);

    // Check for unknown input args
    if (!argSet.isEmpty()) {
      tracer.trace("Syntax error: {}", getRequestSyntax(args));
      tracer.trace(USAGE);
      throw new RuntimeException(
          logger.error(lobj, "Unsupported input parameters({})", args.toString()));
    }

    // Log all input args
    tracer.trace(ARG_VERSION + "=" + version);
    tracer.trace(ARG_VERBOSE + "=" + (verboseFg ? "TRUE" : "FALSE"));

    // Turn on verbose tracing if required
    if (verboseFg) {
      Trace.setUserVerbose(verboseFg);
    }

	// TODO Implement this
  }
}
