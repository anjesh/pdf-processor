from AbbyyOnlineSdk import *

class AbbyyPdfTextExtractor:
    def __init__(self, indir, outdir, pages, language):
        self.processor = AbbyyOnlineSdk()
        self.processor.ApplicationId = "user"
        self.processor.Password = "password"
        self.outputFormat = 'txt'
        self.language = language
        self.indir = indir
        self.pages = pages
        self.outdir = outdir
    
    def processPdfPage(self, page):
        """
        all the pdf in outdir are named as 1.pdf, 2.pdf based on the page numbers
        """
        infile = os.path.join(self.indir, "%d.pdf" % page)
        outfile = os.path.join(self.outdir, "%d.txt" % page)
        settings = ProcessingSettings()
        settings.Language = self.language
        settings.OutputFormat = self.outputFormat

        task = self.processor.ProcessImage(infile, settings)
        if task == None:
            print "Error"
            return
        print "Id = %s" % task.Id
        print "Status = %s" % task.Status

        # Wait for the task to be completed
        sys.stdout.write( "Waiting.." )
        # Note: it's recommended that your application waits at least 2 seconds
        # before making the first getTaskStatus request and also between such requests
        # for the same task. Making requests more often will not improve your
        # application performance.
        # Note: if your application queues several files and waits for them
        # it's recommended that you use listFinishedTasks instead (which is described
        # at http://ocrsdk.com/documentation/apireference/listFinishedTasks/).

        while task.IsActive() == True :
            time.sleep( 5 )
            sys.stdout.write( "." )
            task = self.processor.GetTaskStatus(task)

        print "Status = %s" % task.Status
        
        if task.Status == "Completed":
            if task.DownloadUrl != None:
                self.processor.DownloadResult(task, outfile)
                print "Result was written to %s" % outfile
        else:
            print "Error processing task"

    def extractPages(self):
        for page in range(1, self.pages+1):
            self.processPdfPage(page)
