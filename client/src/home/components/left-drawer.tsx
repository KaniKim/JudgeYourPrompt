import {
  Dialog,
  DialogBackdrop,
  DialogPanel,
  DialogTitle,
  TransitionChild,
} from '@headlessui/react';
import CloseIcon from '@mui/icons-material/Close';
import { RootState } from '../../store/store';
import { useDispatch, useSelector } from 'react-redux';
import { openerActions } from '../../store';

export const Drawer = () => {
  const dispatch = useDispatch();
  const open = useSelector((state: RootState) => state.open.value);
  return (
    <Dialog
      open={open}
      onClose={() => dispatch(openerActions.close())}
      className='relative z-10'
    >
      <DialogBackdrop
        transition
        className="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity duration-500 ease-in-out data-[closed]:opacity-0"
      />

      <div className="fixed top-0 left-0 inset-0 overflow-hidden">
        <div className="absolute inset-0 overflow-hidden">
          <div className="pointer-events-none fixed inset-y-0 left-0 flex max-w-full">
            <DialogPanel
              transition
              className="pointer-events-auto relative pt-16 min-w-64 transform transition duration-500 ease-in-out data-[closed]:-translate-x-full sm:duration-700"
            >
              <TransitionChild>
                <div className="absolute left-0 top-0 flex pt-4 duration-500 ease-in-out data-[closed]:opacity-0 ">
                  <button
                    type="button"
                    onClick={() => dispatch(openerActions.close())}
                    className="relative rounded-md text-gray-300 hover:text-white focus:outline-none focus:ring-2 focus:ring-white"
                  >
                    <span className="absolute -inset-2.5" />
                    <span className="sr-only">Close panel</span>
                    <CloseIcon aria-hidden="true" className="h-6 w-6" />
                  </button>
                </div>
              </TransitionChild>
              <div className="flex h-full flex-col overflow-y-scroll bg-white py-6 shadow-xl">
                <div className="px-4 sm:px-6">
                  <DialogTitle className="text-xl text-center font-semibold leading-6 text-gray-900">
                    내가 쓴 글 보기
                  </DialogTitle>
                </div>
                <div className="relative mt-6 flex-1 px-4 sm:px-6"></div>
              </div>
            </DialogPanel>
          </div>
        </div>
      </div>
    </Dialog>
  );
};
