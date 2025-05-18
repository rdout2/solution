export interface Application {
  id: number;
  jobTitle: string;
  company: string;
  status: ApplicationStatus;
  date: string;
  logo?: string;
}

export type ApplicationStatus = 'Wishlist' | 'Applied' | 'Interview' | 'Offer' | 'Rejected';

export interface GroupedApplications {
  Wishlist: Application[];
  Applied: Application[];
  Interview: Application[];
  Offer: Application[];
  Rejected: Application[];
}