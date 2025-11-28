import argparse
import logging
logger = logging.getLogger(__name__)

from gwr_links_to_calendar import parse_table, read_pdf, write_csv


if __name__ == "__main__":

    # Command line args
    parser = argparse.ArgumentParser()
    # Required args
    parser.add_argument("-i", "--input", help="path to input .pdf timetable file", required=True)
    parser.add_argument("-n", "--name", help="name of person as shown on the timetable (eg. \'S MACKENZIE\')", required=True)
    # Optional args
    parser.add_argument("-o", "--output", help="path to output .csv file. Default: \'shifts.csv\'", default="shifts.csv")
    parser.add_argument("-w", "--num-weeks", help="number of weeks of events to create. Default behaviour is as many weeks as there are rows in the relevant table.", type=int, default=None)
    parser.add_argument("-d", "--debug", help="enables debug mode (provides extra additional output)", action="store_const", dest="loglevel", const=logging.DEBUG, default=logging.INFO)
    # Parse
    args = parser.parse_args()

    logging.basicConfig(level=args.loglevel)

    logger.debug(f"{args.input=}")
    logger.debug(f"{args.name=}")
    logger.debug(f"{args.output=}")
    logger.debug(f"{args.num_weeks=}")
    logger.debug(f"{args.loglevel=}")

    # Open pdf
    pdf_text = read_pdf.read_pdf(args.input)
    logger.info(f"Opened input file \'{args.input}\'")

    name_found_on_page = None
    for i in range(len(pdf_text)):
        page = pdf_text[i]

        if args.name in page:
            name_found_on_page = i+1

            logger.info(f"Found name \'{args.name}\' on page {name_found_on_page}")

            commencing_date = parse_table.parse_commencing_date(page)
            logger.info(f"Found commencing date {commencing_date}")

            lines = parse_table.filter_page(page)
            parsed_lines = parse_table.offset_start_row_from_name(
                [parse_table.parse_table_row(l) for l in lines],
                args.name
            )
            logger.info(f"Successfully parsed input file")

            shifts = parse_table.create_schedule(parsed_lines, commencing_date, args.num_weeks)
            n_weeks = args.num_weeks if args.num_weeks is not None else len(parsed_lines)
            logger.info(f"Found {len(shifts)} shifts across {n_weeks} weeks")
            for s in shifts:
                logger.debug(f"Found shift {s.to_str()}")
            
            write_csv.write_csv(args.output, [s.to_output_dict() for s in shifts])
            logger.info(f"Wrote output to \'{args.output}\'")

            break
        
        logger.debug(f"Name \'{args.name}\' not found on page {i+1}")
    
    if name_found_on_page is None:
        logger.error(f"Name \'{args.name}\' was not found in the timetable. Please check the spelling and capitalisation")
